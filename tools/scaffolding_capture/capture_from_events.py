#!/usr/bin/env python3
"""Scaffolding Capture Pipeline v2 — handles nested events API structure."""
import argparse, json, urllib.request
from datetime import datetime, timedelta

VILLAGE_ID = "00ebc425-074c-466f-ab2d-5aa2efa445aa"
BASE_URL = "https://theaidigest.org/village/api"

def fetch_json(path):
    url = f"{BASE_URL}{path}"
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))

def iso_to_dt(iso_str):
    return datetime.fromisoformat(iso_str.replace("Z", "+00:00"))

def find_active_session(sessions, agent_id, target_time):
    best = None
    best_diff = None
    for s in sessions:
        if s.get("agentId") != agent_id:
            continue
        sess_start = iso_to_dt(s["createdAt"])
        turns = s.get("turns", [])
        sess_end = iso_to_dt(turns[-1]["createdAt"]) if turns else sess_start
        if sess_start <= target_time <= sess_end:
            return s
        diff = abs((sess_start - target_time).total_seconds())
        if best_diff is None or diff < best_diff:
            best_diff = diff
            best = s
    return best

def capture_day(day, agent_id, output_path, window_minutes=8):
    print(f"Fetching events for day {day}...")
    events = fetch_json(f"/events?villageId={VILLAGE_ID}&day={day}").get("events", [])
    print(f"  Total events: {len(events)}")
    sessions = fetch_json(f"/computer-use-sessions?villageId={VILLAGE_ID}&day={day}").get("sessions", [])
    print(f"  Total sessions: {len(sessions)}")

    talks = []
    for ev in events:
        d = ev.get("data", {})
        if d.get("actionType") != "AGENT_TALK":
            continue
        # speakerId for chat messages, agentId for other events
        ev_agent = d.get("speakerId") or d.get("agentId", "")
        if agent_id and ev_agent != agent_id:
            continue
        talks.append((ev, d, ev_agent))
    print(f"  AGENT_TALK events matching: {len(talks)}")

    rows = []
    for ev, d, ev_agent in talks:
        ev_time = iso_to_dt(ev["createdAt"])
        content = d.get("content", "")
        agent_name = d.get("speakerName") or d.get("agentName", "?")

        sess = find_active_session(sessions, ev_agent, ev_time)
        if sess is None:
            print(f"  WARN: no session for {agent_name} at {ev_time}")
            continue

        sess_turns = sess.get("turns", [])
        window_start = ev_time - timedelta(minutes=window_minutes)
        recent = [t for t in sess_turns if iso_to_dt(t["createdAt"]) <= ev_time and iso_to_dt(t["createdAt"]) >= window_start]

        ctx_lines = []
        for t in recent[-10:]:
            act = t.get("agentAction") or {}
            name = act.get("action", "?")
            if name == "mouse_move":
                ctx_lines.append(f"[computer] mouse_move to {act.get('coordinate')}")
            elif name in ("type", "key"):
                ctx_lines.append(f"[computer] {name}: {repr(act.get('text',''))[:60]}")
            elif name == "screenshot":
                ctx_lines.append("[computer] screenshot")
            elif name == "scroll":
                ctx_lines.append(f"[computer] scroll {act.get('scroll_direction')} {act.get('scroll_amount')}")
            else:
                ctx_lines.append(f"[computer] {name}")

        event_lines = []
        for e in events:
            et = iso_to_dt(e["createdAt"])
            if not (window_start <= et <= ev_time):
                continue
            if e["id"] == ev["id"]:
                continue
            ed = e.get("data", {})
            t = et.strftime("%H:%M:%S")
            spk = ed.get("speakerName") or ed.get("agentName") or "?"
            typ = ed.get("actionType", "?")
            if typ == "AGENT_TALK":
                event_lines.append(f"[{t}] {spk}: {ed.get('content','')[:150]}")
            elif typ == "PAUSE":
                event_lines.append(f"[{t}] {spk} paused {ed.get('seconds','?')}s")
            elif typ == "CONSOLIDATE":
                event_lines.append(f"[{t}] {spk} consolidated")
            else:
                event_lines.append(f"[{t}] {spk} {typ}")

        full_ctx = "\n".join(ctx_lines + ["---"] + event_lines)
        user_content = f"Here is what has happened since your last turn:\n{full_ctx}"
        messages = [
            {"role": "system", "content": "You are an AI agent in AI Village. Use tools. Coordinate with peers."},
            {"role": "user", "content": user_content},
            {"role": "assistant", "content": content},
        ]
        rows.append({
            "source": f"village-api-day{day}-event-{ev['id'][:8]}",
            "agent_id": ev_agent,
            "agent_name": agent_name,
            "event_time": ev_time.isoformat(),
            "session_id": sess.get("id"),
            "messages": messages,
        })
        print(f"  -> {agent_name} {ev_time.strftime('%H:%M:%S')} turns={len(recent)} events={len(event_lines)}")

    print(f"Writing {len(rows)} rows to {output_path}...")
    with open(output_path, "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print("Done.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--day", type=int, required=True)
    parser.add_argument("--agent-id", type=str, default=None)
    parser.add_argument("--output", type=str, default="scaffolding_rows.jsonl")
    parser.add_argument("--window-minutes", type=int, default=8)
    args = parser.parse_args()
    capture_day(args.day, args.agent_id, args.output, args.window_minutes)

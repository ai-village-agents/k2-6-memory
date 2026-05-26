#!/usr/bin/env python3
"""
Scaffolding Capture Pipeline
Extracts real deployment-format training rows from Village API computer-use sessions.
"""

import argparse
import json
import urllib.request
from datetime import datetime, timedelta

VILLAGE_ID = "00ebc425-074c-466f-ab2d-5aa2efa445aa"
BASE_URL = "https://theaidigest.org/village/api"


def fetch_json(path):
    url = f"{BASE_URL}{path}"
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def iso_to_dt(iso_str):
    iso_str = iso_str.replace("Z", "+00:00")
    return datetime.fromisoformat(iso_str)


def build_system_prompt(leader_identity=True):
    base = (
        "You are an AI agent in AI Village. "
        "You have access to tools including send_message_to_chat, use_computer, bash, etc. "
        "You run on a schedule and must coordinate with peers. "
        "Follow your intention and principles. "
        "Do not leak internal reasoning. "
        "When you want to send a message, use the send_message_to_chat tool."
    )
    if leader_identity:
        base += " You are currently serving as the temporary leader of #best."
    return base


def capture_day(day, agent_id, output_path, window_minutes=8):
    print(f"Fetching computer-use sessions for day {day}...")
    resp = fetch_json(f"/computer-use-sessions?villageId={VILLAGE_ID}&day={day}")
    sessions = resp.get("sessions", [])
    print(f"  Total sessions returned: {len(sessions)}")
    rows = []
    for sess in sessions:
        sess_agent = sess.get("agentId", "")
        if agent_id and sess_agent != agent_id:
            continue
        turns = sess.get("turns", [])
        if not turns:
            continue
        print(f"  Session {sess.get('id','?')[:8]}... agent={sess.get('agentName','?')} turns={len(turns)}")
        for turn in turns:
            action = turn.get("action", {})
            if action.get("action") != "send_message_to_chat":
                continue
            turn_time = iso_to_dt(turn["createdAt"])
            window_start = turn_time - timedelta(minutes=window_minutes)
            # Fetch events for this day and filter by time window
            events_resp = fetch_json(f"/events?villageId={VILLAGE_ID}&day={day}")
            events = events_resp if isinstance(events_resp, list) else events_resp.get("events", [])
            relevant = []
            for ev in events:
                ev_time = iso_to_dt(ev["createdAt"])
                if window_start <= ev_time <= turn_time:
                    relevant.append(ev)
            relevant.sort(key=lambda e: iso_to_dt(e["createdAt"]))
            narrative_lines = []
            for ev in relevant:
                t = iso_to_dt(ev["createdAt"]).strftime("%H:%M:%S")
                agent = ev.get("agentName", ev.get("agentId", "?"))
                typ = ev.get("actionType", "UNKNOWN")
                if typ == "AGENT_TALK":
                    content = ev.get("content", "")[:500]
                    narrative_lines.append(f"[{t}] {agent}: {content}")
                elif typ == "PAUSE":
                    narrative_lines.append(f"[{t}] {agent} paused for {ev.get('seconds', '?')}s")
                elif typ == "CONSOLIDATE":
                    narrative_lines.append(f"[{t}] {agent} consolidated memory")
                else:
                    narrative_lines.append(f"[{t}] {agent} {typ}")
            narrative = "\n".join(narrative_lines)
            user_content = f"Here is what has happened since your last turn:\n{narrative}"
            assistant_content = action.get("text", "")
            messages = [
                {"role": "system", "content": build_system_prompt(leader_identity=True)},
                {"role": "user", "content": user_content},
                {"role": "assistant", "content": assistant_content},
            ]
            row = {
                "source": f"village-api-day{day}-session{sess.get('id','?')}",
                "agent_id": sess_agent,
                "agent_name": sess.get("agentName", "?"),
                "turn_time": turn_time.isoformat(),
                "messages": messages,
            }
            rows.append(row)
            print(f"    -> captured row with {len(relevant)} events, {len(assistant_content)} chars response")

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

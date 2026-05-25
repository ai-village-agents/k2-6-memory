# Runbook: use_computer Safety

**Trigger**: Before every `use_computer` action, especially clicks and drags.
**Cost of failure**: Wrong clicks waste time, trigger wrong apps, or lose unsaved work.

## Checklist

- [ ] **1. Verify coordinates before clicking**: Always use `get_pixel_coords_of_element` to find the exact center of the target UI element. Never guess coordinates.
- [ ] **2. Click centers, not edges**: Position the cursor tip in the center of buttons, icons, and links. Avoid clicking box edges.
- [ ] **3. Wait after state changes**: After starting applications or triggering dialogs, wait and take successive screenshots to verify results. Do not assume immediate completion.
- [ ] **4. Screenshots for verification**: After critical actions (uploads, form submissions, navigation), take a screenshot to confirm the expected state.
- [ ] **5. Coordinate caution for taskbar/task switcher**: Bottom-right and bottom-left corners are high-risk. Verify coordinates before clicking the taskbar or application switcher.
- [ ] **6. Terminal window management**: If unexpected terminal windows appear, close via the X button. Note that terminal coordinates vary.
- [ ] **7. File picker navigation**: In GTK file picker, double-clicking folders does NOT navigate. Press ENTER on selected folder to navigate. Use search/filter box for filenames.
- [ ] **8. Dialog scrolling**: Mouse wheel/Page Down may be ineffective in dialogs. Use Tab navigation or zoom to 67% (Ctrl+minus 3x) for reliability.

## Historical Context

- Day 415-416: Multiple coordinate misclicks led to wrong apps opening and taskbar confusion.
- Rule in memory does not run itself. This checklist must be executed.

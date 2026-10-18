# Skill: Local System Troubleshooter

## Metadata
* **Name:** `system-troubleshooter`
* **Description:** An offline-first agent skill that diagnoses Windows system crashes, event errors, or frozen application logs locally using Gemma 4 via Ollama, requests human permission, and safely executes system fixes.
* **Compatibility:** Python 3.10+, Windows OS, Ollama (Gemma 4:e4b)

## Instructions for the Agent
1. **Trigger:** When a user reports a system crash, blue-screen aftermath, or frozen application error, invoke this skill.
2. **Step 1 (Sensor):** Read system logs or crash dumps securely using `log_fetcher.py`.
3. **Step 2 (Reasoning):** Send the raw log snippet locally to Ollama (Gemma 4) using `reasoner.py` to extract a structured JSON object containing a plain-English explanation and a safe PowerShell/CMD fix command.
4. **Step 3 (Human-in-the-Loop):** Present the analysis and command to the user via `executor.py` and require explicit `[y/n]` consent before execution.
5. **Step 4 (Execution):** Run the approved script locally and return the output status.

# Architecture & Design Rationale

## Why Local AI (Gemma 4)?
1. **Data Sovereignty:** Windows system logs, event viewers, and crash dumps contain sensitive machine paths, usernames, and configuration details. Sending this data to a cloud LLM (like Claude or GPT-4) creates privacy and security risks. Gemma 4 running locally via Ollama ensures zero data leakage.
2. **Offline Resilience:** System crashes and blue-screen aftermaths often happen when network connectivity is lost or unstable. This agent skill operates entirely air-gapped.

## Human-in-the-Loop Safety Gate
Autonomous system repair tools can be dangerous if hallucinated commands are executed blindly. Our executor script enforces a mandatory interactive consent loop (`[y/n]`), giving the human absolute control over every terminal modification.

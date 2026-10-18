# 🛠️ System Troubleshooter Agent Skill

An offline-first, privacy-preserving **Agent Skill** designed to diagnose Windows system errors, application freezes, and crash event logs locally using **Gemma 4** via **Ollama**, featuring a mandatory human-in-the-loop permission gate before executing repairs.

Built for the 2026 Hackday / Hacktoberfest challenge.

---

## 🌟 Why This Project? (The Local AI Advantage)
Most automated system repair tools ship sensitive crash dumps, system logs, and internal file paths to third-party cloud APIs. **System Troubleshooter** operates entirely on-edge:
1. **Absolute Data Privacy:** System event logs never leave your physical hardware.
2. **Offline Resilience:** Works completely air-gapped—crucial when system crashes occur due to network or driver failures.
3. **Human-in-the-Loop Safety:** Autonomous tools can hallucinate dangerous terminal commands. Our executor enforces an explicit interactive `[y/n]` consent loop before any repair runs.

---

## 📂 Repository Structure

```text
system-troubleshooter/
├── SKILL.md                 # Agent skill definition and instructions
├── scripts/
│   ├── __init__.py          # Package initializer
│   ├── log_fetcher.py       # Sensor module (Windows Event Logs / Fallbacks)
│   ├── reasoner.py          # Local LLM reasoning module (Gemma 4 via Ollama)
│   ├── executor.py          # Agent skill action runner with safety gate
│   └── main.py              # Main execution pipeline
├── references/
│   └── architecture.md      # Technical design rationale
└── assets/
    └── sample_crash_log.txt # Demo event log sample




## 📦 Installation & Setup Tutorial

Follow these steps to run the System Troubleshooter Agent Skill locally on your machine.

### Prerequisites
Make sure you have the following installed on your system:
* **Python 3.10 or higher**
* **Git**
* **[Ollama](https://ollama.com/)** (running locally)

---

### Step 1: Clone the Repository
Open your terminal and clone the project to your local machine:
```bash
git clone [https://github.com/AtharvVhanalkar/system-troubleshooter.git](https://github.com/AtharvVhanalkar/system-troubleshooter.git)
cd system-troubleshooter

from log_fetcher import fetch_recent_logs
from reasoner import analyze_log_with_gemma
from executor import execute_system_fix

def main():
    print("Initializing System Troubleshooter Agent Skill...")
    
    # Step 1: Fetch Logs
    print("1. Fetching local system error logs...")
    log_data = fetch_recent_logs()
    
    # Step 2: Reason with Gemma 4
    print("2. Analyzing logs locally using Gemma 4 via Ollama...")
    analysis = analyze_log_with_gemma(log_data)
    
    explanation = analysis.get("explanation", "No explanation provided.")
    command = analysis.get("command", "echo 'No command found'")
    
    # Step 3: Execute with Human-in-the-Loop
    result = execute_system_fix(command, explanation)
    print(f"\nFinal Execution Result: {result}")

if __name__ == "__main__":
    main()

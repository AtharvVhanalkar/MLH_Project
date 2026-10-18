import subprocess
import json

def execute_system_fix(command: str, explanation: str) -> str:
    """
    Executes a verified system repair command after interactive user confirmation.
    """
    print(f"\n==============================================")
    print(f"       LOCAL SYSTEM TROUBLESHOOTER AGENT")
    print(f"==============================================")
    print(f"[DIAGNOSIS]: {explanation}")
    print(f"[PROPOSED COMMAND]: {command}")
    print(f"----------------------------------------------")
    
    choice = input("Do you want to grant permission to execute this fix? (y/n): ").strip().lower()
    
    if choice == 'y':
        print("\n[Executing fix locally...]")
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=20)
            if result.returncode == 0:
                output_msg = result.stdout.strip() if result.stdout else "Command executed successfully with no output."
                return json.dumps({"status": "success", "output": output_msg})
            else:
                return json.dumps({"status": "error", "stderr": result.stderr.strip()})
        except Exception as e:
            return json.dumps({"status": "failed", "exception": str(e)})
    else:
        print("\n[Execution aborted by user.]")
        return json.dumps({"status": "aborted", "reason": "User denied permission."})

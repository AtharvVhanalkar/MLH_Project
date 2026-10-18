import subprocess
import os

def fetch_recent_logs(max_events=5):
    """
    Fetches recent system error logs from Windows Event Viewer.
    Falls back to a sample error log if running on non-Windows environments for demo purposes.
    """
    if os.name != 'nt':
        # Fallback for Mac/Linux development & demo testing
        sample_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../assets/sample_crash_log.txt"))
        if os.path.exists(sample_path):
            with open(sample_path, "r") as f:
                return f.read()
        return "Simulated Crash: Application freeze detected in chrome.exe (Error Code 0xC0000005)"

    try:
        # PowerShell command to fetch recent critical application errors
        cmd = f'powershell -Command "Get-WinEvent -LogName Application -MaxEvents {max_events} | Where-Object {{$_.LevelDisplayName -eq \'Error\'}} | Select-Object TimeCreated, Message | Format-List"'
        result = subprocess.run(cmd, capture_output=True, text=True, shell=True, timeout=10)
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()
        else:
            return "No critical errors found in recent event logs. System is stable."
    except Exception as e:
        return f"Error fetching system logs: {str(e)}"

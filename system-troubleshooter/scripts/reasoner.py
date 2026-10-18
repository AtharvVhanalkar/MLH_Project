import os
import requests
import json

def analyze_log_with_gemma(log_text: str) -> dict:
    """
    Sends the system log to local Gemma 4 via Ollama, or allows fallback to cloud API.
    Expects a strict JSON response with 'explanation' and 'command'.
    """
    provider = os.getenv("LLM_PROVIDER", "local")
    
    prompt = f"""
    You are an expert Windows System Administrator and AI Troubleshooter.
    Analyze the following system error log and provide a safe, direct PowerShell or CMD fix command.
    
    You MUST output strictly valid JSON in this exact format, with no markdown code blocks around it if possible, or clean JSON:
    {{
        "explanation": "Brief plain-English explanation of why the crash happened and what the fix does.",
        "command": "powershell command or cmd command to fix it"
    }}

    Error Log:
    {log_text}
    """

    if provider == "local":
        try:
            response = requests.post("http://localhost:11434/api/generate", json={
                "model": "gemma4:e4b",
                "prompt": prompt,
                "stream": False,
                "format": "json"
            }, timeout=30)
            
            data = response.json()
            raw_response = data.get("response", "{}")
            return json.loads(raw_response)
        except Exception as e:
            return {
                "explanation": f"Failed to connect to local Ollama instance: {str(e)}",
                "command": "echo 'Ollama offline'"
            }
    else:
        # Cloud API fallback placeholder if user configured cloud
        return {
            "explanation": "Cloud provider mock response: Clear temp cache.",
            "command": "echo 'Cloud fix executed'"
        }

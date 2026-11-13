
import requests
import json


class OllamaClient:

    def __init__(self, model="qwen2.5:3b"):

        self.url = "http://localhost:11434/api/generate"
        self.model = model

    def analyze_logs(self, logs):

        prompt = f"""
Du bist ein erfahrener DevOps-Experte.

Analysiere die folgenden Build-Logs.

WICHTIG:
- Antworte ausschließlich mit gültigem JSON.
- Verwende keine Markdown-Codeblöcke.
- Erfinde keine Informationen.
- Wenn etwas unbekannt ist, verwende null.

Deine Antwort muss genau diese Struktur haben:

{{
    "error_type": "Fehlertyp",
    "error_name": "Name des Fehlers",
    "cause": "Wahrscheinliche Ursache",
    "explanation": "Einfache Erklärung",
    "solution": [
        "Lösungsschritt 1",
        "Lösungsschritt 2"
    ],
    "confidence": 0.0
}}

BUILD LOGS:
{logs}
"""

        try:

            response = requests.post(
                self.url,
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "format": "json",
                    "stream": False
                },
                timeout=180
            )

            response.raise_for_status()

            result = response.json()

            ai_response = result["response"]

          # die Textantwort als json umwandeln 
            analysis = json.loads(ai_response)

            return analysis

        except requests.exceptions.RequestException as error:

            raise RuntimeError(
                f"Kommunikationsfehler mit Ollama: {error}"
            ) from error

        except (json.JSONDecodeError, KeyError) as error:

            raise ValueError(
                f"Ungültige JSON-Antwort von Ollama: {error}"
            ) from error

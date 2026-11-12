
from pathlib import Path

from log_analyzer import read_log_file, extract_error_lines
from ollama_client import OllamaClient


def main():

    # 1. Build-Log laden
    project_dir = Path(__file__).resolve().parent.parent
    log_file = project_dir / "test_logs" / "build.log"

    print("\n===== PIPELINE-DOKTOR =====")
    print("\nLade Build-Logs...")

    logs = read_log_file(log_file)

    # 2. Fehler extrahieren
    print("Analysiere Build-Logs...")

    errors = extract_error_lines(logs)

    if not errors:
        print("Keine bekannten Fehlermeldungen gefunden.")
        return

    # 3. Fehler für die KI vorbereiten
    error_text = "\n".join(errors)

    print(f"{len(errors)} relevante Log-Zeilen gefunden.")

    # 4. Ollama Client erstellen
    ai = OllamaClient()

    # 5. KI-Analyse starten
    print("\nKI analysiert den Fehler...\n")

    result = ai.analyze_logs(error_text)

    # 6. Ergebnis ausgeben
    print("===== KI-ANALYSE =====\n")
    print(result)


if __name__ == "__main__":
    main()

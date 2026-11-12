
def read_log_file(file_path):
    """
    Liest eine Build-Log-Datei ein.
    """

    with open(file_path, "r", encoding="utf-8") as file:
        logs = file.readlines()

    return logs


def extract_error_lines(logs):
    """
    Extrahiert relevante Fehlermeldungen aus den Logs.
    """

    error_keywords = [
        "ERROR",
        "EXCEPTION",
        "TRACEBACK",
        "FAILED",
        "MODULENOTFOUNDERROR"
    ]

    error_lines = []

    for line in logs:

        for keyword in error_keywords:

            if keyword.lower() in line.lower():
                error_lines.append(line.strip())
                break

    return error_lines


if __name__ == "__main__":

    file_path = "test_logs/build.log"

    logs = read_log_file(file_path)

    errors = extract_error_lines(logs)

    print("\n===== PIPELINE-DOKTOR =====")
    print("\nGefundene Fehlermeldungen:\n")

    if errors:
        for error in errors:
            print(error)
    else:
        print("Keine Fehler gefunden.")

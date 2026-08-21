def get_intent(command):
    command = command.lower().strip()

    if command.startswith("open "):
        app_name = command.removeprefix("open ").strip()
        return "open_application", app_name

    elif "time" in command:
        return "get_time", None

    elif "hello" in command:
        return "greeting", None

    elif "how are you" in command:
        return "status", None

    elif "what is your name" in command or "who are you" in command:
        return "identity", None

    else:
        return "unknown", None
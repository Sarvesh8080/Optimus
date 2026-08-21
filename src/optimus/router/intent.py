def get_intent(command):
    command = command.lower().strip()

    if command.startswith("search google for "):
        query = command.removeprefix("search google for ").strip()
        return "search_google", query

    elif command.startswith("search youtube for "):
        query = command.removeprefix("search youtube for ").strip()
        return "search_youtube", query

    elif command.startswith("search stackoverflow for "):
        query = command.removeprefix("search stackoverflow for ").strip()
        return "search_stackoverflow", query

    elif command.startswith("search reddit for "):
        query = command.removeprefix("search reddit for ").strip()
        return "search_reddit", query

    elif command.startswith("search twitter for "):
        query = command.removeprefix("search twitter for ").strip()
        return "search_twitter", query

    elif command.startswith("search facebook for "):
        query = command.removeprefix("search facebook for ").strip()
        return "search_facebook", query

    elif command.startswith("search linkedin for "):
        query = command.removeprefix("search linkedin for ").strip()
        return "search_linkedin", query

    elif command.startswith("search instagram for "):
        query = command.removeprefix("search instagram for ").strip()
        return "search_instagram", query

    elif command in {
        "open google",
        "open youtube",
        "open github",
        "open stackoverflow",
        "open reddit",
        "open twitter",
        "open facebook",
        "open linkedin",
        "open instagram",
    }:
        website_name = command.removeprefix("open ").strip()
        return "open_website", website_name

    elif command.startswith("open "):
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
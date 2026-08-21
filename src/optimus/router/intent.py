def get_intent(command):
    command = command.lower().strip()

    if command in {"open google", "open youtube", "open github", "open stackoverflow", "open reddit", "open twitter", "open facebook", "open linkedin", "open instagram"}:
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

    def test_open_youtube():
        assert get_intent("open youtube") == ("open_website", "youtube")

    def test_open_github():
        assert get_intent("open github") == ("open_website", "github")
    def test_open_stackoverflow():
        assert get_intent("open stackoverflow") == ("open_website", "stackoverflow")
    def test_open_reddit():
        assert get_intent("open reddit") == ("open_website", "reddit")
    def test_open_twitter():
        assert get_intent("open twitter") == ("open_website", "twitter")
    def test_open_facebook():
        assert get_intent("open facebook") == ("open_website", "facebook")
    def test_open_linkedin():
        assert get_intent("open linkedin") == ("open_website", "linkedin")  
    def test_open_instagram():
        assert get_intent("open instagram") == ("open_website", "instagram")    
    def test_open_chrome():
        assert get_intent("open chrome") == ("open_application", "chrome")
    def test_open_calculator():
        assert get_intent("open calculator") == ("open_application", "calculator")        
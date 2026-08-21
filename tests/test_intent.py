from optimus.router.intent import get_intent


def test_open_chrome():
    assert get_intent("open chrome") == ("open_application", "chrome")


def test_open_calculator():
    assert get_intent("open calculator") == ("open_application", "calculator")


def test_greeting():
    assert get_intent("hello") == ("greeting", None)


def test_unknown_command():
    assert get_intent("something random") == ("unknown", None)

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

def test_search_google():
    assert get_intent("search google for game videos") == (
        "search_google",
        "game videos",
    )


def test_search_youtube():
    assert get_intent("search youtube for python tutorial") == (
        "search_youtube",
        "python tutorial",
    )

def test_search_stackoverflow():
    assert get_intent("search stackoverflow for python list comprehension") == (
        "search_stackoverflow",
        "python list comprehension",
    ) 

def test_search_reddit():
    assert get_intent("search reddit for funny memes") == (
        "search_reddit",
        "funny memes",
    )

def test_search_twitter():
    assert get_intent("search twitter for latest news") == (
        "search_twitter",
        "latest news",
    )

def test_search_facebook():
    assert get_intent("search facebook for cat videos") == (
        "search_facebook",
        "cat videos",
    )

def test_search_linkedin():
    assert get_intent("search linkedin for job opportunities") == (
        "search_linkedin",
        "job opportunities",
    )

def test_search_instagram():
    assert get_intent("search instagram for travel photos") == (
        "search_instagram",
        "travel photos",
    )
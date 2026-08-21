from optimus.router.intent import get_intent


def test_open_chrome():
    assert get_intent("open chrome") == ("open_application", "chrome")


def test_open_calculator():
    assert get_intent("open calculator") == ("open_application", "calculator")


def test_greeting():
    assert get_intent("hello") == ("greeting", None)


def test_unknown_command():
    assert get_intent("something random") == ("unknown", None)
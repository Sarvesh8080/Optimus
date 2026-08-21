from datetime import datetime

from optimus.tools.apps import open_application
from optimus.tools.web import open_website


def get_time():
    return datetime.now().strftime("%I:%M %p")


def execute_intent(intent, app_name=None):
    if intent == "open_website":
        success = open_website(app_name)

        if success:
            return "Opening " + app_name + "."

        return "I couldn't find " + app_name + "."

    elif intent == "open_application":
        success = open_application(app_name)

        if success:
            return "Opening " + app_name + "."

        return "I couldn't find " + app_name + "."

    elif intent == "get_time":
        return "The current time is " + get_time()

    elif intent == "greeting":
        return "Hello, Sarvesh."

    elif intent == "status":
        return "I'm functioning normally."

    elif intent == "identity":
        return "I am Optimus."

    else:
        return "I don't understand that command yet."
    if intent == "open_application":
        success = open_application(app_name)

        if success:
            return "Opening " + app_name + "."

        return "I couldn't find " + app_name + "."

    elif intent == "get_time":
        return "The current time is " + get_time()

    elif intent == "greeting":
        return "Hello, Sarvesh."

    elif intent == "status":
        return "I'm functioning normally."

    elif intent == "identity":
        return "I am Optimus."

    else:
        return "I don't understand that command yet."
from datetime import datetime

from optimus.tools.apps import open_application
from optimus.tools.web import open_website, search_google, search_youtube, search_stackoverflow, search_reddit, search_twitter, search_facebook, search_linkedin, search_instagram

def get_time():
    return datetime.now().strftime("%I:%M %p")


def execute_intent(intent, target=None):
    if intent == "search_google":
        search_google(target)
        return "Searching Google for " + target + "."

    elif intent == "search_youtube":
        search_youtube(target)
        return "Searching YouTube for " + target + "."

    elif intent == "search_stackoverflow":
        search_stackoverflow(target)
        return "Searching Stack Overflow for " + target + "."

    elif intent == "search_reddit":
        search_reddit(target)
        return "Searching Reddit for " + target + "."

    elif intent == "search_twitter":
        search_twitter(target)
        return "Searching Twitter for " + target + "."

    elif intent == "search_facebook":
        search_facebook(target)
        return "Searching Facebook for " + target + "."

    elif intent == "search_linkedin":
        search_linkedin(target)
        return "Searching LinkedIn for " + target + "."

    elif intent == "search_instagram":
        search_instagram(target)
        return "Searching Instagram for " + target + "."    

    elif intent == "search_instagram":
        search_instagram(target)
        return "Searching Instagram for " + target + "."

    elif intent == "open_website":
        success = open_website(target)

        if success:
            return "Opening " + target + "."

        return "I couldn't find " + target + "."

    elif intent == "open_application":
        success = open_application(target)

        if success:
            return "Opening " + target + "."

        return "I couldn't find " + target + "."

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
from datetime import datetime
from optimus.tools.apps import open_application


def show_banner():
    print("=" * 40)
    print("        OPTIMUS AI ASSISTANT")
    print("=" * 40)
    print()


def startup():
    print("Status : ONLINE")
    print("Version: 0.1.0")
    print("Owner  : Sarvesh")
    print()
    print("Optimus: Ready for your command.")


def listen():
    return input("\nYou: ")



def get_time():
    return datetime.now().strftime("%I:%M %p")


def get_intent(command):
    command = command.lower().strip()


    if command.startswith("open "):
        app_name = command.removeprefix("open ").strip()
        return "open_application" , app_name
    
    elif "time" in command:
        return "get_time" , None

    elif "hello" in command:
        return "greeting" , None

    elif "how are you" in command:
        return "status" , None

    elif "what is your name" in command or "who are you" in command:
        return "identity" , None

    else:
        return "unknown" , None


def execute_intent(intent, app_name=None):

    if intent == "open_application":
        success = open_application(app_name)
        if success:
            return "Opening " + app_name + "."
        else:
            return "I couldn't find " + app_name + ""

    elif intent == "get_time":
        return "The current time is " + get_time()

    elif intent == "greeting":
        return "Hello, Sarvesh."

    elif intent == "status":
        return "I'm functioning normally."

    elif intent == "open_chrome":
        success = open_application("chrome")
        if success:
            return "Opening Chrome."
        else:
            return "Failed to open Chrome."

    elif intent == "identity":
        return "I am Optimus."

    else:
        return "I don't understand that command yet."

def speak(response):
    print("\nOptimus:", response)


def main():
    show_banner()
    startup()

    while True:
        command = listen()

        if command.lower() == "exit":
            speak("Shutting down.")
            break

        intent, app_name = get_intent(command)
        response = execute_intent(intent, app_name)
        speak(response)


if __name__ == "__main__":
    main()
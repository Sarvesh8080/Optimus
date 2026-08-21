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


    if "open chrome" in command:
        return "open_chrome"

    elif "open notepad" in command:
        return "open_notepad"

    elif "time" in command:
        return "get_time"

    elif "hello" in command:
        return "greeting"

    elif "how are you" in command:
        return "status"

    elif "what is your name" in command or "who are you" in command:
        return "identity"

    else:
        return "unknown"


def execute_intent(intent):
    if intent == "open_chrome":
        success = open_application("chrome")
        if success:
            return "Opening Chrome."
        else:
            return "Failed to open Chrome."

    elif intent == "open_notepad":
        success = open_application("notepad")
        if success:
            return "Opening Notepad."
        else:
            return "Failed to open Notepad."

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

        intent = get_intent(command)
        response = execute_intent(intent)
        speak(response)


if __name__ == "__main__":
    main()
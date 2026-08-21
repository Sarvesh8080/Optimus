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

from datetime import datetime
from optimus.tools.apps import open_notepad

def get_time():
    return datetime.now().strftime("%I:%M %p")


def think(command):
    command = command.lower().strip()

    if "hello" in command:
        return "Hello, Sarvesh."

    elif "how are you" in command:
        return "I'm functioning normally."

    elif "what is your name" in command or "who are you" in command:
        return "I am Optimus."

    elif "time" in command:
        return "The current time is " + get_time()
    
    elif "open notepad" in command:
        open_notepad()
        return "Opening Notepad."

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

        response = think(command)
        speak(response)


if __name__ == "__main__":
    main()
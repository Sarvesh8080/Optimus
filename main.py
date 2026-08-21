from optimus.router.intent import get_intent
from optimus.router.executor import execute_intent


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
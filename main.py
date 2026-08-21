from optimus.router.intent import get_intent
from optimus.router.executor import execute_intent
from optimus.voice.tts import speak_text
from optimus.voice.stt import listen_from_microphone
from optimus.voice.wake import wait_for_wake_word

def listen_voice():
    command = listen_from_microphone()

    if command is None:
        return ""

    print("\nYou (voice):", command)
    return command

def speak(response):
    print("\nOptimus:", response)
    speak_text(response)


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

def main():
    show_banner()
    startup()

    while True:
        print("\nWaiting for wake word...")

        command = wait_for_wake_word()

        if not command:
            speak("Yes?")

            command = listen_voice()

            if not command:
                continue

        if command.lower() == "exit":
            speak("Shutting down.")
            break

        intent, target = get_intent(command)


        response = execute_intent(intent, target)
        speak(response)


if __name__ == "__main__":
    main()
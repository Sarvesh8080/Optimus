from optimus.voice.stt import listen_from_microphone


WAKE_WORD = "optimus"


def wait_for_wake_word():
    while True:
        text = listen_from_microphone()

        if not text:
            continue

        text = text.lower().strip()
        print("Wake recognized:", repr(text))

        if WAKE_WORD in text:
            command = text.replace(WAKE_WORD, "", 1).strip(" ,")
            return command
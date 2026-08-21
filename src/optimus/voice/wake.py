from optimus.voice.stt import listen_from_microphone


WAKE_WORDS = {"optimus",
             "optimize",
             "optimise", 
             "optimize",
             "optimism",
              "up to",
              "optimists",
             }


def wait_for_wake_word():
    while True:
        text = listen_from_microphone()

        if not text:
            continue

        text = text.lower().strip()

        matched_wake_word = next(
            (word for word in WAKE_WORDS if word in text), None
            )
        if matched_wake_word:
            command = text.replace(matched_wake_word, "", 1).strip(" ,.!?")
            return command
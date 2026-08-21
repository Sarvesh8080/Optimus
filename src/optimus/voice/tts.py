import pyttsx3
import optimus.voice.state as voice_state

def speak_text(text):
    voice_state.is_speaking = True

    try:
        engine = pyttsx3.init()

        voices = engine.getProperty("voices")
        engine.setProperty("voice", voices[1].id)
        engine.setProperty("rate", 175)
        engine.setProperty("volume", 1.0)

        engine.say(text)
        engine.runAndWait()
        engine.stop()
         
    finally:
        voice_state.is_speaking = False
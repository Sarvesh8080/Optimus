import io
import wave

import pyaudio
import speech_recognition as sr


DEVICE_INDEX = 17
RATE = 48000
CHANNELS = 2
CHUNK = 1024
FORMAT = pyaudio.paInt16
DURATION = 5

recognizer = sr.Recognizer()


def listen_from_microphone():
    audio = pyaudio.PyAudio()

    stream = audio.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        input_device_index=DEVICE_INDEX,
        frames_per_buffer=CHUNK,
    )

    print("Recording for 5 seconds... speak now.")

    frames = []

    for _ in range(int(RATE / CHUNK * DURATION)):
        data = stream.read(CHUNK, exception_on_overflow=False)
        frames.append(data)

    stream.stop_stream()
    stream.close()

    sample_width = audio.get_sample_size(FORMAT)
    audio.terminate()

    print("Recording finished. Recognizing...")

    wav_buffer = io.BytesIO()

    with wave.open(wav_buffer, "wb") as wav:
        wav.setnchannels(CHANNELS)
        wav.setsampwidth(sample_width)
        wav.setframerate(RATE)
        wav.writeframes(b"".join(frames))

    wav_buffer.seek(0)

    with sr.AudioFile(wav_buffer) as source:
        recorded_audio = recognizer.record(source)

    try:
        return recognizer.recognize_google(recorded_audio)

    except sr.UnknownValueError:
        print("Could not understand audio.")
        return None

    except sr.RequestError as error:
        print("Recognition service error:", error)
        return None
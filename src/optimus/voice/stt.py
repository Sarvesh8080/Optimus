import audioop
import io
import time
import wave

import pyaudio
import speech_recognition as sr


DEVICE_INDEX = 17
RATE = 48000
CHANNELS = 2
CHUNK = 1024
FORMAT = pyaudio.paInt16

START_THRESHOLD = 500
SILENCE_THRESHOLD = 350
SILENCE_DURATION = 1.0
MAX_RECORD_SECONDS = 10

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

    print("Waiting for speech...")

    frames = []
    recording = False
    silence_started = None
    start_time = time.time()

    while True:
        data = stream.read(CHUNK, exception_on_overflow=False)

        volume = audioop.rms(data, 2)

        if not recording:
            if volume >= START_THRESHOLD:
                print("Listening...")
                recording = True
                frames.append(data)

        else:
            frames.append(data)

            if volume < SILENCE_THRESHOLD:
                if silence_started is None:
                    silence_started = time.time()

                elif time.time() - silence_started >= SILENCE_DURATION:
                    break
            else:
                silence_started = None

            if time.time() - start_time >= MAX_RECORD_SECONDS:
                break

    stream.stop_stream()
    stream.close()

    sample_width = audio.get_sample_size(FORMAT)
    audio.terminate()

    print("Recognizing...")

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
import audioop
import tempfile
import time
import wave

import pyaudio
from faster_whisper import WhisperModel


DEVICE_INDEX = 17
RATE = 48000
CHANNELS = 2
CHUNK = 1024
FORMAT = pyaudio.paInt16

START_THRESHOLD = 300
SILENCE_THRESHOLD = 350
SILENCE_DURATION = 1.0
MAX_RECORD_SECONDS = 10

model = WhisperModel(
    "base.en",
    device="cpu",
    compute_type="int8",
)


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
                start_time = time.time()

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

    with tempfile.NamedTemporaryFile(
        suffix=".wav",
        delete=False,
    ) as temp_file:
        temp_path = temp_file.name

    with wave.open(temp_path, "wb") as wav:
        wav.setnchannels(CHANNELS)
        wav.setsampwidth(sample_width)
        wav.setframerate(RATE)
        wav.writeframes(b"".join(frames))

    print("Recognizing locally...")

    segments, _ = model.transcribe(
        temp_path,
        language="en",
    )

    text = " ".join(
        segment.text.strip()
        for segment in segments
    ).strip()



    if not text:
        return None

    return text
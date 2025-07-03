import pyaudio
import numpy as np

# Parameters
CHUNK = 1024  # Number of audio samples per frame
FORMAT = pyaudio.paInt16  # 16-bit audio
CHANNELS = 1  # Mono audio
RATE = 44100  # Sample rate (Hz)
THRESHOLD = 500  # Threshold for detecting sound

def is_voice(data, threshold=THRESHOLD):
    """Return True if volume is above the threshold."""
    audio_data = np.frombuffer(data, dtype=np.int16)
    volume = np.linalg.norm(audio_data)
    return volume > threshold

def listen():
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("Listening for voice... Press Ctrl+C to stop.")
    try:
        while True:
            data = stream.read(CHUNK, exception_on_overflow=False)
            if is_voice(data):
                print("Voice detected!")
    except KeyboardInterrupt:
        print("Stopped listening.")
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()

if "__name__" == "_main_":
    listen()
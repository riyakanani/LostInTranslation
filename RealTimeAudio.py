import pyaudio
import numpy as np
import librosa
import soundfile as sf

def slow_down(data, factor=1):
    return np.repeat(data, factor)


def callback(in_data, frame_count, time_info, status):
    data = np.frombuffer(in_data, dtype=np.float32)
    
    processed_data = data.copy()
    processed_data = slow_down(processed_data, factor=2)  
    
    return processed_data.tobytes(), pyaudio.paContinue

p = pyaudio.PyAudio()

CHUNK = 1024
FORMAT = pyaudio.paFloat32
CHANNELS = 1
RATE = 44100

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=CHUNK,
                stream_callback=callback)

stream.start_stream()

while stream.is_active():
    pass

stream.stop_stream()
stream.close()

p.terminate()


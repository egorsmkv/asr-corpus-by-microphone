import torch
import time
import pyaudio
import wave
import os

from utils_vad import get_speech_timestamps, read_audio, init_jit_model, save_audio

# Fix the number of threads (as it is shown in Silero demos)
torch.set_num_threads(1)

# Init the model
model = init_jit_model('./silero_vad.jit')
window_size_samples = 512

# Config for microphone
CHUNK = 1024 
FORMAT = pyaudio.paInt16
CHANNELS = 1 
RATE = 16000
RECORD_SECONDS = 20
REMOVE_ORIGINAL_RECORDING = False


def split_speech(filename):
    wav = read_audio(filename, sampling_rate=16000)
    speech_timestamps = get_speech_timestamps(wav,
                                              model,
                                              sampling_rate=16000,
                                              window_size_samples=window_size_samples)
    for idx, ts in enumerate(speech_timestamps):
        segment = wav[ts['start'] : ts['end']]
        new_filename = filename.replace('data/','').replace('.wav', f'_{idx}.wav')
        save_dir = f'speech/{new_filename}'

        save_audio(save_dir, segment)

        print(f'File {save_dir} saved')
    
    if REMOVE_ORIGINAL_RECORDING:
        os.remove(filename)


def run():
    while True:
        output_filename = f"data/recording_{time.time()}.wav"

        p = pyaudio.PyAudio()
        stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

        # Recording audio
        print("* recording")
        frames = []
        for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)
        print("* done recording")

        stream.stop_stream()
        stream.close()
        p.terminate()

        # Save a recording into a WAV file
        wf = wave.open(output_filename, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

        # Split the recording by VAD
        split_speech(output_filename)

        print('Done, going to the next recording...')


if __name__ == '__main__':
    run()

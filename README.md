# ASR Corpus by Microphone

## Overview

This repository contains code to run a script that collects speech data from your microphone.

Watch video below to see how it works:

<a href="https://www.youtube.com/watch?v=WLPNZElikOc"><img src="./demo.png" width="200"></a>

## Installation

Install Python requirements:

```
pip install wave torch torchaudio pyaudio
```

## Running

```
# Create folders for work
mkdir data
mkdir speech

python record_and_split.py
```

## Help

- If you have any issues - [create an issue in the repository](https://github.com/egorsmkv/asr-corpus-by-microphone/issues/new)

## Acknowledgements

- Silero VAD: https://github.com/snakers4/silero-vad
- PyAudio: https://people.csail.mit.edu/hubert/pyaudio/
- wave: https://pythonhosted.org/Wave/

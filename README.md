# ASR Corpus by Microphone

## Overview

This repository contains code to run a script that collects speech data from your microphone.

Watch video below to see how it works:

<a href="https://www.youtube.com/watch?v=WLPNZElikOc"><img src="./demo.png" width="200"></a>

### Examples of Usage

- Collect ASR Corpus with your computer in places without internet connection (it's important for low-resourced languages)
- Split speech to chunks by Voice Activity Detection mechanism

## Installation

Install Python requirements:

### Linux

```bash
# the author has successfully tested the project with wave=0.0.2, torch==1.11.0, torchaudio==0.11.0, sox==1.4.1, and pyaudio==0.2.11
pip install wave torch torchaudio pyaudio sox
```

### MacOS

```bash
brew install portaudio sox

pip install wave
pip install --global-option='build_ext' --global-option='-I/usr/local/include' --global-option='-L/usr/local/lib' pyaudio
```

To install torch and torchaudio on MacOS you need to install [conda](https://docs.conda.io/en/latest/) or [miniconda](https://docs.conda.io/en/latest/miniconda.html) (I recommend it) and then install torch libraries:

For Intel:

```bash
conda install pytorch torchaudio -c pytorch
```

For M1:
```bash
pip3 install torch torchaudio
```

If you have problems with installation of pyaudio, then check out [this link](https://stackoverflow.com/questions/33513522/when-installing-pyaudio-pip-cannot-find-portaudio-h-in-usr-local-include). For me below command works:

```bash
pip3 install --global-option='build_ext' --global-option='-I/opt/homebrew/Cellar/portaudio/19.7.0/include/' --global-option='-L/opt/homebrew/Cellar/portaudio/19.7.0/lib/' pyaudio
```

## Running

```bash
# Create folders where audio files will appear
mkdir data
mkdir speech

# Run the loop (this script will record speech and save it into the speech/ folder)
# Use Ctrl-C to stop the script
python record_and_split.py
```

## Help

- If you have any issues - [create an issue in the repository](https://github.com/egorsmkv/asr-corpus-by-microphone/issues/new)
- Currently tested on Linux and MacOS, for Windows you need to change the script slightly

## Acknowledgements

- Silero VAD: https://github.com/snakers4/silero-vad
- PyAudio: https://people.csail.mit.edu/hubert/pyaudio/
- wave: https://pythonhosted.org/Wave/

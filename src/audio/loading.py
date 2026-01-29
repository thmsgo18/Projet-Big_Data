import numpy as np
import librosa

def load_audio(path: str, target_sr: int = 22050, mono: bool = True):
    waveform, sr = librosa.load(path, target_sr, mono)
    return waveform, sr
import numpy as np
import librosa as lb
in_voice = []
mfcc_voice = lb.feature.mfcc(in_voice, sr=44100)
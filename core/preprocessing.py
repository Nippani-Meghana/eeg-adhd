#helper_functions.py
#This python file contains all the pre-processing functions

import scipy.signal as signal

def iir_butterworth_filter(data, order, freq_range, fs):
    sos_bandpass = signal.butter(order, freq_range, btype='bandpass', fs=fs, output='sos')
    return signal.sosfiltfilt(sos_bandpass, data)

def iir_notch_filter(data, notch_freq, Q, fs):
    b_notch, a_notch = signal.iirnotch(notch_freq, Q=Q, fs=fs)
    return signal.filtfilt(b_notch, a_notch, data)

def four_sec_segment(data, segment_duration, fs):
    samples_per_segment = int(segment_duration * fs)
    num_segments = len(data) // samples_per_segment
    return data[:num_segments * samples_per_segment].reshape(num_segments, samples_per_segment)
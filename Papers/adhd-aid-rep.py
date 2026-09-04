#MDPI: Attallah, O. 
# ADHD-AID: Aiding Tool for Detecting 
# Children's Attention Deficit Hyperactivity Disorder 
# via EEG-Based Multi-Resolution Analysis and Feature Selection. 
# Biomimetics 2024, 9, 188. https://doi.org/10.3390/biomimetics9030188

#Path resolution 
import sys
from pathlib import Path

_here = Path(__file__).resolve().parent
_project_root = None
for _candidate in [_here, *_here.parents]:
    if (_candidate / "nasarbadi_helper.py").exists():
        _project_root = _candidate
        break

if _project_root is None:
    raise RuntimeError("Could not locate project root (nasarbadi_helper.py not found).")

if str(_project_root) not in sys.path:
    sys.path.insert(0, str(_project_root))

#Standard imports
import pywt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pysdkit as psy

#Local imports
import nasarbadi_helper
from core import preprocessing as hp
from core import feature_extraction_metrics as fsm

#Configuration
PROJECT_ROOT = _project_root
OUTPUT_DIR = PROJECT_ROOT / "datasets" / "adhd-aid-data"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

FS = 128                          # Sampling frequency (Hz)
BANDPASS_ORDER = 4                # Butterworth filter order
BANDPASS_RANGE = (0.5, 45.0)     # Bandpass frequency range (Hz) — standard for EEG
NOTCH_FREQ = 50.0                 # Notch filter frequency (Hz) — powerline noise
NOTCH_Q = 30.0                   # Notch quality factor
SEGMENT_DURATION = 4              # Segment length (seconds)

#Subject List
all_subjects = pd.read_csv(
    PROJECT_ROOT / "datasets" / "metadata" / "nasarbadi_subject_index.csv"
)["ID"].tolist()

#Pre-processing
print("Pre-processing:")
for subject_id in all_subjects:
    subject_data, class_label = nasarbadi_helper.get_subject_info(subject_id)

    file_name = f"subject_{subject_id}.npy"
    file_path = OUTPUT_DIR / file_name

    if file_path.exists():
        print(f"Skipping subject {subject_id}: '{file_name}' already exists.")
        continue

    subject_processed_channels = []
    for channel in subject_data.columns:
        raw_data = subject_data[channel].values

        # Preprocessing cascade
        bandpassed = hp.iir_butterworth_filter(raw_data, order=BANDPASS_ORDER, freq_range=BANDPASS_RANGE, fs=FS)
        cleaned    = hp.iir_notch_filter(bandpassed, notch_freq=NOTCH_FREQ, Q=NOTCH_Q, fs=FS)
        segmented  = hp.four_sec_segment(cleaned, segment_duration=SEGMENT_DURATION, fs=FS)

        subject_processed_channels.append(segmented)

    # Stack all channels in shape: (n_channels, n_segments, samples_per_segment)
    subject_array = np.array(subject_processed_channels)
    np.save(file_path, subject_array)
    print(f"Saved: {file_name} | Array Shape: {subject_array.shape}")

#The above saves the data in this structure:
#                     data
#                      │
#           ┌──────────┴──────────┐
#           │                     │
#       Channel 0             Channel 1 ...
#           │
#      ┌────┴────┐
#      │         │
#  Segment 0  Segment 1 ...
#      │
#   ┌──┴─────────────────────────┐
#   │  t0  t1  t2 ... t510 t511  │
#   └────────────────────────────┘

#Multi-Resolution Analysis

#1. VDM

#VMD Parameters
K = 9        
alpha = 2000 
tau = 0      
DC = 0       
init = "uniform"     
tol = 1e-7
VMD_DIR = OUTPUT_DIR / "vmd"
VMD_DIR.mkdir(parents=True, exist_ok=True)

print("VDM:")
for subject_id in all_subjects:
    subject_file = OUTPUT_DIR/f"subject_{subject_id}.npy"
    subject_data = np.load(subject_file)

    vmd_file = VMD_DIR / f"subject_{subject_id}_vmd.npy"

    if vmd_file.exists():
            print(f"Skipping subject {subject_id}: 'subject_{subject_id}_vmd' already exists.")
            continue
    
    channel, segment, sample = subject_data.shape
    subject_vmd = np.empty(
        (channel, segment, K, sample),
        dtype=np.float32
    )
    for i in range(channel):
        for j in range (segment):
            signal = subject_data[i,j,:]
            vmd = psy.VMD(alpha=alpha,K=K,tau=tau,DC=DC,init=init,tol=tol)
            IMFs = vmd.fit_transform(signal=signal)
            subject_vmd[i, j, :, :] = IMFs
    
    np.save(vmd_file, subject_vmd)

    print(
        f"Saved: {vmd_file.name} | "
        f"Array Shape: {subject_vmd.shape}"
    )

#2. Feature extraction
#Testing statisitical features for now

def load_vm(subject_id):
    VMD_DIR = OUTPUT_DIR / "vmd"
    vmd_subject_file = VMD_DIR/f"subject_{subject_id}_vmd.npy"
    vmd_data = np.load(vmd_subject_file)
    return vmd_data

data = load_vm("v1p")
imf = data[0, 0, 2, :]
features = fsm.statistical_time_domain(imf)
print(features)

# Parameters Based On
# MDPI: Attallah, O. 
# ADHD-AID: Aiding Tool for Detecting 
# Children's Attention Deficit Hyperactivity Disorder 
# via EEG-Based Multi-Resolution Analysis and Feature Selection. 
# Biomimetics 2024, 9, 188. https://doi.org/10.3390/biomimetics9030188

from core import EegDataset
import pandas as pd

FS = 128
BANDPASS_ORDER = 6
BANDPASS_RANGE = (0.5, 60.0)
NOTCH_FREQ = 50.0
NOTCH_ORDER = 2
SEGMENT_DURATION = 4
EPS = 1e-12

data_1 = pd.read_csv("../../datasets/raw_data/adhdata.csv")
nasarbadi_dataset = EegDataset.EegDataset(
    name="nasarbadi_adhd",
    sampling_freq_hz=128.0,
    participants=len(data_1["ID"].unique()),
    num_channels=19,
    adhd_num=data_1[data_1["Class"] == "ADHD"]["ID"].nunique(),
    control_num=data_1[data_1["Class"] == "Control"]["ID"].nunique(),
    channel_names=[f"Channel_{i}" for i in range(19)],
    raw_data_path="./datasets/raw_data/adhdata.csv",
    interim_data_path="../../datasets/interim_data/nasarbadi/",
    metadata_path = "../../datasets/metadata"

    )
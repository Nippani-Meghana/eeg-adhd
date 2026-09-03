# nasarbadi_helper.py

from pathlib import Path

import pandas as pd
from core import EegDataset

PROJECT_ROOT = Path(__file__).resolve().parent


def _data_path(*parts):
    return PROJECT_ROOT.joinpath(*parts)


def get_dataset_info():
    data = pd.read_csv(_data_path("datasets", "raw_data", "adhdata.csv"))

    dataset_info = EegDataset.EegDataset(
        name="nasarbadi_adhd",
        sampling_freq_hz=128.0,
        participants=len(data["ID"].unique()),
        num_channels=19,
        adhd_num=data[data["Class"] == "ADHD"]["ID"].nunique(),
        control_num=data[data["Class"] == "Control"]["ID"].nunique(),
        channel_names=[f"Channel_{i}" for i in range(19)],
        raw_data_path=str(_data_path("datasets", "raw_data", "adhdata.csv")),
        interim_data_path=str(_data_path("datasets", "interim_data", "nasarbadi")),
        metadata_path=str(_data_path("datasets", "metadata")),
    )

    return dataset_info


def get_subject_info(subject_id):
    subject_data = pd.read_csv(_data_path("datasets", "interim_data", "nasarbadi", f"{subject_id}.csv"))

    if subject_data.empty:
        raise ValueError(f"No data found for subject ID: {subject_id}")

    metadata_path = _data_path("datasets", "metadata", "nasarbadi_subject_index.csv")
    metadata = pd.read_csv(metadata_path)
    class_label = metadata.loc[metadata["ID"] == subject_id, "Class"].values[0]
    return [subject_data, class_label]
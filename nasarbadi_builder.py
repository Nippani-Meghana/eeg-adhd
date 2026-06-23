#nasarbadi_builder.py

import pandas as pd
import EegDataset
import os

def _build_subject_csvs(data):
    if(data is None):
        raise ValueError("Data is None")

    unique_ids = data["ID"].unique()

    # Check if all files already exist
    all_files_exist = all(os.path.exists(f"./datasets/interim_data/nasarbadi/{id}.csv") for id in unique_ids)
    if all_files_exist:
        print(f"All {len(unique_ids)} files already exist. Skipping conversion.")
        return
    
    # Convert to CSV
    for id in unique_ids:
        subject_data = data.loc[data["ID"] == id]
        subject_data = subject_data.drop(columns=["ID"])
        subject_data.to_csv(f"./datasets/interim_data/nasarbadi/{id}.csv", index=False)


if __name__ == "__main__":

    # Load the raw data
    data_1 = pd.read_csv("./datasets/raw_data/adhdata.csv")

    # Create an instance of EegDataset
    df_1 = EegDataset.EegDataset(
        name="nasarbadi_adhd",
        sampling_freq_hz=128.0,
        participants=len(data_1["ID"].unique()),
        num_channels=19,
        adhd_num=data_1[data_1["Class"] == "ADHD"]["ID"].nunique(),
        control_num=data_1[data_1["Class"] == "Control"]["ID"].nunique(),
        channel_names=[f"Channel_{i}" for i in range(19)],
        raw_data_path="./datasets/raw_data/adhdata.csv",
        interim_data_path="./datasets/interim_data/nasarbadi/"

    )

    _build_subject_csvs(data_1)
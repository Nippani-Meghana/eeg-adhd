#nasarbadi_builder.py

import pandas as pd
import EegDataset
import EegSubject
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
        subject_data = subject_data.drop(columns=["ID", "Class"])  
        subject_data.to_csv(f"./datasets/interim_data/nasarbadi/{id}.csv", index=False)

def _build_subject_index(data, sampling_freq_hz, metadata_path):
    if(data is None):
        raise ValueError("Data is None")

    unique_ids = data["ID"].unique()
    index_data = []

    for id in unique_ids:
        subject_data = data.loc[data["ID"] == id]
        duration_sec = len(subject_data) / sampling_freq_hz
        n_samples = len(subject_data)
        class_label = subject_data["Class"].iloc[0]  # Assuming the class label is the same for all rows of a subject
        index_data.append({"ID": id, "Duration_sec": duration_sec, "Class": class_label, "n_samples": n_samples})

    index_df = pd.DataFrame(index_data)
    index_df.to_csv(os.path.join(metadata_path, "nasarbadi_subject_index.csv"), index=False)
    
   

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
        interim_data_path="./datasets/interim_data/nasarbadi/",
        metadata_path = "./datasets/metadata"

    )


    #Already done this step, so commenting it out to avoid overwriting existing files.
    #_build_subject_csvs(data_1)
    #_build_subject_index(data_1, df_1.sampling_freq_hz, df_1.metadata_path)
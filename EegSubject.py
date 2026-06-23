#EegSubject.py

from dataclasses import dataclass

@dataclass
class EegSubject:
    subject_id: str
    duration_sec: float
    class_label: str
    n_samples: int
    sampling_freq_hz: float
    channel_names: list
    file_path: str


def _retrieve_subject_info(data, sampling_freq_hz, subject_id):
    subject_data = data.loc[data["ID"] == subject_id]
    duration_sec = len(subject_data) / sampling_freq_hz
    n_samples = len(subject_data)
    class_label = subject_data["Class"].iloc[0]  # Assuming the class label is the same for all rows of a subject
    file_path = f"./datasets/interim_data/nasarbadi/{subject_id}.csv"
    
    return EegSubject(
        id=subject_id,
        duration_sec=duration_sec,
        class_label=class_label,
        n_samples=n_samples,
        sampling_freq_hz=sampling_freq_hz,
        file_path=file_path
    )

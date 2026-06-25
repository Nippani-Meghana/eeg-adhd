#signal_processing/testing.py
import mne

import pandas as pd
import matplotlib.pyplot as plt
import nasarbadi_helper

all_subjects = pd.read_csv("./datasets/metadata/nasarbadi_subject_index.csv")["ID"].tolist()

#plot a subject's 1 channel data

subject_id = all_subjects[0]
subject_data, class_label = nasarbadi_helper.get_subject_info(subject_id)


#Plot the signal of the first channel
plt.figure(figsize=(12, 6))
subject_data.iloc[:, 0].plot(title=f"Subject ID: {subject_id}, Class: {class_label}, Channel: {subject_data.columns[0]}")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.show()




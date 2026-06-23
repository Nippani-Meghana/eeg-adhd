#EegDataset.py

from dataclasses import dataclass
import pandas as pd
import os

@dataclass
class EegDataset:
    name: str
    sampling_freq_hz: float
    participants: int
    num_channels: int
    adhd_num: int
    control_num: int
    channel_names: list
    raw_data_path: str 
    interim_data_path: str 

    



    
        
            

#core/EegSubject.py

from dataclasses import dataclass
import pandas as pd
import numpy as np
from typing import Optional
from pathlib import Path
import os


@dataclass
class EegSubject:
    subject_name: str
    classification: str
    segment_number: int
    raw_csv_path: Path
    preprocessed_path: Optional[Path] = None
    vmd_path: Optional[Path] = None
    dwt_path: Optional[Path] = None
    ewt_path: Optional[Path] = None
    features: Optional[np.ndarray] = None

    def load_raw_csv(self) -> pd.DataFrame:
        """Load and return the raw CSV data on demand."""
        return pd.read_csv(self.raw_csv_path)
    
    def load_preprocessed(self) -> np.ndarray:
        return np.load(self.preprocessed_path)
    
    def load_vmd(self) -> np.ndarray:
        return np.load(self.vmd_path)



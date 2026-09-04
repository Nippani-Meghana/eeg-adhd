#core/feature_extraction_metrics.py

import numpy as np
import scipy as sc

def statistical_time_domain(imf_wave):
    """
    Calculates basic statistical features from a single IMF wave 
    The following features are measured and returned:
    1. Mean
    2. Standard deviation
    3. Variance
    4. Minimum
    5. Maximum
    6. Skewness: Is the amplitude distribution asymmetric?
    Skewness = 0, roughly symmetric
    Positive skewness = longer/heavier tail toward large positive values
    Negative skewness = longer/heavier tail toward large negative values
    7. Kurtosis: How heavy-tailed/extreme is the amplitude distribution?
    8. Mean Curve Length: How much does the waveform fluctuate/change?
    9. Mean Energy: how much amplitude/activity the IMF contains
    10. Mean Teager Energy: How strong is its local oscillatory activity considering 
    amplitude + frequency?
    
    """
    mean_val = np.mean(imf_wave)
    std_val  = np.std(imf_wave)
    var_val  = np.var(imf_wave)
    min_val  = np.min(imf_wave)
    max_val  = np.max(imf_wave)
    skew_val = sc.stats.skew(imf_wave, axis = 0, bias = False)
    kurtosis_val = sc.stats.kurtosis(imf_wave, axis = 0, fisher = True, bias = False)
    mcl_val = np.mean(np.abs(np.diff(imf_wave)))
    mean_en_val = np.mean(imf_wave**2)
    #mean_teager_en_val = 
    return [mean_val, std_val, var_val, min_val, max_val,skew_val, 
            kurtosis_val, mcl_val, mean_en_val]

def spectral_band_power(imf_wave):
    """Calculates and returns the following:
     1.Band-Power Alpha: amount of signal power in the alpha frequency range (~8-13 Hz).
     2.Band-Power Beta: how much signal power is present in the beta frequency range.
     3.Band-Power Delta: how much signal power is contained in very slow oscillations.
     4.Band-Power Gamma: how much signal power is present in the gamma range.
     5.Band-Power Theta: how much signal power is contained in the 4-8 Hz range.
     The above 5 ask how much of EEG signal is happening at each frequency range
     6.Ratio Band-Power Alpha/Beta 
     """
    
    pass

def information_theory(imf_wave):
    """Calculates and returns the following:
    1.Log Energy Entropy
    2.Rényi Entropy
    3.Shannon Entropy
    4.Tsallis Entropy"""

def Hjorth_dynamic_variations(imf_wave):
    """Calculates and returns the following:
    1.Hjorth Activity
    2.Hjorth Complexity
    3.Hjorth Mobility
    4.Log Root Sum of Sequential Variation"""

def difference_features(imf_wave):
    """Calculates and returns the following:
    1. First Difference
    2. Second Difference
    3. Normalized First Difference
    4. Normalized Second Difference"""

def model_based(inf_wave):
    """Calculates and returns the following:
    1. Autoregressive Model"""
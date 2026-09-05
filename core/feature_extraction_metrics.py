#core/feature_extraction_metrics.py

import numpy as np
import scipy as sc

def statistical_time_domain(wave):
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
    mean_val = np.mean(wave)
    std_val  = np.std(wave)
    var_val  = np.var(wave)
    min_val  = np.min(wave)
    max_val  = np.max(wave)
    skew_val = sc.stats.skew(wave, axis = 0, bias = False)
    kurtosis_val = sc.stats.kurtosis(wave, axis = 0, fisher = True, bias = False)
    mcl_val = np.mean(np.abs(np.diff(wave)))
    mean_en_val = np.mean(wave**2)
    #mean_teager_en_val = 
    return [mean_val, std_val, var_val, min_val, max_val,skew_val, 
            kurtosis_val, mcl_val, mean_en_val]

def spectral_band_power(fs, wave):
    """Calculates and returns the following:
     1.Band-Power Alpha: amount of signal power in the alpha frequency range (~8-13 Hz).
     2.Band-Power Beta: how much signal power is present in the beta frequency range.
     3.Band-Power Delta: how much signal power is contained in very slow oscillations.
     4.Band-Power Gamma: how much signal power is present in the gamma range.
     5.Band-Power Theta: how much signal power is contained in the 4-8 Hz range.
     The above 5 ask how much of EEG signal is happening at each frequency range
     6.Ratio Band-Power Alpha/Beta 
     """
    from scipy.signal import welch
    from scipy.integrate import simpson
    bands = {
    'Delta': (1, 4),
    'Theta': (4, 8),
    'Alpha': (8, 12),
    'Beta': (12, 30),
    'Gamma': (30, 60)
    }
    frequencies, psd = welch(wave, fs, nperseg=fs*2)

    def get_band_power(frequencies, psd, band_range):
        idx_band = np.logical_and(frequencies >= band_range[0], frequencies <= band_range[1])
        band_power = simpson(psd[idx_band], frequencies[idx_band])
        return band_power

    delta_power = get_band_power(frequencies, psd, bands['Delta'])
    theta_power = get_band_power(frequencies, psd, bands['Theta'])
    alpha_power = get_band_power(frequencies, psd, bands['Alpha'])
    beta_power = get_band_power(frequencies, psd, bands['Beta'])
    gamma_power = get_band_power(frequencies, psd, bands['Gamma'])
    alpha_beta_ratio = alpha_power/beta_power

    return [delta_power, theta_power, alpha_power, beta_power, gamma_power, alpha_beta_ratio]


def information_theory(fs,wave, eps):
    """Calculates and returns the following:
    1.Log Energy Entropy: Distribution of signal energy, logarithmically scaled
    2.Rényi Entropy: Overall uncertainty/disorder
    3.Shannon Entropy: Generalized entropy with tunable sensitivity
    4.Tsallis Entropy: Generalized entropy suited to complex/non-extensive distributions
    """
    from scipy.stats import entropy
    import antropy as ant

    from dit.other import renyi_entropy
    wave_sq = wave**2
    wave_sq = np.where(wave_sq == 0, eps, wave_sq )
    log_energy_entropy = np.sum(np.log(wave_sq)) 

    #renyi_entropy = 
    #Calculating Spectral Shannon Entropy
    spec_entropy = ant.spectral_entropy(wave, sf=fs, method='welch', normalize=True)
    

    


def Hjorth_dynamic_variations(wave):
    """Calculates and returns the following:
    1.Hjorth Activity: How much the signal's amplitude is varying?
    2.Hjorth Complexity: Is the way it's changing itself complicated? 
    3.Hjorth Mobility: How quickly is the signal varying?
    4.Log Root Sum of Sequential Variation:How much total sample-to-sample variation is there?
    """
    hjorth_activity = np.var(wave) #activity = var(y(t))

    first_diff = np.diff(wave) 
    variance_first_diff = np.var(first_diff)
    hjorth_mobility = np.sqrt(variance_first_diff/hjorth_activity) # mobility = sqrt(var(y'(t))/var(y(t)))

    second_diff = np.diff(first_diff) 
    variance_second_diff = np.var(second_diff)
    mobility_first_diff = np.sqrt(variance_second_diff/variance_first_diff)
    hjorth_complexity = (mobility_first_diff/hjorth_mobility) 

    root_sum_sequential_variation = np.sqrt(np.sum(first_diff ** 2))
    lrssv = np.log(root_sum_sequential_variation)

    return [hjorth_activity, hjorth_mobility, hjorth_complexity, lrssv]


def difference_features(wave):
    """Calculates and returns the following:
    1. First Difference: How much did the signal change at each step?
    2. Second Difference: Is the rate at which the signal is changing itself changing?
    3. Normalized First Difference: How rapidly does the signal change, relative to how 
    large the signal itself is?
    4. Normalized Second Difference: how rapidly the signal's rate of change changes, relative 
    to the signal's overall magnitude.
    """
    first_diff = np.diff(wave)
    second_diff = np.diff(first_diff)
    std_dev = np.std(wave)
    normalized_first_diff = first_diff/std_dev
    normalized_sec_diff = second_diff/std_dev

    return [first_diff, second_diff, normalized_first_diff, normalized_sec_diff]

def model_based(wave):
    """Calculates and returns the following:
    1. Autoregressive Model"""
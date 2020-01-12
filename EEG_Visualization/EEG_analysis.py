import numpy as np
import mne
from mne.datasets import eegbci

# Read the CSV file as a NumPy array
data = np.loadtxt('muse_Dataset/museMonitor_2018-11-09--22-56-00.csv', delimiter=',')

# Some information about the channels
ch_names = ['CH 1', 'CH 2', 'CH 3', 'CH 4', 'CH 5', 'CH 6', 'CH 7', 'CH 8', 'CH 9', 'CH 10', 'CH 11', 'CH 12', 
'CH 13', 'CH 14', 'CH 15', 'CH 16', 'CH 17', 'CH 18', 'CH 19']  # TODO: finish this list

# Sampling rate of the Nautilus machine
sfreq = 500  # Hz

# Create the info structure needed by MNE
info = mne.create_info(ch_names, sfreq)

# Finally, create the Raw object
raw = mne.io.RawArray(data, info)

# Plot it!
raw.plot()
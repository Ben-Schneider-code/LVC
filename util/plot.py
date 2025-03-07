import torch
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import os 
def plot_heatmap(attn: torch.Tensor, save_path="./fig.png"):
    # Convert attention tensor to numpy array
    attention_data = attn.numpy()
    rows, cols = attention_data.shape
    
    # Set DPI for output (controls resolution-to-pixel ratio)
    save_dpi = 100  # Adjust for different resolutions if needed
    
    # Calculate figure dimensions to match data shape
    fig_width = cols / save_dpi
    fig_height = rows / save_dpi

    # Create figure with exact dimensions needed for the data
    fig, ax = plt.subplots(
        figsize=(fig_width, fig_height),
        dpi=save_dpi,
        constrained_layout=True  # Automatically adjust subplot params
    )
    
    # Remove margins and padding
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1, wspace=0, hspace=0)
    
    # Create heatmap with exact pixel mapping
    heatmap = ax.imshow(
        attention_data,
        cmap='viridis',
        aspect='auto',
        norm=LogNorm(),
        interpolation='none'  # Prevent pixel interpolation
    )
    
    # Remove axes and labels
    ax.axis('off')
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    # Save with exact pixel dimensions and no padding
    plt.savefig(
        save_path,
        dpi=save_dpi,
        pad_inches=0,
        bbox_inches='tight'
    )
    plt.close()

import numpy as np
import matplotlib.pyplot as plt

def freq_plot(arr, save_path):


    # Compute FFT and frequencies
    n = len(arr)
    fft_values = np.fft.rfft(arr)  # FFT for real input
    frequencies = np.fft.rfftfreq(n, d=1)  # d=1 corresponds to timestep of 1
    magnitude = np.abs(fft_values)  # Magnitude of each frequency component

    # Plotting
    plt.plot(frequencies, magnitude)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.title('Frequency Domain Plot')
    plt.grid(True)
    plt.savefig(
        save_path,
        pad_inches=0,
        bbox_inches='tight'
    )
    plt.close()

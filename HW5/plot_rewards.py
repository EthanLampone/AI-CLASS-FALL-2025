## ETHAN LAMPONE
## 9 DECEMBER 2025
## PLOT AVERAGE REWARDS

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd # Needed for moving average calculation

def plot_moving_average_reward(filename, window_size=50):
    """
    Loads raw episode rewards and plots the N-episode moving average.
    """
    # 1. Load the data
    try:
        rewards = np.loadtxt(filename, delimiter=",")
    except OSError:
        print(f"File {filename} not found. Run the game first!")
        return

    # 2. Calculate the Moving Average
    # This is the "Average Reward per Episode" over the last 'window_size' episodes.
    series = pd.Series(rewards)
    # The '.rolling(window=window_size).mean()' function computes the rolling average.
    moving_avg = series.rolling(window=window_size).mean()

    # 3. Plotting
    plt.figure(figsize=(10, 6))
    
    # Plot raw data (faint background)
    plt.plot(rewards, alpha=0.3, color='gray', label='Raw Episode Reward')
    
    # Plot the Moving Average (the smoothed curve)
    plt.plot(moving_avg, color='blue', linewidth=3, label=f'Average Reward ({window_size}-Episode Moving Window)')

    plt.title('Agent Training Performance: Average Reward per Episode')
    plt.xlabel('Episode')
    plt.ylabel(f'Average Total Reward (over {window_size} episodes)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()

# Example usage:
plot_moving_average_reward("trained_rewards.csv", window_size=50)

import pandas as pd
import matplotlib.pyplot as plt

def plot_rewards(filename='car_dqn_rewards.csv', window_size=50):
    """
    Loads episode rewards from a CSV, calculates a moving average, and plots them.
    """
    try:
        # Load the data
        df = pd.read_csv(filename)
        
        # Calculate Moving Average (to smooth the curve and show the trend)
        df['Moving Average'] = df['Reward'].rolling(window=window_size).mean()

        plt.figure(figsize=(12, 6))
        
        # Plot the raw episode rewards (in lighter color)
        plt.plot(df['Episode'], df['Reward'], color='gray', alpha=0.4, label='Raw Episode Reward')
        
        # Plot the moving average (main trend line)
        plt.plot(df['Episode'], df['Moving Average'], color='blue', linewidth=2, 
                 label=f'Moving Average (Window={window_size})')
        
        plt.title('DQN Car Driving Agent Learning Progress 🚗', fontsize=16)
        plt.xlabel('Episode', fontsize=14)
        plt.ylabel('Total Reward per Episode', fontsize=14)
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.legend()
        plt.tight_layout()
        plt.show()

    except FileNotFoundError:
        print(f"Error: Reward file '{filename}' not found. Run the training first!")
    except Exception as e:
        print(f"An error occurred during plotting: {e}")

# Call the function to generate the plot
if __name__ == "__main__":
    plot_rewards()
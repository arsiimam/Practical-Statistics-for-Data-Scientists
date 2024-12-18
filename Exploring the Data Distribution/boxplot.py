import matplotlib.pyplot as plt
import pandas as pd
import os

# Load the CSV file
file_path = os.path.join('..', 'Estimates of Locations', 'data.csv')
df = pd.read_csv(file_path, delimiter=';')

# Ensure the required columns exist
if 'Subject' in df.columns and 'Score' in df.columns:
    # Get unique subjects dynamically
    subjects = df['Subject'].unique()

    # Create the boxplot
    plt.figure(figsize=(8, 6))
    plt.boxplot([df[df['Subject'] == subject]['Score'] for subject in subjects],
                patch_artist=True,
                boxprops=dict(facecolor='lightblue', color='blue'),
                medianprops=dict(color='red', linewidth=2))

    # Add labels and title
    plt.xticks(ticks=range(1, len(subjects) + 1), labels=subjects)  # X-axis labels
    plt.title("Analysis of Student Score Distribution by Subject")
    plt.ylabel("Scores")
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Show the plot
    plt.show()
else:
    print("Error: 'Subject' or 'Score' column not found in the data.")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

NUM_BINS = 10  # n: for [0-n]
TITLE = "Finance 2 Exam results" # set a title
FIG_SIZE = (12, 7) # adjust figure size
PLANK = -1 # if x >= PLANK, else: skip
MAX_MARK = 100 # x = min(MAX_MARK, x)
MY_MARK = -1 # add your mark as line, -1 for disable
SCALE_FACTOR = 0.1

# Load and process data
marks = []
with open('stuff/distribution/simple_data.txt', 'r') as file:
    for line in file:
        try:
            marks.append(float(line.strip().replace(',', '.')))
        except:
            for x in line.strip().split():
                marks.append(float(x.strip().replace(',', '.')))

# Filter and round marks
median = np.median(marks)*SCALE_FACTOR
mean = np.mean(marks)*SCALE_FACTOR
marks = [round(SCALE_FACTOR * min(x, MAX_MARK)) for x in marks if x >= PLANK]

# Count occurrences of each integer mark
mark_counts = {i: marks.count(i) for i in range(NUM_BINS)}

# Create the plot
fig, ax = plt.subplots(figsize=FIG_SIZE)

# Set the background color
fig.patch.set_facecolor('#FAF9F6')
ax.set_facecolor('#FAF9F6')

# Create bar chart
bars = ax.bar(range(NUM_BINS), [mark_counts[i] for i in range(NUM_BINS)], 
              edgecolor='black', color="#6A9C89")

# Customize the plot
ax.set_title(TITLE, fontsize=20, fontweight='bold')
ax.set_xlabel('Marks', fontsize=14)
ax.set_ylabel('Frequency', fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=12)

# Add labels for bars
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height,
            f'{int(height)}',
            ha='center', va='bottom', fontweight='bold', fontsize=10)

# Set x-axis ticks for each integer from 0 to 10
ax.set_xticks(range(NUM_BINS))
ax.set_xticklabels(range(NUM_BINS))

# Add grid lines for y-axis
ax.grid(axis='y', linestyle='--', alpha=0.5)

# Calculate statistics for integer marks
marks_series = pd.Series(marks)
mode = marks_series.mode().iloc[0] if not marks_series.mode().empty else None

# Add lines for mean and median
max_height = max(mark_counts.values())
ax.axvline(mean, color='red', linestyle='--', linewidth=1, label=f'Mean: {mean:.2f}')
ax.axvline(median, color='green', linestyle='--', linewidth=1, label=f'Median: {median:.2f}')

# Add a line for MY_MARK if it's not -1
if MY_MARK != -1 and MY_MARK.is_integer() and 0 <= MY_MARK <= 10:
    ax.axvline(MY_MARK, color='blue', linestyle='--', linewidth=1, label=f'My Mark: {MY_MARK:.0f}')

# Customize the legend
ax.legend(loc='upper right', fontsize=12)

# Adjust y-axis to accommodate the lines
ax.set_ylim(0, max_height * 1.2)

# Adjust layout and display
plt.tight_layout()
plt.show()

# Print additional statistics
quartiles = marks_series.quantile([0.25, 0.5, 0.75])
print(f"Quartiles:\n{quartiles}")
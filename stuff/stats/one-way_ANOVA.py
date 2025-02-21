import numpy as np
from scipy.stats import f

# Data
x = [[85, 75, 82, 76, 71, 85], 
     [71, 75, 73, 74, 69, 82], 
     [59, 64, 62, 69, 75, 67]]

# Convert to numpy array for easier calculations
data = np.array(x)
data = data.T

# Calculate the overall mean
overall_mean = np.mean(data)

# Calculate the total sum of squares (SST)
sst = np.sum((data - overall_mean) ** 2)

# Calculate the mean of each group
group_means = np.mean(data, axis=0)

# Calculate the between-group sum of squares (SSB)
ssb = len(data) * np.sum((group_means - overall_mean) ** 2)

# Calculate the within-group sum of squares (SSW)
ssw = np.sum((data - group_means) ** 2)

# Calculate the mean squares
k = len(group_means)  # number of groups
N = data.size  # total number of observations

msb = ssb / (k - 1)
msw = ssw / (N - k)

# Calculate the F-score
f_score = msb / msw

# Calculate the p-value
p_value = 1 - f.cdf(f_score, k - 1, N - k)

print(f'Overall Mean: {overall_mean:.3f} points')
print(f"Total Sum of Squares (SST): {sst:.3f}")
print(f"Between-Group Sum of Squares (SSB): {ssb:.3f}")
print(f"Within-Group Sum of Squares (SSW): {ssw:.3f}")
print(f"F-score: {f_score:.3f}")
print(f"P-value: {p_value:.3f}")

# columns means
column_means = np.mean(data, axis=0)
print(f'Column Means: {column_means}')

# calculate sample variance for each column
sample_variance = np.var(data, axis=0, ddof=1)
print(f'Sample Variance: {sample_variance}')

# calculate the overall sample variance
overall_sample_variance = np.var(data, ddof=1)
print(f'Overall Sample Variance: {overall_sample_variance:.3f}')
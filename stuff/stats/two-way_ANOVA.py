import numpy as np
from scipy.stats import f

# Example Data
# Replace this with your actual data
# Assume a balanced design with 3 levels for Factor1 and 3 levels for Factor2
x = np.array([
    [4.8, 5.3, 4.9], 
    [4.6, 5.0, 4.3], 
    [4.6, 5.1, 4.8]
])

# Calculate the overall mean
overall_mean = np.mean(x)

# Calculate row means and column means
row_means = np.mean(x, axis=1)
column_means = np.mean(x, axis=0)

# Calculate sample variances for rows and columns
row_variances = np.var(x, axis=1, ddof=1)
column_variances = np.var(x, axis=0, ddof=1)

print(f"Overall Mean: {overall_mean:.3f}")
print("Row Means:", " ".join(f"{mean:.2f}" for mean in row_means))
print("Column Means:", " ".join(f"{mean:.2f}" for mean in column_means))
print("Row Sample Variances:", " ".join(f"{var:.2f}" for var in row_variances))
print("Column Sample Variances:", " ".join(
    f"{var:.2f}" for var in column_variances))
# print(f"rc*x_bar^2 {len(x)*len(x[0])*overall_mean**2:.3f}")

# Calculate the sum of squares of each element
sum_of_squares = np.sum(x ** 2)
print(f"Sum of Squares of Each Element: {sum_of_squares:.3f}\n")

# Calculate SSB (Sum of Squares Between)
n_columns = x.shape[1]
ssb = n_columns * np.sum((row_means - overall_mean) ** 2)
print(f"SSB (Sum of Squares Between): {ssb:.3f}")


# Calculate SST (Total Sum of Squares)
sst = np.sum((x - overall_mean) ** 2)
print(f"SST (Total Sum of Squares): {sst:.3f}")

# Calculate SSBR (Sum of Squares Between Rows)
ssbr = n_columns * np.sum((row_means - overall_mean) ** 2)
print(f"SSBR (Sum of Squares Between Rows): {ssbr:.3f}")

# Calculate SSBC (Sum of Squares Between Columns)
n_rows = x.shape[0]
ssbc = n_rows * np.sum((column_means - overall_mean) ** 2)
print(f"SSBC (Sum of Squares Between Columns): {ssbc:.3f}")

sse = sst - ssbc-ssbr
print(f"SSE (Sum of Squares Error): {sse:.3f}")

# Calculate degrees of freedom
df_rows = n_rows - 1
df_columns = n_columns - 1
df_error = (n_rows - 1) * (n_columns - 1)

# Calculate mean squares
ms_rows = ssbr / df_rows
ms_columns = ssbc / df_columns
ms_error = sse / df_error

# Calculate F-statistics
F_row = ms_rows / ms_error
F_col = ms_columns / ms_error

# Calculate p-values
p_value_row = 1 - f.cdf(F_row, df_rows, df_error)
p_value_col = 1 - f.cdf(F_col, df_columns, df_error)

print(f"F-statistic for Rows: {F_row:.3f}, p-value: {p_value_row:.5f}")
print(f"F-statistic for Columns: {F_col:.3f}, p-value: {p_value_col:.5f}")



# Calculate critical F-values for different significance levels
alpha_levels = [0.01, 0.05, 0.10]  # 1%, 5%, 10%

print("\nCritical F-values:")
print("Significance Level | Rows | Columns")
print("-" * 40)

for alpha in alpha_levels:
    # Calculate critical F-values
    f_crit_row = f.ppf(1 - alpha, df_rows, df_error)
    f_crit_col = f.ppf(1 - alpha, df_columns, df_error)
    
    # Print critical values
    print(f"{alpha*100:>17}% | {f_crit_row:.3f} | {f_crit_col:.3f}")

# Print interpretation
print("\nInterpretation:")
for alpha in alpha_levels:
    f_crit_row = f.ppf(1 - alpha, df_rows, df_error)
    f_crit_col = f.ppf(1 - alpha, df_columns, df_error)
    
    row_significant = F_row > f_crit_row
    col_significant = F_col > f_crit_col
    
    print(f"At {alpha*100}% significance level:")
    print(f"  - Row effect is {'significant' if row_significant else 'not significant'}")
    print(f"  - Column effect is {'significant' if col_significant else 'not significant'}")
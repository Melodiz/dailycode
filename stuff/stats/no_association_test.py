import scipy.stats as stats

X = [
    [47, 7], 
    [49, 30], 
    [65, 85]
]

# Calculate row sums
row_sums = [sum(row) for row in X]

# Calculate column sums
col_sums = [sum(col) for col in zip(*X)]

# Calculate grand total
grand_total = sum(row_sums)

# Calculate margins
row_margins = [row_sum / grand_total for row_sum in row_sums]
col_margins = [col_sum / grand_total for col_sum in col_sums]

print("Row margins:", row_margins)
print("Column margins:", col_margins)

# Calculate expected table
expected_table = []
for i in range(len(X)):
    expected_row = []
    for j in range(len(X[0])):
        expected_value = grand_total * row_margins[i] * col_margins[j]
        expected_row.append(round(expected_value, 2))
    expected_table.append(expected_row)

print("\nExpected table:")
for row in expected_table:
    print(row)

# Calculate chi-square statistic
chi_square_table = expected_table.copy()

chi_square = 0
for i in range(len(X)):
    for j in range(len(X[0])):
        observed = X[i][j]
        expected = expected_table[i][j]
        chi_square += (observed - expected) ** 2 / expected
        chi_square_table[i][j] = round((observed - expected) ** 2 / expected,2)

print("\nChi-square table:")
for row in chi_square_table:
    print(row)

print(f"\nChi-square statistic: {chi_square:.2f}")

# Calculate degrees of freedom
df = (len(X) - 1) * (len(X[0]) - 1)

# Calculate p-value
p_value = 1 - stats.chi2.cdf(chi_square, df)

print(f"Degrees of freedom: {df}")
print(f"p-value: {p_value:.4f}")
print(f"p-value: {100*p_value:.4f} %")


# Calculate critical values for different alpha levels
alpha_levels = [0.10, 0.05, 0.01]
critical_values = [stats.chi2.ppf(1 - alpha, df) for alpha in alpha_levels]

print("\nCritical values:")
for alpha, crit_value in zip(alpha_levels, critical_values):
    print(f"Alpha {100*alpha:.2f}%: {crit_value:.4f}")

# Compare chi-square statistic with critical values
print("\nComparison with critical values:")
for alpha, crit_value in zip(alpha_levels, critical_values):
    if chi_square > crit_value:
        print(f"Reject H0 at alpha = {alpha:.2f} (Chi-square {chi_square:.4f} > Critical value {crit_value:.4f})")
    else:
        print(f"Fail to reject H0 at alpha = {alpha:.2f} (Chi-square {chi_square:.4f} <= Critical value {crit_value:.4f})")

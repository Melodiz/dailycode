import scipy.stats as stats
import numpy as np

# Define observed values
observed = [100, 200, 250, 180]
n = len(observed)
total = sum(observed)

# Calculate expected values (assuming uniform distribution)
expected = [total/n] * n  # Each expected value is the total divided by number of categories

print(f"Observed values: {observed}")
print(f"Expected values: {[round(x, 2) for x in expected]}")

# Calculate chi-square statistic
chi_square = 63.35

print(f"\nChi-square calculation:")
for i in range(n):
    component = (observed[i] - expected[i])**2 / expected[i]
    print(f"({observed[i]} - {expected[i]:.2f})²/{expected[i]:.2f} = {component:.4f}")

print(f"\nChi-square statistic: {chi_square:.4f}")

# Calculate degrees of freedom (n-1 for goodness-of-fit test)
df = n - 1

# Calculate p-value
p_value = 1 - stats.chi2.cdf(chi_square, df)

print(f"Degrees of freedom: {df}")
print(f"p-value: {p_value:.6f}")
print(f"p-value: {100*p_value:.4f}%")

# Calculate critical values for different alpha levels
alpha_levels = [0.10, 0.05, 0.01]
critical_values = [stats.chi2.ppf(1 - alpha, df) for alpha in alpha_levels]

print("\nCritical values:")
for alpha, crit_value in zip(alpha_levels, critical_values):
    print(f"Alpha {100*alpha:.1f}%: {crit_value:.4f}")

# Compare chi-square statistic with critical values
print("\nComparison with critical values:")
for alpha, crit_value in zip(alpha_levels, critical_values):
    if chi_square > crit_value:
        print(f"Reject H0 at alpha = {alpha:.2f} (Chi-square {chi_square:.4f} > Critical value {crit_value:.4f})")
    else:
        print(f"Fail to reject H0 at alpha = {alpha:.2f} (Chi-square {chi_square:.4f} <= Critical value {crit_value:.4f})")
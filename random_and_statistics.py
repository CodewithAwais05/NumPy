import numpy as np

# ==========RANDOM NUMBER GENERATION==========

# Set seed for reproducibility
np.random.seed(42)

# Different distributions
uniform = np.random.uniform(0, 1, 1000)      # Uniform distribution (This generates 1000 random numbers between 0 and 1.)
#np.random.normal(mean, standard_deviation, size)
normal = np.random.normal(0, 1, 1000)        # Normal (Gaussian)(This generates 1000 values from a normal/Gaussian distribution.)
binomial = np.random.binomial(10, 0.5, 1000) # Binomial
poisson = np.random.poisson(3, 1000)         # Poisson
exponential = np.random.exponential(1, 1000) # Exponential

# Permutation
arr = np.array([1, 2, 3, 4, 5])
shuffled = np.random.permutation(arr)  # Shuffled copy
np.random.shuffle(arr)  # Shuffle in-place

# Choice
np.random.choice(arr, size=3, replace=False)  # Sample without replacement
np.random.choice(['a', 'b', 'c'], size=5, p=[0.1, 0.8, 0.1])  # Weighted


# ==========STATISTICAL FUNCTIONS==========

arr = np.random.normal(0, 1, 1000)

# Basic stats
print(f"Mean: {np.mean(arr)}")
print(f"Median: {np.median(arr)}")
print(f"Std: {np.std(arr)}")
print(f"Variance: {np.var(arr)}")
print(f"Skewness: {np.mean(((arr - np.mean(arr)) / np.std(arr)) ** 3)}")
print(f"Kurtosis: {np.mean(((arr - np.mean(arr)) / np.std(arr)) ** 4) - 3}")

# Percentiles
print(np.percentile(arr, [25, 50, 75]))  # Quartiles
print(np.quantile(arr, [0.25, 0.5, 0.75]))

# Correlation
x = np.random.randn(100)
y = 2 * x + np.random.randn(100) * 0.1
correlation = np.corrcoef(x, y)
print(correlation)  # Correlation matrix

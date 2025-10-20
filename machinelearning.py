import numpy as np

days = 365
num_cities = 5
base_temp = np.array([20, 16, 14, 18, 19]).reshape(num_cities, 1)

day_indices = np.arange(days)

# Small random amplitude variation for each city
amplitude = 10 + np.random.uniform(-2, 2, size=(num_cities, 1))

# Small random phase shift for each city
phase_shift = np.random.uniform(0, 2*np.pi, size=(num_cities, 1))

# Seasonal variation per city
sin_curve = amplitude * np.sin(2 * np.pi * day_indices / days + phase_shift)

# Random daily noise
random_noise = np.random.randint(-10, 11, size=(num_cities, days))

# Final temperature array
temperatures = base_temp + sin_curve + random_noise

print(temperatures)

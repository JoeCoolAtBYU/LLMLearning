python
def lcg(seed, a=1664525, c=1013904223, m=2**32):
    """
    Linear Congruential Generator (LCG) to produce a sequence of pseudo-random numbers.

    Parameters:
    seed (int): The initial seed value for generating the sequence.
    a (int): The multiplier. Default is 1664525.
    c (int): The increment. Default is 1013904223.
    m (int): The modulus. Default is 2^32.

    Yields:
    int: Next pseudo-random number in the sequence.
    """
    value = seed
    while True:
        value = (a * value + c) % m
        yield value

def max_subarray_sum(n, seed, min_val, max_val):
    """
    Calculate the maximum subarray sum of a list of random numbers generated using LCG.

    Parameters:
    n (int): The number of random numbers to generate.
    seed (int): Seed for the LCG to ensure reproducibility.
    min_val (int): Minimum possible value for the random numbers.
    max_val (int): Maximum possible value for the random numbers.

    Returns:
    int: The maximum sum of any contiguous subarray.
    """
    # Generate the random numbers using LCG
    lcg_gen = lcg(seed)
    random_numbers = [next(lcg_gen) % (max_val - min_val + 1) + min_val for _ in range(n)]
    
    max_sum = float('-inf')  # Initialize maximum sum as negative infinity for tracking
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += random_numbers[j]  # Accumulate the current sum
            if current_sum > max_sum:
                max_sum = current_sum  # Update the maximum sum if current sum is higher
    return max_sum

def total_max_subarray_sum(n, initial_seed, min_val, max_val):
    """
    Calculate the total of maximum subarray sums over 20 iterations with different seeds.

    Parameters:
    n (int): The number of random numbers to generate for each iteration.
    initial_seed (int): Initial seed for the LCG to ensure reproducibility.
    min_val (int): Minimum possible value for the random numbers.
    max_val (int): Maximum possible value for the random numbers.

    Returns:
    int: Total sum of the maximum subarray sums from 20 different sequences.
    """
    total_sum = 0
    lcg_gen = lcg(initial_seed)
    for _ in range(20):
        seed = next(lcg_gen)  # Get new seed for each iteration
        total_sum += max_subarray_sum(n, seed, min_val, max_val)  # Accumulate the total sum
    return total_sum

# Parameters for the simulation
n = 10000         # Number of random numbers to generate
initial_seed = 42 # Initial seed for the LCG
min_val = -10     # Minimum value for the random numbers
max_val = 10      # Maximum value for the random numbers

import time
start_time = time.time()
# Calculate the result
result = total_max_subarray_sum(n, initial_seed, min_val, max_val)
end_time = time.time()

# Output the results
print("Total Maximum Subarray Sum (20 runs):", result)
print("Execution Time: {:.6f} seconds".format(end_time - start_time))

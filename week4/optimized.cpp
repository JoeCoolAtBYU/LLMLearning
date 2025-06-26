#include <iostream>
#include <vector>
#include <cstdint>
#include <chrono>

// Linear Congruential Generator (LCG)
class LCG {
    std::uint32_t value;
    static constexpr std::uint32_t a = 1664525;
    static constexpr std::uint32_t c = 1013904223;
    static constexpr std::uint32_t m = 0x100000000; // 2^32

public:
    explicit LCG(std::uint32_t seed) : value(seed) {}

    std::uint32_t next() {
        value = (a * value + c) % m;
        return value;
    }
};

// Find maximum subarray sum using Kadane's algorithm
int64_t max_subarray_sum(int n, std::uint32_t seed, int min_val, int max_val) {
    LCG lcg_gen(seed);
    std::vector<int> random_numbers(n);
    for (int i = 0; i < n; ++i) {
        random_numbers[i] = lcg_gen.next() % (max_val - min_val + 1) + min_val;
    }

    int64_t max_sum = INT64_MIN, current_sum = 0;
    for (int& num : random_numbers) {
        current_sum = std::max(static_cast<int64_t>(num), current_sum + num);
        max_sum = std::max(max_sum, current_sum);
    }
    
    return max_sum;
}

int64_t total_max_subarray_sum(int n, std::uint32_t initial_seed, int min_val, int max_val) {
    int64_t total_sum = 0;
    LCG lcg_gen(initial_seed);
    for (int i = 0; i < 20; ++i) {
        std::uint32_t seed = lcg_gen.next();
        total_sum += max_subarray_sum(n, seed, min_val, max_val);
    }
    return total_sum;
}

int main() {
    int n = 10000;               // Number of random numbers
    std::uint32_t initial_seed = 42; // Initial seed for the LCG
    int min_val = -10;           // Minimum value of random numbers
    int max_val = 10;            // Maximum value of random numbers

    // Timing the function
    auto start_time = std::chrono::high_resolution_clock::now();
    int64_t result = total_max_subarray_sum(n, initial_seed, min_val, max_val);
    auto end_time = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed = end_time - start_time;

    std::cout << "Total Maximum Subarray Sum (20 runs): " << result << std::endl;
    std::cout << "Execution Time: " << elapsed.count() << " seconds" << std::endl;

    return 0;
}

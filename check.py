from multiprocessing import Pool

def luhn_checksum_optimized(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    
    # Precompute sum of digits for double of digits 0-9
    double_digit_sums = [sum(digits_of(i * 2)) for i in range(10)]

    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = sum(odd_digits) + sum(double_digit_sums[d] for d in even_digits)
    return checksum % 10

def count_valid_in_range(start, end):
    count = 0
    for i in range(start, end):
        if luhn_checksum_optimized(i) == 0:
            count += 1
    return count

def generate_valid_numbers_parallel():
    # Divide the range into chunks of 1,000,000 numbers
    ranges = [(start, start + 1000000) for start in range(10000000, 100000000, 1000000)]
    
    # Use multiprocessing to count valid numbers in parallel
    with Pool() as pool:
        results = pool.starmap(count_valid_in_range, ranges)
    
    return sum(results)

if __name__ == "__main__":
    total_valid = generate_valid_numbers_parallel()
    print(f"Total number of valid 8-digit numbers: {total_valid}")
    print(f"Percentage of valid numbers: {(total_valid / 90000000) * 100:.2f}%")

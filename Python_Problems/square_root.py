def calculate_square_root(N, tolerance=1e-10):
    if N < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    
    if N == 0:
        return 0
    
    guess = N / 2.0  # Initial guess
    while True:
        better_guess = (guess + N / guess) / 2.0
        if abs(guess - better_guess) < tolerance:
            return better_guess
        guess = better_guess

# Example usage
N = 35
result = calculate_square_root(N)
print(f"The square root of {N} is {result}")

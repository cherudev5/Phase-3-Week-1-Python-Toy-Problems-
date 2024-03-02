def solution(N):
    # Validate input range
    if N < 1 or N > 200000:
        raise ValueError("N should be an integer within the range [1..200,000]")

    # Initialize variables
    alphabet_size = min(N, 26)
    equal_occurrences = N // alphabet_size
    remaining_letters = N % alphabet_size

    # Generate the string with equal occurrences of each letter
    result = ''.join(chr(ord('a') + i) * equal_occurrences for i in range(alphabet_size))

    # Add remaining letters if any
    result += ''.join(chr(ord('a') + i) for i in range(remaining_letters))

    return result
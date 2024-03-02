def solution(A):
    # Create a dictionary to store the sums of digits for each number in A
    sums_of_digits = {}
    for num in A:
        sum_of_digits = sum(int(digit) for digit in str(num))
        if sum_of_digits not in sums_of_digits:
            sums_of_digits[sum_of_digits] = [num]
        else:
            sums_of_digits[sum_of_digits].append(num)

    # Find the maximum sum of two numbers whose digits add up to an equal sum
    max_sum = -1
    for sum_of_digits in sums_of_digits:
        if len(sums_of_digits[sum_of_digits]) >= 2:
            # Sort the numbers in descending order
            numbers = sorted(sums_of_digits[sum_of_digits], reverse=True)
            # Find the maximum sum of two numbers from the same list
            max_sum = max(max_sum, numbers[0] + numbers[1])
            # If there are at least 3 numbers with the same sum of digits,
            # find the maximum sum of two numbers from the first two numbers
            if len(numbers) >= 3:
                max_sum = max(max_sum, numbers[0] + numbers[2])

    return max_sum



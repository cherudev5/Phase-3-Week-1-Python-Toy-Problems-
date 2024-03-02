def solution(A):
    N = len(A)
    target_bricks = 10

    # Calculate the total number of bricks in the given boxes,sum of all boxes in the array
    total_bricks = sum(A)

    # Check if it is possible to distribute the bricks equally if not divisibe with 10 return -1
    if total_bricks % N != 0:
        return -1

    # Calculate the target number of bricks per box
    target_per_box = total_bricks // N

    # Initialize variables for moves and current excess/deficit of bricks
    moves = 0
    current_diff = 0

    # Iterate through the boxes and calculate the moves needed
    for i in range(N):
        current_diff += A[i] - target_per_box

        # Calculate moves needed to reach target bricks in the current box
        moves += abs(current_diff)

    return moves



class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        n = len(A)
        flip = [0] * n  # Flip tracker
        num_flips = 0  # Total number of flips
        current_flips = 0  # Ongoing flips in the current window

        for i in range(n):
            if i >= K:
                current_flips ^= flip[i - K]  # Undo the effect of the flip that goes out of the window

            if A[i] == current_flips % 2:  # If current bit is 0 after the flips
                if i + K > n:  # If we cannot flip because we are out of bounds
                    return -1
                flip[i] = 1  # Mark this position as flipped
                current_flips ^= 1  # Update current flips
                num_flips += 1  # Increment the flip count

        return num_flips
from typing import List

class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # prefix sum per column
        pref = [[0]*n for _ in range(n+1)]
        for j in range(n):
            for i in range(n):
                pref[i+1][j] = pref[i][j] + grid[i][j]

        dp = [[0]*n for _ in range(n)]

        for j in range(1, n):
            for h in range(n):
                best = 0
                for prev_h in range(n):
                    val = dp[j-1][prev_h]

                    if prev_h < h:
                        # take from left column
                        val += pref[h][j-1] - pref[prev_h][j-1]
                    elif prev_h > h:
                        # take from current column
                        val += pref[prev_h][j] - pref[h][j]

                    best = max(best, val)

                dp[j][h] = best

        return max(dp[n-1])
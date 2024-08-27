class solution:
    def task1(self, N, K):
        if K == 0:
            return 0
        
        dp = [float('inf')] * (K + 1)
        dp[0] = 0

        for i in range(1, N + 1):
            for j in range(K, i - 1, -1):
                dp[j] = min(dp[j], dp[j - i] + 1)
        
        if dp[K] != float('inf'):
            return dp[K]
        return -1
    
    def task2(self, A, B):
        N = len(A)

        prefix_sum_A = [0] * (N + 1)
        prefix_sum_B = [0] * (N + 1)

        for i in range(1, N + 1):
            prefix_sum_A[i] = prefix_sum_A[i - 1] + A[i - 1]
            prefix_sum_B[i] = prefix_sum_B[i - 1] + B[i - 1]
        
        res = 0
        for K in range(1, N):
            if prefix_sum_A[K] == prefix_sum_A[N] - prefix_sum_A[K] and \
               prefix_sum_B[K] == prefix_sum_B[N] - prefix_sum_B[K] and \
               prefix_sum_A[K] == prefix_sum_B[K]:
                res += 1
        return res
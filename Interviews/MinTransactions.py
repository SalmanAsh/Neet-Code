def getMinTransactions(n, debts):
    # Calculate the net balance of each person
    balance = [0] * n
    for debt in debts:
        from_person, to_person, amount = debt
        balance[from_person] -= amount
        balance[to_person] += amount
    
    # Filter out the people with zero balance as they don't need any transactions
    balance = list(filter(lambda x: x != 0, balance))
    
    def dfs(balance, start):
        # Skip settled balances
        while start < len(balance) and balance[start] == 0:
            start += 1
        
        if start == len(balance):
            return 0
        
        min_transactions = float('inf')
        
        for i in range(start + 1, len(balance)):
            if balance[start] * balance[i] < 0:
                # Try to settle start with i
                balance[i] += balance[start]
                min_transactions = min(min_transactions, 1 + dfs(balance, start + 1))
                # Backtrack
                balance[i] -= balance[start]
        
        return min_transactions
    
    return dfs(balance, 0)
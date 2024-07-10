def minCoins(coins, m, V):
	
	table = [0 for i in range(V + 1)]
	table[0] = 0

	for i in range(1, V + 1):
		table[i] = 32767

	for i in range(1, V + 1):
		for j in range(m):
			if (coins[j] <= i):
				sub_res = table[i - coins[j]]
				if (sub_res != 32767 and
					sub_res + 1 < table[i]):
					table[i] = sub_res + 1
	
	if table[V] == 32767 :
		return -1
	
	return table


coins = [9, 6, 5, 1]
m = len(coins)
V = 11
res = minCoins(coins, m, V)
print("Minimum coins required is ", res[V] )
print("Table: ", res)


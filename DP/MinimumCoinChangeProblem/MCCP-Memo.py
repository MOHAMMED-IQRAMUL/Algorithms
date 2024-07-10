import sys

def minCoinsUtil(coins, m, V, dp):
	if V == 0:
		return 0
	if dp[V] != -1:
		return dp[V]
 
	res = sys.maxsize

	for i in range(m):
		if coins[i] <= V:
			sub_res = minCoinsUtil(coins, m, V - coins[i], dp)

			if sub_res != sys.maxsize and sub_res + 1 < res:
				res = sub_res + 1

	dp[V] = res

	return res

def minCoins(coins, m, V):
	dp = [-1] * (V + 1)
	return minCoinsUtil(coins, m, V, dp)


if __name__ == "__main__":
	coins = [9, 6, 5, 1]
	m = len(coins)
	V = 11
	res = minCoins(coins, m, V)

	if res == sys.maxsize:
		res = -1
	print("Minimum coins required is", res)

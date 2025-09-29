#the number of ways we can change a money using a predifined coin list

#Input Format
#First line will contain 2 integer N (money) and M (list of coins) respectively.
#Second line contain M integer that represent list of distinct coins that are available in infinite amount.


#Output Format
#One integer which is the number of ways in which we can get a sum of N from the given infinite supply of M types of coins.

#nuWays[m][c]:  the number of ways we can construct the sum m using the first c coins
#list of coins are predetermined and definite

arr=map(int,raw_input("Enter the amount of money and the number of coins: ").strip().split())
coins=map(int, raw_input("Enter the list of coins: ").strip().split())
money=arr[0]
nuCoins=arr[1]

nuWays=[[0 for i in range(nuCoins+1)] for j in range(money+1)]
for i in range(nuCoins+1):
    nuWays[0][i]=1
for i in range(money+1):
    nuWays[i][0]=0

for m in range(1,(money+1)):
    for c in range(1,(nuCoins+1)):
        if(coins[c-1]< money):
            if (m - coins[c - 1] >= 0):
                nuWays[m][c]=nuWays[m-coins[c-1]][c]+nuWays[m][c-1]
            else:
                nuWays[m][c] =  nuWays[m][c - 1]

print(str(nuWays[money][nuCoins]).strip())

#nuWays[m][c]: how many ways we can get the sum of m using the first c coins we have in nuCoins[:c+1]
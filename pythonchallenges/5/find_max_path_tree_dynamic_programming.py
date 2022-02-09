
dp = [0]*100

def dfs(a, v, u, parent):

    dp[u] = a[u - 1]
     
    maximum = 0

    for child in v[u]:

        if child == parent:
            continue
         
        dfs(a, v, child, u)

        maximum = max(maximum, dp[child])
         
    dp[u] += maximum
 

def maximumValue(a, v):
    dfs(a, v, 1, 0)
    print(dp)
    return dp[1]
 
def main():
     
    n = 14
     
    v = {}
    for i in range(n + 1):
        v[i] = []
         
    v[1].append(2), v[2].append(1)
    v[1].append(3), v[3].append(1)
    v[1].append(4), v[4].append(1)
    v[2].append(5), v[5].append(2)
    v[2].append(6), v[6].append(2)
    v[3].append(7), v[7].append(3)
    v[4].append(8), v[8].append(4)
    v[4].append(9), v[9].append(4)
    v[4].append(10), v[10].append(4)
    v[5].append(11), v[11].append(5)
    v[5].append(12), v[12].append(5)
    v[7].append(13), v[13].append(7)
    v[7].append(14), v[14].append(7)
     
    a = [ 3, 2, 1, 10, 1, 3, 9,
          1, 5, 3, 4, 5, 9, 8 ]
     
    print(maximumValue(a, v))
main()

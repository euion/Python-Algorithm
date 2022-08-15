N, K = map(int,input().split())

def bottleSum(N, K):
    answer = 0
    while bin(N).count('1') > K:
        findOne = bin(N)[::-1].index('1') 
        answer += 2 ** findOne 
        N += 2 ** findOne 
    return answer

print(bottleSum(N,K))
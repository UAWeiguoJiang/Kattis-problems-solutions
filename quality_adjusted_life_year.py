# https://open.kattis.com/submissions/5986184
years = int(input())

qaly = 0
for _ in range(0, years):
    q, p = list(map(float, input().split()))
    qaly += q * p 
print(qaly) 

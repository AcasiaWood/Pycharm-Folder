memory = [[-1]*100]*100

def binomial_coefficient(n, k):
    if memory[n][k] != -1:
        return memory[n][k]
    if n == k or n == 0 or k == 0:
        memory[n][k] = 1
        return memory[n][k]
    memory[n][k] = binomial_coefficient(n-1, k-1) + binomial_coefficient(n-1, k)
    return memory[n][k]

n = int(input())
triangle = []

for i in range(n+1):
    triangle.append(binomial_coefficient(n, i))
print(triangle)
# enter the string value.
a, b = map(str, input().split())
flag = False
# insert the number of the alphabet.
alpha = [0]*26
beta = [0]*26
# compare two string's length.
if len(a) != len(b):
    flag = False
else:
    # append the individual string's alphabet numbers.
    for i in range(len(a)):
        alpha[ord(a[i]) - ord('a')] += 1
        beta[ord(b[i]) - ord('a')] += 1
    if alpha == beta:
        flag = True
print(alpha, beta)
if flag:
    print('It is anagram.')
else:
    print('It is not anagram')

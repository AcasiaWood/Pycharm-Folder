# encryption

data = 'NICE TO MEET YOU'
encrypted = ''
char_dist = 3
print('Before Encrypted: '+data)
for i in range(len(data)):
    if data[i] == '  ':
        encrypted += '  '
        continue
    temp = ord(data[i]) + char_dist
    if temp > ord('Z'):
        temp = temp - ord('Z') + 64
    encrypted += chr(temp)
print('After Encrypted: '+encrypted)

# decryption

data = 'NICE TO MEET YOU'
decrypted = ''
char_dist = -3
print('Before Decryption: '+encrypted)
for j in range(len(encrypted)):
    if encrypted[j] == '  ':
        decrypted += '  '
        continue
    temp = ord(encrypted[j]) + char_dist
    if temp < ord('A'):
        temp += 26
    decrypted += chr(temp)
print('After Decrypted: '+decrypted)

# encode

data = input('Enter the Data: ')
encoded = ''
count = 1
print('Before Encoding: '+data)
for i in range(1, len(data)):
    flag = 0
    if data[i] == data[i-1]:
        count += 1
    else:
        encoded += data[i-1] + str(count)
        count = 1
    if i == len(data)-1:
        encoded += data[i] + str(count)
print('After Encoding: '+encoded)

# decode

data = input('Enter the Data: ')
decoded = ''
decoded_list = []
save_data = ''
combination = []
j = 0
print('Before Decoding: '+encoded)
for i in range(1, len(encoded), 2):
    decoded += encoded[i-1]*int(encoded[i])
print('After Decoding: '+decoded)

# machine running model

def step(x):
    if x >= 0:
        return 1
    else:
        return 0

inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
outputs = [0, 0, 0, 0]
targets = [0, 1, 1, 1]

threshold = 0.2
learning_rate = 0.1
weight = [0.1, 0.1]

epoch = 1

while True:
    print("----------------------%d번째 학습----------------------" % epoch)
    for p in range(4):
        temp = 0
        for i in range(2):
            temp += inputs[p][i]*weight[i]-threshold
        outputs[p] = step(temp)
        nextWeight = [0.0, 0.0]
        for i in range(2):
            nextWeight[i] = weight[i]+learning_rate*inputs[p][i]*(targets[p]-outputs[p])
        print("입력: {0}| 출력: {1}| 목표: {2}| 변경 전 가중치: {3}| 변경 후 가중치: {4}"
              .format(inputs[p], outputs[p], targets[p], weight, nextWeight, ))
        weight = nextWeight
    epoch += 1
    if outputs == targets:
        break
print('DONE!')

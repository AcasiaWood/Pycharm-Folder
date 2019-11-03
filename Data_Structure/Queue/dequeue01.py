def dequeue():
    if len(queue) == 0:
        print("underflow")
        return
    else:
        print(queue[0])
        del queue[0]
        return
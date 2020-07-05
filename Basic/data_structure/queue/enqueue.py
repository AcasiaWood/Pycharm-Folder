def enqueue(num):
    if len(queue) > max:
        print("overflow")
        return
    else:
        queue.append(num)

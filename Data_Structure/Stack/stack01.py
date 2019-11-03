def push():
    if (len(stack) > limit):
        print("overflow")

    b = random.randrange(10)

    stack.append(b)


def pop():
    if (len(stack) == 0):

        print("You can`t pop them")

    else:

        print(stack)

        del stack[len(stack) - 1]

        print(stack)
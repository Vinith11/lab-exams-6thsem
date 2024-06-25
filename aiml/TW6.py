#TW 6

# OR Gate
def OR():
    w1 = 0
    w2 = 0
    a = 0.2
    t = 0
    X = [[0, 0], [0, 1], [1, 0], [1, 1]]
    Y = [0, 1, 1, 1]
    while True:
        Out = []
        count = 0
        for i in X:
            step = (w1 * i[0] + w2 * i[1])
            if step <= t:
                O = 0
            else:
                O = 1
            if O == Y[count]:
                Out.append(O)
                count += 1
            else:
                if step <= t:
                    w1 += a * i[0]
                    w2 += a * i[1]
                    print("w1={} w2={}".format(round(w1, 2), round(w2, 2)))
                print(w1, w2, Out)
        print("------->")
        if Out == Y:
            print("Final Output of OR ::\n")
            print("Weights: w1={} and w2={} >>>> {}".format(w1, w2, Out))
            break

OR()

# AND Gate
def AND():
    w1 = 0
    w2 = 0
    a = 0.2
    t = 1
    X = [[0, 0], [0, 1], [1, 0], [1, 1]]
    Y = [0, 0, 0, 1]
    while True:
        Out = []
        count = 0
        for i in X:
            step = (w1 * i[0] + w2 * i[1])
            if step < t:
                O = 0
            else:
                O = 1
            if O == Y[count]:
                Out.append(O)
                count += 1
            else:
                print('Weights changed to..')
                w1 += a * i[0]
                w2 += a * i[1]
                print("w1={} w2={}".format(round(w1, 2), round(w2, 2)))
            print(w1, w2, Out)
            print("------->")
        if Out == Y:
            print("\nFinal Output of AND::\n")
            print("Weights: w1={} and w2={} >>>> {}".format(round(w1, 2), round(w2, 2), Out))
            break

AND()

# NOT Gate
def NOT():
    X = [0, 1]
    Y = [1, 0]
    weight = -1
    bias = 1
    Out = []
    for i in X:
        j = weight * i + bias
        if j >= 0:
            Out.append(1)
        else:
            Out.append(0)
    print("\nFinal Output of NOT ::\n")
    for i in range(len(X)):
        print("NOT Gate {}--> {}".format(X[i], Out[i]))

NOT()

# AND
def AND():
    w1 = 0
    w2 = 0
    a = 0.2
    t = 1
    X = [[0, 0], [0, 1], [1, 0], [1, 1]]
    Y = [0, 0, 0, 1]
    Out = []
    
    while True:
        count = 0
        Out = []
        for i in X:
            step = (w1 * i[0] + w2 * i[1])
            if step <= t:
                O = 0
                if O == Y[count]:
                    Out.append(O)
                    count += 1
                    print(w1, w2, Out)
                else:
                    print("Weights changed to..")
                    w1 = w1 + (a * i[0] * 1)
                    w2 = w2 + (a * i[1] * 1)
                    print("w1={} w2={}".format(round(w1, 2), round(w2, 2)))
                    print("---------->")
            else:
                O = 1
                if O == Y[count]:
                    Out.append(O)
                    count += 1
                    print(w1, w2, Out)
                else:
                    print("Weights changed to..")
                    w1 = w1 + (a * i[0] * 0)
                    w2 = w2 + (a * i[1] * 0)
                    print("w1={} w2={}".format(round(w1, 2), round(w2, 2)))
                    print("---------->")
        
        if Out[:] == Y[:]:
            print("\nFinal Output of AND::\n")
            print("Weights: w1={} and w2={} >>> {}".format(round(w1, 2), round(w2, 2), Out))
            break

AND()

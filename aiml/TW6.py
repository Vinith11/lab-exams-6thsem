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


# OR Gate
def OR():
    w1 = 0  # Initialize weight 1
    w2 = 0  # Initialize weight 2
    a = 0.2  # Learning rate
    t = 0  # Threshold

    X = [[0, 0], [0, 1], [1, 0], [1, 1]]  # Training data (inputs)
    Y = [0, 1, 1, 1]  # Desired outputs

    while True:  # Loop until convergence
        Out = []  # List to store outputs for each iteration
        count = 0

        for i in X:  # Iterate through training data
            step = w1 * i[0] + w2 * i[1]  # Calculate weighted sum of inputs

            if step <= t:  # Check if weighted sum is less than or equal to threshold
                if Out == Y[0:count]:  # Check if previous outputs match desired outputs so far
                    O = 0
                else:
                    O = 0  # No update for weights here (weights are only updated when output doesn't match)
            else:
                O = 1  # Output is 1 (activation)

                # Update weights based on Hebbian learning rule (increase for matching inputs)
                w1 += a * i[0] * 1
                w2 += a * i[1] * 1

            Out.append(O)  # Append output to list
            count += 1  # Increment counter for desired output

        print("------->")  # Print separator after each iteration

        # Check if output matches desired output for all inputs
        if Out == Y:
            print("Final Output of OR::\n")
            print("Weights: w1={} and w2={} >>>> {}".format(w1, w2, Out))
            break  # Break out of loop if convergence is achieved

    OR()


# NOT Gate
def NOT():
  X = [0, 1]  # Input values
  Y = [1, 0]  # Desired output values (opposite of input)
  weight = -1  # Initial weight
  bias = 1  # Initial bias
  Out = []  # List to store outputs

  for i in X:
    j = weight * i + bias  # Calculate weighted sum of input and bias
    Out.append(j)  # Append output to the list

    # Print Output with label
    print("\nFinal Output of NOT ::\n")
    print("NOT Gate {} --> {}".format(i, Out[Out.index(j)]))

NOT()

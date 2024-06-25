x1=[1,1]
x2=[1,-1]
x3=[-1,1]
x4=[-1,-1]
xilist=[x1, x2,x3,x4]
y=[1,-1,-1,-1]

w1=w2=bw=0
b=1

def heb_learn():
    global w1, w2, bw
    print("dw1\tdw2\tdb\twl\tw2\tb")
    for i in range(len(xilist)):
        dwl = xilist[i][0] * y[i]
        dw2 = xilist[i][1] * y[i]
        db = y[i]
        w1 = w1 + dwl
        w2 = w2 + dw2
        bw += db
        print(dwl, dw2, db, w1, w2, bw, sep='\t')

print("Learning...")
heb_learn()

print("Learning completed")

print("Output of AND gate using obtained w1,w2,bw:")
print("x1\tx2\ty")

for xi in xilist:
    output = 1 if w1*xi[0] + w2*xi[1] + b*bw > 0 else 0
    print(xi[0], xi[1], output, sep='\t')
print("Final weights are: wl=" + str(w1) + " w2=" + str(w2))

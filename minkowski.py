import matplotlib.pyplot as plt

def minkowski_curve(p1, p2, depth):
    print(depth)
    if depth == 0:
        return [p1, p2]

    x1, y1 = p1
    x2, y2 = p2

    dx = (x2 - x1) / 4
    dy = (y2 - y1) / 4

    pA = (x1, y1)
    pB = (x1 + dx, y1 + dy)
    pC = (pB[0] - dy, pB[1] + dx)
    pD = (pC[0] + dx, pC[1] + dy)
    pE = (pD[0] + dy, pD[1] - dx)
    pF = (pE[0] + dy, pE[1] - dx)
    pG = (pF[0] + dx, pF[1] + dy)
    pH = (pG[0] - dy, pG[1] + dx)
    pI = (x2, y2)

    points = []

    segments = [(pA,pB),(pB,pC),(pC,pD),(pD,pE),
                (pE,pF),(pF,pG),(pG,pH),(pH,pI)]

    for s in segments:
        part = minkowski_curve(s[0], s[1], depth-1)
        points += part[:-1]
    

    points.append(pI)
    return points


# segment initial
p1 = (0,0)
p2 = (1,0)
#p3=(0,1)
#p4=(1,1)
points1 = minkowski_curve(p1, p2, 4)
#points2 = minkowski_curve(p1, p3, 4)
#points3 = minkowski_curve(p3, p4, 4)
#points4 = minkowski_curve(p2, p4, 4)
x1 = [p[0] for p in points1]
y1 = [p[1] for p in points1]
#x2 = [p[0] for p in points2]
#y2 = [p[1] for p in points2]
#x3 = [p[0] for p in points3]
#y3 = [p[1] for p in points3]
#x4 = [p[0] for p in points4]
#y4 = [p[1] for p in points4]

plt.figure(figsize=(8,4))
plt.plot(x1,y1,color="black")
#plt.plot(x2,y2,color="black")
#plt.plot(x3,y3,color="black")
#plt.plot(x4,y4,color="black")
plt.axis("equal")
plt.axis("off")
plt.show()

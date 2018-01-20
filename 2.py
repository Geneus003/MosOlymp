a = int(input())
b = True
j = 0
g = [1, 2, 5, 10, 50, 100, 500, 1000, 5000, 10000000]

def sch(a):

    u = 0
    def something(a,u):
        for i in range(0,9,1):
            if (g[i + 1] > a) and (a >= (2 * g[i]) and (a != 0)):
                    a -= 2*g[i]
                    if a == 0:
                        return True
                        u = 1
                    else:
                        if something(a,u) == True:
                            return True
                            u = 1

        if u == 0:
            return False


    k = something(a,u)

    if k == True:
        print("YES")
    elif k == False:
        print("NO")


if a == 1 or a == 2 or a == 5 or a == 10 or a == 50 or a == 100 or a == 500 or a == 1000 or a == 5000:
    print("NO")
else:
    sch(a)
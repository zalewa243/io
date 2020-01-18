def F_A():
    F_B()
    print("wywołano F_A")

def F_B():
    F_A()
    print("wywołano F_B")

def F_C():
    print("wywołano F_C")
    F_A()
    F_B()
    F_A()

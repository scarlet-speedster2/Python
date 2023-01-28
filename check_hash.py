
def fixed(o):

    try:
        hash(o)

    except:
        return False
    return True


t = (1,2,(1,3))
tt = (1,2,[1,3])
print(fixed(t))
print(fixed(tt))


pole={}

def add(k):
    global pole
    if pole.has_key(k):
        pole[k] += 1
    else:
        pole[k]=1
        
def spocti(s):
    x,y = 0,0
    suma = 0
    add("x0y0")
    for c in s:
        if c == '>': x += 1
        elif c == "<": x -= 1
        elif c == "^": y += 1
        elif c == "v": y -= 1
        else: continue
        
        k='x'+str(x)+'y'+str(y)
        add(k)
    
    return len(pole)



print spocti(open("03.in").read())


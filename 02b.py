



file=open("02.in")

suma=0

while True:
    line=file.readline()
    line=line.strip('\n')
    if line == "":
        break
    line=line.split("x")

    a=int(line[0])
    b=int(line[1])
    c=int(line[2])
    
    s=[a,b,c]
    s.sort()
    
    a=s[0]
    b=s[1]
    c=s[2]

    suma+=2*(a+b)+a*b*c

print suma

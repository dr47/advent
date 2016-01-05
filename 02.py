



file=open("01.in")

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
    
    ab=a*b
    ac=a*c
    bc=b*c
    
    mini=min(ab,ac,bc)
    size=(ab+ac+bc)*2+mini
    suma+=size

    #print line
    
#    print int(line[0])

    
print suma



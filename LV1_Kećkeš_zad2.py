try:
    ocijena = float(input())

    if(ocijena>1):
        print("broj prevelik")
    elif(ocijena >=0.9):
        print("A")
    elif(ocijena >=0.8):
        print("B")
    elif(ocijena >=0.7):
        print("C")
    elif(ocijena >=0.6):
        print("D")
    elif(ocijena <0.6 and ocijena >= 0):
        print("F")
    else:
        print("broj premal")
except:
    print("nije unesen broj")
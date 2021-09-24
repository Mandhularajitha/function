def fname(speed):
    if speed<70:
        print("ok")
    else:
        a=[0,70,80,90,100,110,120,130,140,150,160,170,180]
        i=0
        while i<len(a):
            if a[i]>=speed:
                print(i,"point")
                break
            if i>=12:
                print("lines suspended")
            i=i+1
n=int(input("enter num"))            
fname(n)            

def ice_cream(*flavours):
    i=0
    while i<len(flavours):
        print("i love"+str(flavours[i]))
        i=i+1

ice_cream("chocolate", "butterscotch","vanilla","strawberry")
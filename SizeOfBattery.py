def SizeOfBattery(l,M,volts):

    print("Different types of batteries and their values are shown here")
    Types={"12":3659,"24":18689,"48":72399,"96":126000,"120":150000}
    print("Price increases with number of days")
    for x,y in Types.items():
        print(x,"Volts : Rs",y)

   
    BatteryCost=Types[str(volts)]*M
    return BatteryCost

    
    





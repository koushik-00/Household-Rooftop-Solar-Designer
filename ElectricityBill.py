def ElectricityBill(units):
    if(units<=200):
        payAmount=units*5
        fixedcharge=60.00
    elif(units<=300):
        payAmount=(200*5)+(units-200)*7.2
        fixedcharge=60.00
    elif(units<=400):
        payAmount=(200*5)+(100)*7.2+(units-300)*8.5
        fixedcharge=80.00
    elif(units<=800):
        payAmount=(200*5)+(100)*7.2+(100)*8.5+(units-400)*9
        fixedcharge=80.00
    else:
        payAmount=(200*5)+(100)*7.2+(100)*8.5+(400)*9+(units-800)*9.5
        fixedcharge=80.00
    Total=payAmount+fixedcharge+units*0.06;
    return Total

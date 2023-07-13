def FinalAmount(Amount,SolarArrayNumber):
    if SolarArrayNumber<=3:
        FAmount=Amount-0.4*Amount
    elif SolarArrayNumber==4:
        FAmount=2*((2/4*Amount)-0.4*(2/4*Amount))
    elif SolarArrayNumber==5:
        FAmount=(3/5*Amount)-0.4*(3/5*Amount)+(2/5*Amount)-0.4*(2/5*Amount)
    elif SolarArrayNumber==6:
        FAmount=2*((3/6*Amount)-0.4*(3/6*Amount))
    elif SolarArrayNumber==7:
        FAmount=2*((3/7*Amount)-0.4*(3/7*Amount))+(1/7*Amount)-0.4*(1/7*Amount)
    elif SolarArrayNumber==8:
        FAmount=2*((3/8*Amount)-0.4*(3/8*Amount))+(2/8*Amount)-0.4*(2/8*Amount)
    elif SolarArrayNumber==9:
        FAmount=3*((3/9*Amount)-0.4*(3/9*Amount))
    elif SolarArrayNumber==10:
        FAmount=3*((3/10*Amount)-0.4*(3/10*Amount))+(1/10*Amount)-0.4*(1/10*Amount)
    elif SolarArrayNumber==11:
        FAmount=3*((3/11*Amount)-0.4*(3/11*Amount))+(2/11*Amount)-0.4*(2/11*Amount)
    Subsidy=Amount-FAmount
    return FAmount,Subsidy


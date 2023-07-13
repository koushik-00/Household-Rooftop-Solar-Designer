from FinalAmount import FinalAmount
def MainModule(X,Q,P,M):
    from Invertor import soi
    from NoOfSolarCells import nsc
    from functools import reduce
    from ElectricityBill import ElectricityBill
    from Output import Output
    Units=X
    BillCal=ElectricityBill(Units)
    global SolarArrayNumber
    SolarArrayNumber=((Units/30)/5)//0.8+1
    print("\nThe output of the solar PV Design :",SolarArrayNumber,"kW\n")
    NoOfPanels,CostOfPanels=nsc(SolarArrayNumber,Q)
    print("\nThe number of panels required :",NoOfPanels)
    print("The total cost of the panels : Rs",CostOfPanels)
    Invertorcost,BatteryCost=soi(SolarArrayNumber*1000,P,M)
    print("The cost of Invertor : ",Invertorcost)
    print("The cost of Battery : ",BatteryCost)

    CGST = 0.025
    SGST = 0.025
    NonTaxAmount = (CostOfPanels + Invertorcost + BatteryCost)
    CGSTAmount=0.025*NonTaxAmount
    Tax = NonTaxAmount * (SGST+CGST)
    Amount = NonTaxAmount + Tax
    NonTaxAmount2=NonTaxAmount+2500+3000
    Tax2=Tax+225+225+270+270
    FullTaxAmount=NonTaxAmount2+Tax2
    print(Amount)
    FAmount,subsidy=FinalAmount(FullTaxAmount,SolarArrayNumber)
    print(FAmount)
    Output(SolarArrayNumber,CGSTAmount,NonTaxAmount,Amount,FAmount,NonTaxAmount2,Tax2,FullTaxAmount,subsidy)



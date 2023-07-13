from SizeOfBattery import SizeOfBattery
def soi(n,P,M):
    print("This is your power consumption a day:",n)
    if P==1:

        dict = {
            "750": 4564,
            "1100": 5694,
            "1400": 7099,
            "1600": 7990,
            "2335": 11750,
            "2550": 15750,
            "5000": 145000,
            "7500": 75000,
            "10000": 150000
        }

        if n<750:
            volts=12
            choice="750"
        elif 750<=n<1100:
            volts=12
            choice="1100"
        elif 1100<=n<1400:
            volts=12
            choice="1400"
        elif 1400<=n<1600:
            volts=12
            choice="1600"
        elif 1600<=n<2335:
            volts=24
            choice="2335"
        elif 2335<=n<2550:
            volts=24
            choice="2550"
        elif 2550<=n<5000:
            volts=48
            choice="5000"
        elif 5000<=n<=7500:
            volts=96
            choice="7500"
        elif 7500<=n<=11000:
            volts=120
            choice="10000"

        Invertorcost=dict[choice]
        BatteryCost=SizeOfBattery(n,M,volts)


    elif P == 2:
        a={
            "1000": 22619,
            "2000": 26390,
            "3000": 28500,
            "3200": 32686,
            "3600": 36871,
            "4000": 41017,
            "4600": 42977,
            "5000": 46748,
            "5500": 76892,
            "6600": 78415,
            "8800": 85954,
            "10000": 90479,
            "11000": 93494
        }
        print("These are the options for On-grid system:")
        for x,y in a.items():
            print(x, "W", ": Rs", y)

        if n<=1000:
            choice="1000"
        elif 1000< n <= 2000:
            choice="2000"
        elif 2000< n <= 3000:
            choice="3000"
        elif 3000<n <=3200:
            choice="3200"
        elif 3200< n <=3600:
            choice="3600"
        elif 3600< n <=4000:
            choice="4000"
        elif 4000<n <=4600:
            choice="4600"
        elif 4600<n <=5000:
            choice="5000"
        elif 5000< n <=5500:
            choice="5500"
        elif 5500< n <=6600:
            choice="6600"
        elif 6600<n <=8800:
            choice="8800"
        elif 8800< n <=10000:
            choice="10000"
        elif 10000< n <=11000:
            choice="11000"

        Invertorcost=a[choice]
        BatteryCost=0
    return Invertorcost,BatteryCost




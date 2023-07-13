#number of solar panels
def nsc(n,Q):
     n*=1000
     print("Select the voltage of solar  cells required from the given options:")
     dict={
         "60": 3100,
         "165": 6900,
         "350": 13000
     }
     for x,y in dict.items():
         print (x,"W",": Rs",y)
     cs=str(Q)
     m=n//Q+1
     return m,m*dict[cs]


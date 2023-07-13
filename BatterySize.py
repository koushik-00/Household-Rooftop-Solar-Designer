def volts(n):
    if n==12:
        return "The battery you chose is 12V."
    elif n==24:
        return "The battery you chose is 24V."
    elif n==48:
        return "The battery you chose is 48V."
    else:
        return "Choose from 12V, 24V and 48V only."

def days(m):
    if m<=3:
        return ("Energy stored for {} day(s)".format(m))
    else:
        return ("The capacity is way too large to store.")
 
    

        

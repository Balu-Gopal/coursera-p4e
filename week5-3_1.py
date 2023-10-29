hrs = input("Enter Hours:")
h = float(hrs)
rte = input("Enter rate:")
r = float(rte)  
if h<=40:
   print (pay=h*r)
else :
    pay = (h*r)
    gpay = (h-40.0)*(r*0.5)
    gp = pay+gpay
    print (gp)
consume=float(input("enter the consume unit: "))
if consume<0:
    print("invalid entry")
elif consume<=50:
    print("bill amounnt is", 5.0*consume,"Rs")
elif consume<=100:
    print("bill amount is", 6.5*consume,"Rs")
elif consume<=200:
    print("bill amount is", 8.0*consume,"Rs")
else:
    print("bill amount is", 10.0*consume,"Rs")


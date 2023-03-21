unit = input("Starting unit F/C ")

if unit == "F" or "f":
    f = float(input("Value: "))
    c = (f - 32) * 5 / 9
    print(c)
elif unit == "C":
    c = float(input("Value: "))
    f =  (c * 9 / 5 ) + 32
    print(f)
else:    print("what")


while True:
    fuel = input("Fraction: ")
    try:
        numerator, denominator = fuel.split("/")
        new_numerator = int(numerator)
        new_denominator = int(denominator)

        f = new_numerator / new_denominator
        if f <= 1:
            break
    except(ValueError, ZeroDivisionError):
        pass

p = int(f *100)

if p <= 1:
    print("E")
elif p >= 99:
    print("F")
else:
    print(f"{p}%")


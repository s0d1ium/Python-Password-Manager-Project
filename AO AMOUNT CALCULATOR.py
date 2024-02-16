amount = float(input("Crafting amount > "))
Return_rate = float(input("Return rate > "))

value = amount
value2 = amount

while value > 1:
    value = value*Return_rate

    value2 += round(value)

print(value2)

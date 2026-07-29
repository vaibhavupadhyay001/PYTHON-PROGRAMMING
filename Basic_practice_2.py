price1 = float(input("Enter price of product 1: "))
price2 = float(input("Enter price of product 2: "))
price3 = float(input("Enter price of product 3: "))


total_bill = price1 + price2 + price3
average_price = total_bill / 3


print("Total Bill Amount =", total_bill)
print("Average Price =", average_price)


superhero=input("Enter the name of superhero")

print(superhero.startswith("S") or superhero.startswith("s"))
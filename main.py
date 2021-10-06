#programmer: Brian Tallay
#date: oct 6th 2021
#desc:create a cash register that can make a sale

price = float(input("Enter the price:"))
total = (float(price)*1.13)
print(f"The total with tax is ${total:,.2f}")

paid = float(input("Enter the cash paid:"))
change = (float(paid)-(total))
print(f"Your change is ${change:,.2f}")
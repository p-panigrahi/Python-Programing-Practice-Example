# write a program to calcualte profit or loss
actual_cost = float(input("Enter Actual_Cost : "))
sales_amount = float(input("Enter Sales_Amount : "))
if (actual_cost > sales_amount):
    amount = actual_cost - sales_amount
    print(f"Total loss amount {amount}")
elif (sales_amount > actual_cost):
    amount = sales_amount - actual_cost
    print(f"Total profit amount is {amount}")
else:
    print("No Profit or Loss")
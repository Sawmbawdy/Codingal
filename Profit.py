ActualCost = float(input("Please input Actual Amount: "))
SaleCose = float(input("Please Enter Sale Cost: "))

if SaleCose > ActualCost:
    profit = SaleCose - ActualCost
    print("The Profit Is", profit, "MOONEY")
else:
    print("NO PROFIT!!!!!!!!!!!!!!!!")
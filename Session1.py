# eCommerce Problem

# Model
# Container Creation Statements
# 1. Single Value Storage Containers
sellingPriceAmazon = 15000
sellingPriceFlipkart = 14800

profitsAmazon = 3800.33
profitsFlipkart = 4000.12

taxes = 18

# 2. Multi Value Storage Containers
#               0     1     2
salesAmazon = [1200, 4200, 300]
salesFlipkart = [1350, 8349, 1977]

# Printing/Reading Statements
print("sellingPriceAmazon:", sellingPriceAmazon, type(sellingPriceAmazon))
print("sellingPriceFlipkart:", sellingPriceFlipkart, type(sellingPriceFlipkart))

print()

print("profitsAmazon:", profitsAmazon, type(profitsAmazon))
print("profitsFlipkart:", profitsFlipkart, type(profitsFlipkart))

print()

print("taxes:", taxes, type(taxes))

print()

print("salesAmazon:", salesAmazon, type(salesAmazon))
print("salesFlipkart:", salesFlipkart, type(salesFlipkart))

# CONTROLLER
# Computational Statement | Maths
totalSalesAmazon = (salesAmazon[0] + salesAmazon[1] + salesAmazon[2]) * sellingPriceAmazon
totalSalesFlipkart = (salesFlipkart[0] + salesFlipkart[1] + salesFlipkart[2]) * sellingPriceFlipkart

totalProfitsAmazon = (salesAmazon[0] + salesAmazon[1] + salesAmazon[2]) * profitsAmazon
totalProfitsFlipkart = (salesFlipkart[0] + salesFlipkart[1] + salesFlipkart[2]) * profitsFlipkart


print()

print("totalSalesAmazon:", totalSalesAmazon, type(totalSalesAmazon))
print("totalSalesFlipkart:", totalSalesFlipkart, type(totalSalesFlipkart))

print()

print("totalProfitsAmazon:", totalProfitsAmazon, type(totalProfitsAmazon))
print("totalProfitsFlipkart:", totalProfitsFlipkart, type(totalProfitsFlipkart))

# MI would like to take a decision
# who so ever sold more products will be paid 1000 extra per product as incentive

if totalSalesAmazon > totalSalesFlipkart:
    print(">> Amazon made more Sales")
else:
    print(">> Flipkart made more Sales")


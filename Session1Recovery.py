"""
	MI		 X
	Amazon   15000 	[500.12]
	Flipkart 14800  [300.55]

	Day1
	Amazon		1237
	Flipkart	2241

	Day2
	Amazon		3137
	Flipkart	1241

	Day3
	Amazon		2371
	Flipkart	4122

	1. Sales by Amazon and Profits to Amazon
	2. Sales by Flipkart and Profits to Flipkart
	3. Amazon or Flipkart who Sold More
	4. How much Taxes are to be paid to Gov

"""

# Clean Code

# Storage Container Creation Statement
amazonDay1Sales = 1237
amazonDay2Sales = 3137
amazonDay3Sales = 2371

flipkartDay1Sales = 2241
flipkartDay2Sales = 1241
flipkartDay3Sales = 4122

amazonProfits = 500.12
flipkartProfits = 300.55

# Update Statement
flipkartDay2Sales = 1841

# Computation Statement
totalAmazonSales = amazonDay1Sales + amazonDay2Sales + amazonDay3Sales
totalFlipkartSales = flipkartDay1Sales + flipkartDay2Sales + flipkartDay3Sales

totalAmazonProfits = totalAmazonSales * amazonProfits
totalFlipkartProfits = totalFlipkartSales * flipkartProfits

# Read or Print Statements
print(">> totalAmazonSales:", totalAmazonSales)
print(">> totalFlipkartSales:", totalFlipkartSales)

print(">> totalAmazonProfits:", totalAmazonProfits)
print(">> totalFlipkartProfits:", totalFlipkartProfits)



if totalAmazonSales > totalFlipkartSales:
    print(">> Amazon Made More Sales:",totalAmazonSales)
else:
    print(">> Flipkart Made More Sales:",totalFlipkartSales, "by",(totalFlipkartSales-totalAmazonSales))


# Challenge : What if we have to compute for 1 month ? We will end up in writing more code!
#             Development Time will be Wasted

# Solution  : Optimize Data Storage and Computation

amazonSales = [1237, 3137, 2371]
flipkartSales = [2241, 1241, 4122]

totalAmazonSales = 0
totalFlipkartSales = 0

for i in range(0, len(amazonSales)):
    totalAmazonSales = totalAmazonSales + amazonSales[i]
    flipkartSales = totalFlipkartSales + flipkartSales[i]

totalAmazonProfits = totalAmazonSales * amazonProfits
totalFlipkartProfits = totalFlipkartSales * flipkartProfits

if totalAmazonSales > totalFlipkartSales:
    print(">> Amazon Made More Sales:",totalAmazonSales)
else:
    print(">> Flipkart Made More Sales:",totalFlipkartSales, "by",(totalFlipkartSales-totalAmazonSales))
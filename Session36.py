import pandas as pd
import matplotlib.pyplot as plt

table = pd.read_csv("BigMartSalesData.csv")
# print(table)

"""
1. Plot Total Sales Per Month for Year 2011. 
   How the total sales have increased over months in Year 2011. 
   Which month has lowest Sales?
"""
def answer1():
    print("Data for Year 2011: ")
    salesYear2011Data = table[table['Year'] == 2011]
    print(salesYear2011Data)

    print("~~~~~~~~~~")

    print("Group the Data Month Wise for Year 2011: ")
    salesYear2011DataMonthWise = salesYear2011Data.groupby('Month').sum()['Amount']
    print(salesYear2011DataMonthWise)
    print(type(salesYear2011DataMonthWise))

    print("Lowest Sales {} recorded in month {}".format(salesYear2011DataMonthWise.min(), salesYear2011DataMonthWise.idxmin()))
    print("Highest Sales {} recorded in month {}".format(salesYear2011DataMonthWise.max(), salesYear2011DataMonthWise.idxmax()))

    """
    minValue = pd.Index(salesYear2011DataMonthWise).min()
    maxValue = pd.Index(salesYear2011DataMonthWise).max()

    print(">> minIdx is:", minValue)
    print(">> maxIdx is:", maxValue)
    """

    plt.plot(salesYear2011DataMonthWise.index, salesYear2011DataMonthWise.values)
    plt.xlabel("Years")
    plt.ylabel("Sales")
    plt.title("2011 Sales Report")
    plt.show()


"""
2. Plot Total Sales Per Month for Year 2011 as Bar Chart. 
Is Bar Chart Better to visualize than Simple Plot?
"""
def answer2():
    print("Data for Year 2011: ")
    salesYear2011Data = table[table['Year'] == 2011]
    print(salesYear2011Data)

    print("~~~~~~~~~~")

    print("Group the Data Month Wise for Year 2011: ")
    salesYear2011DataMonthWise = salesYear2011Data.groupby('Month').sum()['Amount']
    print(salesYear2011DataMonthWise)
    print(type(salesYear2011DataMonthWise))

    plt.bar(salesYear2011DataMonthWise.index, salesYear2011DataMonthWise.values, color="red")
    plt.xlabel("Years")
    plt.ylabel("Sales")
    plt.title("2011 Sales Report")
    plt.show()

"""
3. Plot Pie Chart for Year 2011 Country Wise. 
Which Country contributes highest towards sales?
"""
def answer3():
    print("Data for Year 2011: ")
    salesYear2011Data = table[table['Year'] == 2011]
    print(salesYear2011Data)

    print("~~~~~~~~~~")


def main():
    answer1()
    # answer2()


if __name__ == '__main__':
    main()


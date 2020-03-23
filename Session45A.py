"""
    GUI Based Program for showing Predictions to User on Interface
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sklearn.linear_model import LinearRegression
import tkinter as tk

df = pd.read_csv("companies.csv")
print(df)

X = df[['R&DSpend', 'MarketingSpend']]
Y = df['Profit']

model = LinearRegression()
model.fit(X, Y)

print("Interceptor:", model.intercept_)
print("Coefficients:", model.coef_)

RDSpend = 144372.41
MKSpend = 383199.62

predictedProfit = model.predict([[RDSpend, MKSpend]])
print("Predicted profit for RDSpend {} and MKSpend {} is:{}".format(RDSpend, MKSpend, predictedProfit))

# GUI Development

def onClick():
    print("Button Clicked")

    global RDSpend
    RDSpend = float(entryX1.get())

    global MKSpend
    MKSpend = float(entryX1.get())

    global predictedProfit
    predictedProfit = model.predict([[RDSpend, MKSpend]])
    predictionText = ('Predicted Profit', predictedProfit[0])

    lblProfit = tk.Label(root, text=predictionText, bg='orange')
    canvas.create_window(260, 280, window=lblProfit)

# Root Window
root = tk.Tk()

canvas = tk.Canvas(root, width=500, height=300)
canvas.pack()

interceptText = ('Intercept', model.intercept_)
lblIntercept = tk.Label(root, text=interceptText, justify='center')
canvas.create_window(260, 200, window=lblIntercept)

coefText = ('Coefficients', model.coef_)
lblCoef = tk.Label(root, text=coefText, justify='center')
canvas.create_window(260, 220, window=lblCoef)


lblX1 = tk.Label(root, text="R&D Spend:")
canvas.create_window(100, 100, window=lblX1)

entryX1 = tk.Entry(root)
canvas.create_window(260, 100, window=entryX1)

lblX2 = tk.Label(root, text="Marketing Spend:")
canvas.create_window(110, 130, window=lblX2)

entryX2 = tk.Entry(root)
canvas.create_window(260, 130, window=entryX2)


btnPredict = tk.Button(root, text='PREDICT PROFITS', command=onClick, bg='orange')
canvas.create_window(260, 160, window=btnPredict)

# Plot 1st Scatter Graph - R&DSpend VS Profit
figure1 = plt.Figure(figsize=(5, 4), dpi=100)
subPlot1 = figure1.add_subplot(111)
subPlot1.scatter(df['R&DSpend'].astype(float), df['Profit'].astype(float), color='red')
scatterGraph1 = FigureCanvasTkAgg(figure1, root)
scatterGraph1.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH)
# subPlot1.legend()
subPlot1.set_xlabel("R&DSpend")
subPlot1.set_ylabel("Profit")

# Plot 2nd Scatter Graph - MarketingSpend VS Profit
figure2 = plt.Figure(figsize=(5, 4), dpi=100)
subPlot2 = figure2.add_subplot(111)
subPlot2.scatter(df['MarketingSpend'].astype(float), df['Profit'].astype(float), color='green')
scatterGraph2 = FigureCanvasTkAgg(figure2, root)
scatterGraph2.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH)
# subPlot1.legend()
subPlot2.set_xlabel("MarketingSpend")
subPlot2.set_ylabel("Profit")

root.mainloop()
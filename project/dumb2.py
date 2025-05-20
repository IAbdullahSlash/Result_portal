import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from project.dumb_data import sales_data, inventory_data, sales_year_data, inventory_month_data

plt.rcParams["axes.prop_cycle"] = plt.cycler(
    color=["#196F3D", "#FFFFFF"])

# Chart 1: Bar chart of sales data
fig1, ax1 = plt.subplots()
bars = ax1.bar(sales_data.keys(), sales_data.values())
ax1.set_title("Precentage per year")
ax1.set_xlabel("Precentage")
ax1.set_ylabel("Years")
for bar, value in zip(bars, sales_data.values()):
    height = bar.get_height()
    ax1.annotate(f'{value}%', xy=(bar.get_x() + bar.get_width() / 2, height), ha='center')

# Chart 2: Horizontal bar chart of inventory data
fig2, ax2 = plt.subplots()
ax2.barh(list(inventory_data.keys()), list(inventory_data.values()))
ax2.set_title("Inventory by Product")
ax2.set_xlabel("Inventory")
ax2.set_ylabel("Product")



# # Chart 3: Pie chart of product data
# fig3, ax3 = plt.subplots()
# ax3.pie(product_data.values(), labels=product_data.keys(), autopct='%1.1f%%')
# ax3.set_title("Product \nBreakdown")

# Chart 4: Line chart of sales by year
fig4, ax4 = plt.subplots()
ax4.plot(list(inventory_month_data.keys()), list(inventory_month_data.values()))
ax4.set_title("Sales by Year")
ax4.set_xlabel("Year")
ax4.set_ylabel("Sales")

# Chart 5: Area chart of inventory by month
fig5, ax5 = plt.subplots()
ax5.fill_between(sales_year_data.keys(), sales_year_data.values())
ax5.set_title("Inventory by Month")
ax5.set_xlabel("Month")
ax5.set_ylabel("Inventory")

# Create a window and add charts
root = tk.Tk()
root.title("Dashboard")


side_frame = tk.Frame(root, bg="#196F3D")
side_frame.pack(side="left", fill="y")

label = tk.Label(side_frame, text="Dashboard", bg="#196F3D", fg="#FFF", font=25)
label.pack(pady=50, padx=20)

charts_frame = tk.Frame(root)
charts_frame.pack()

upper_frame = tk.Frame(charts_frame)
upper_frame.pack(fill="both", expand=True)

canvas1 = FigureCanvasTkAgg(fig1, upper_frame)
canvas1.get_tk_widget().pack(side="left", fill="both", expand=True)

canvas2 = FigureCanvasTkAgg(fig2, upper_frame)
canvas2.get_tk_widget().pack(side="left", fill="both", expand=True)

# canvas3 = FigureCanvasTkAgg(fig3, upper_frame)
# canvas3.get_tk_widget().pack(side="left", fill="both", expand=True)

lower_frame = tk.Frame(charts_frame)
lower_frame.pack(fill="both", expand=True)

canvas4 = FigureCanvasTkAgg(fig4, lower_frame)
canvas4.get_tk_widget().pack(side="left", fill="both", expand=True)

canvas5 = FigureCanvasTkAgg(fig5, lower_frame)
canvas5.get_tk_widget().pack(side="left", fill="both", expand=True)

root.mainloop()

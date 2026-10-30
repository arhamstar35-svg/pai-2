
import matplotlib.pyplot as plt
import numpy as np


# ==========================================
# 1. BASIC LINE PLOT
# ==========================================

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [100, 150, 120, 200, 250]

# plot() creates a line graph
plt.plot(months, sales)

# title() gives the graph a heading
plt.title("Monthly Sales")

# xlabel() gives the x-axis a name
plt.xlabel("Months")

# ylabel() gives the y-axis a name
plt.ylabel("Sales")

# show() displays the graph
plt.show()


# ==========================================
# 2. CUSTOMIZING A LINE PLOT
# ==========================================

months = [1, 2, 3, 4, 5]
sales = [100, 150, 120, 200, 250]

# color changes the line color
# marker displays points on the line
# linestyle changes the line style
# linewidth changes line thickness
# label gives the line a name for the legend

plt.plot(months, sales, color="blue",
         marker="o", linestyle="--",
         linewidth=2, label="Sales")

plt.title("Sales Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")

# legend() displays labels of plotted lines
plt.legend()

# grid() displays grid lines
plt.grid()

plt.show()


# ==========================================
# 3. MULTIPLE LINES IN ONE GRAPH
# ==========================================

months = [1, 2, 3, 4, 5]

sales = [100, 150, 120, 200, 250]
expenses = [80, 100, 90, 130, 160]

# Multiple plot() calls on the same graph
# create multiple lines

plt.plot(months, sales, label="Sales", marker="o")
plt.plot(months, expenses, label="Expenses", marker="s")

plt.title("Sales vs Expenses")
plt.xlabel("Month")
plt.ylabel("Amount")

plt.legend()
plt.grid()

plt.show()


# ==========================================
# 4. BAR CHART
# ==========================================

students = ["Ali", "Ahmed", "Sara"]
marks = [80, 90, 70]

# bar() creates a vertical bar chart
plt.bar(students, marks, color="skyblue")

plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

# ylim() controls the y-axis range
plt.ylim(0, 100)

plt.show()


# ==========================================
# 5. HORIZONTAL BAR CHART
# ==========================================

students = ["Ali", "Ahmed", "Sara"]
marks = [80, 90, 70]

# barh() creates a horizontal bar chart
plt.barh(students, marks, color="orange")

plt.title("Student Marks")
plt.xlabel("Marks")
plt.ylabel("Students")

plt.show()


# ==========================================
# 6. HISTOGRAM
# ==========================================

marks = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90]

# hist() displays the frequency distribution
# bins determines the number of intervals

plt.hist(marks, bins=5, color="green",
         edgecolor="black")

plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")

plt.show()


# ==========================================
# 7. SCATTER PLOT
# ==========================================

hours = [1, 2, 3, 4, 5, 6]
marks = [40, 50, 55, 65, 75, 90]

# scatter() displays individual data points
# Useful for identifying relationships

plt.scatter(hours, marks, color="red")

plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")

plt.show()


# ==========================================
# 8. PIE CHART
# ==========================================

categories = ["Food", "Transport", "Education", "Other"]
expenses = [4000, 2000, 3000, 1000]

# pie() creates a circular pie chart
# labels displays category names
# autopct displays percentage values

plt.pie(expenses, labels=categories,
        autopct="%1.1f%%")

plt.title("Monthly Expenses")

plt.show()


# ==========================================
# 9. PIE CHART CUSTOMIZATION
# ==========================================

categories = ["Food", "Transport", "Education"]
expenses = [4000, 2000, 3000]

# explode separates a slice from the pie
# startangle rotates the pie chart
# shadow adds a shadow effect

plt.pie(expenses,
        labels=categories,
        autopct="%1.1f%%",
        explode=[0.1, 0, 0],
        startangle=90,
        shadow=True)

plt.title("Expense Distribution")

plt.show()


# ==========================================
# 10. BOXPLOT
# ==========================================

marks = [45, 50, 55, 60, 65, 70, 75, 80, 85, 150]

# boxplot() displays the distribution of data
# Helps identify median, quartiles and outliers

plt.boxplot(marks)

plt.title("Marks Distribution")
plt.ylabel("Marks")

plt.show()


# ==========================================
# 11. FIGURE SIZE
# ==========================================

students = ["Ali", "Ahmed", "Sara"]
marks = [80, 90, 70]

# figure() creates a figure
# figsize controls its width and height

plt.figure(figsize=(8, 5))

plt.bar(students, marks)

plt.title("Student Marks")

plt.show()


# ==========================================
# 12. AXIS LIMITS
# ==========================================

x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

plt.plot(x, y)

# xlim() controls the x-axis range
plt.xlim(0, 6)

# ylim() controls the y-axis range
plt.ylim(0, 60)

plt.show()


# ==========================================
# 13. TICKS
# ==========================================

students = ["Ali", "Ahmed", "Sara"]
marks = [80, 90, 70]

plt.bar(students, marks)

# xticks() controls x-axis tick positions/labels
plt.xticks(rotation=45)

# yticks() controls y-axis tick positions/labels
plt.yticks([0, 20, 40, 60, 80, 100])

plt.show()


# ==========================================
# 14. TEXT AND ANNOTATIONS
# ==========================================

months = [1, 2, 3, 4, 5]
sales = [100, 150, 120, 200, 250]

plt.plot(months, sales, marker="o")

# text() displays text at a specified location
plt.text(4, 200, "Highest Sales")

# annotate() adds an annotation with an arrow
plt.annotate("Maximum",
             xy=(5, 250),
             xytext=(3, 250),
             arrowprops={"arrowstyle": "->"})

plt.show()


# ==========================================
# 15. SAVE GRAPH
# ==========================================

students = ["Ali", "Ahmed", "Sara"]
marks = [80, 90, 70]

plt.bar(students, marks)

plt.title("Student Marks")

# savefig() saves the graph as an image
plt.savefig("student_marks.png")

plt.show()


# ==========================================
# 16. SUBPLOTS
# ==========================================

# subplots() creates multiple graphs
# 2 rows and 2 columns

fig, ax = plt.subplots(2, 2, figsize=(10, 8))

# First graph: Line plot
ax[0, 0].plot([1, 2, 3], [10, 20, 30])
ax[0, 0].set_title("Line Plot")

# Second graph: Bar chart
ax[0, 1].bar(["A", "B", "C"], [20, 40, 30])
ax[0, 1].set_title("Bar Chart")

# Third graph: Scatter plot
ax[1, 0].scatter([1, 2, 3], [30, 20, 40])
ax[1, 0].set_title("Scatter Plot")

# Fourth graph: Histogram
ax[1, 1].hist([10, 20, 20, 30, 40], bins=4)
ax[1, 1].set_title("Histogram")

# tight_layout() adjusts spacing between graphs
fig.tight_layout()

plt.show()


# ==========================================
# 17. OBJECT-ORIENTED MATPLOTLIB
# ==========================================

# fig represents the entire figure
# ax represents the individual plotting area

fig, ax = plt.subplots(figsize=(8, 5))

months = [1, 2, 3, 4, 5]
sales = [100, 150, 120, 200, 250]

# ax.plot() creates a line inside the plotting area
ax.plot(months, sales, marker="o", label="Sales")

# set_title() sets the graph title
ax.set_title("Monthly Sales")

# set_xlabel() sets the x-axis label
ax.set_xlabel("Months")

# set_ylabel() sets the y-axis label
ax.set_ylabel("Sales")

# legend() displays line labels
ax.legend()

# grid() displays grid lines
ax.grid()

# savefig() saves the complete figure
fig.savefig("monthly_sales.png")

plt.show()

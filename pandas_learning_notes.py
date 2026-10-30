"""
PANDAS LEARNING NOTES
=====================
A beginner-friendly reference for the Pandas functions and methods covered
in our learning sessions.

Environment used:
    pandas 3.0.6

Install:
    pip install pandas openpyxl

Run:
    python pandas_learning_notes.py

Note:
    - df, df2, and other variables below are examples.
    - File-reading examples are commented out because they need real files.
    - DataFrame.append() is not used: it was removed in modern Pandas.
      Use pd.concat() when combining DataFrames.
"""

import pandas as pd


# ============================================================
# 1. CREATING DATAFRAMES
# ============================================================

# Create a DataFrame from a dictionary of lists.
data = {
    "Name": ["Ali", "Ahmed", "Sara", "Usman", "Ayesha", "Hamza"],
    "Department": ["IT", "HR", "IT", "HR", "Sales", "Sales"],
    "Age": [22, 25, 24, 23, 26, 27],
    "Salary": [50000, 40000, 60000, 45000, 55000, 65000],
    "Marks": [80, 65, 90, 72, 88, 95]
}

df = pd.DataFrame(data)  # pd.DataFrame() creates a DataFrame.

print("\nORIGINAL DATAFRAME")
print(df)


# Create a DataFrame from a list of lists.
rows = [
    ["Ali", 80],
    ["Sara", 90],
    ["Ahmed", 75]
]

students = pd.DataFrame(rows, columns=["Name", "Marks"])
# columns= assigns column names to the list data.


# Create a DataFrame from a list of dictionaries.
records = [
    {"Name": "Ali", "Marks": 80},
    {"Name": "Sara", "Marks": 90},
    {"Name": "Ahmed", "Marks": 75}
]

results = pd.DataFrame(records)


# ============================================================
# 2. READING AND WRITING FILES
# ============================================================

# Read a CSV file and convert it into a DataFrame.
# df_csv = pd.read_csv("students.csv")

# Save a DataFrame to a CSV file.
# index=False prevents Pandas from writing row indexes as a column.
# df.to_csv("output.csv", index=False)

# Read an Excel file.
# df_excel = pd.read_excel("students.xlsx")

# Save a DataFrame to an Excel file.
# df.to_excel("output.xlsx", index=False)

# Read a tab-separated file.
# tab_df = pd.read_csv("data.txt", sep="\t")

# Convert a DataFrame into JSON records.
# orient="records" makes each row a separate dictionary/object.
# indent=4 makes the JSON easier to read.
# df.to_json("students.json", orient="records", indent=4)

# Read JSON data into a DataFrame.
# json_df = pd.read_json("students.json")


# ============================================================
# 3. INSPECTING A DATAFRAME
# ============================================================

print("\nFIRST FIVE ROWS")
print(df.head())  # head() displays the first 5 rows by default.

print("\nFIRST TWO ROWS")
print(df.head(2))  # head(2) displays the first 2 rows.

print("\nDATAFRAME SHAPE")
print(df.shape)  # shape returns (number_of_rows, number_of_columns).

print("\nNUMBER OF DIMENSIONS")
print(df.ndim)  # ndim returns the number of dimensions; DataFrame is 2D.

print("\nTOTAL NUMBER OF ELEMENTS")
print(df.size)  # size = rows multiplied by columns.

print("\nCOLUMN NAMES")
print(df.columns)  # columns returns all column labels.

print("\nDATA TYPES")
print(df.dtypes)  # dtypes shows the data type of each column.

print("\nDATAFRAME INFORMATION")
df.info()  # info() displays column names, non-null counts, and data types.

print("\nDESCRIPTIVE STATISTICS")
print(df.describe())  # describe() gives statistics for numeric columns.


# ============================================================
# 4. SELECTING COLUMNS AND ROWS
# ============================================================

# Select one column. The result is a Series.
names = df["Name"]
print(names)

# Select multiple columns. The result is a DataFrame.
selected = df[["Name", "Salary"]]
print(selected)

# loc uses row labels and column labels.
print(df.loc[0, "Name"])  # Value at row label 0 and column Name.

# Select rows using labels.
print(df.loc[0:2])  # Label slicing: includes both 0 and 2.

# Select specific rows and columns using labels.
print(df.loc[0:2, ["Name", "Salary"]])

# iloc uses integer positions.
print(df.iloc[0, 1])  # First row, second column.

# Select rows by position. The ending position is excluded.
print(df.iloc[0:3])

# Select specific rows and columns by position.
print(df.iloc[0:3, 0:2])

# at accesses one value using a row label and column label.
print(df.at[1, "Marks"])

# iat accesses one value using integer positions.
print(df.iat[1, 4])


# ============================================================
# 5. FILTERING DATA
# ============================================================

# Select rows where Marks are greater than 80.
high_marks = df[df["Marks"] > 80]
print(high_marks)

# Select rows where Department is IT.
it_students = df[df["Department"] == "IT"]
print(it_students)

# AND (&): both conditions must be true.
condition_and = df[(df["Marks"] > 70) & (df["Age"] < 25)]
print(condition_and)

# OR (|): at least one condition must be true.
condition_or = df[(df["Department"] == "IT") | (df["Department"] == "HR")]
print(condition_or)

# isin() checks whether values belong to a given list.
selected_departments = df[df["Department"].isin(["IT", "Sales"])]
print(selected_departments)


# ============================================================
# 6. ADDING, CHANGING, AND REMOVING DATA
# ============================================================

# Add a new column by assigning values.
df_work = df.copy()
df_work["Bonus"] = [5000, 3000, 6000, 3500, 5500, 6500]

# insert() adds a new column at a specific position.
# Position 2 means the new column will be the third column.
df_insert = df.copy()
priority = ["High", "Medium", "High", "Low", "Medium", "High"]
df_insert.insert(2, "Priority", priority)

# Change a value using loc.
df_change = df.copy()
df_change.loc[0, "Marks"] = 85

# pop() removes a column and returns that removed column.
df_pop = df.copy()
removed_marks = df_pop.pop("Marks")
print(removed_marks)
print(df_pop)

# drop() removes a column or row.
df_drop = df.drop("Age", axis=1)  # axis=1 means columns.
# df.drop(0, axis=0) would remove the row with index label 0.


# ============================================================
# 7. MISSING DATA
# ============================================================

missing_data = {
    "Name": ["Ali", "Sara", "Ahmed", "Usman"],
    "Marks": [80, None, 75, None],
    "Age": [20, 21, None, 23]
}
missing_df = pd.DataFrame(missing_data)

# isnull() returns True where a value is missing.
print(missing_df.isnull())

# isnull().sum() counts missing values in each column.
print(missing_df.isnull().sum())

# fillna() replaces missing values.
filled_df = missing_df.copy()
filled_df["Marks"] = filled_df["Marks"].fillna(0)

# dropna() removes rows containing missing values.
clean_df = missing_df.dropna()


# ============================================================
# 8. APPLYING A MAPPING
# ============================================================

# map() applies a mapping or function to each value in a Series.
grade_map = {
    "Ali": "A",
    "Ahmed": "B",
    "Sara": "A",
    "Usman": "B",
    "Ayesha": "A",
    "Hamza": "A"
}

mapped_df = df.copy()
mapped_df["Grade"] = mapped_df["Name"].map(grade_map)


# ============================================================
# 9. MATHEMATICAL AND STATISTICAL METHODS
# ============================================================

print("\nAVERAGE MARKS")
print(df["Marks"].mean())  # mean() calculates the average.

print("\nMEDIAN MARKS")
print(df["Marks"].median())  # median() returns the middle value.

print("\nMODE OF MARKS")
print(df["Marks"].mode())  # mode() returns the most frequent value(s).

print("\nMAXIMUM MARKS")
print(df["Marks"].max())  # max() returns the largest value.

print("\nMINIMUM MARKS")
print(df["Marks"].min())  # min() returns the smallest value.

print("\nTOTAL SALARY")
print(df["Salary"].sum())  # sum() adds all values.

print("\nCOUNT OF NON-MISSING MARKS")
print(df["Marks"].count())  # count() counts non-missing values.

print("\nNUMBER OF UNIQUE DEPARTMENTS")
print(df["Department"].nunique())  # nunique() counts distinct values.

print("\nFREQUENCY OF EACH DEPARTMENT")
print(df["Department"].value_counts())  # value_counts() counts each category.

# idxmax() returns the index label where the maximum value occurs.
highest_marks_index = df["Marks"].idxmax()
print("\nINDEX OF HIGHEST MARKS")
print(highest_marks_index)

# Use the returned index to retrieve the complete row.
print(df.loc[highest_marks_index])


# ============================================================
# 10. SORTING
# ============================================================

# sort_values() sorts rows according to a column.
sorted_marks = df.sort_values("Marks")
print(sorted_marks)

# ascending=False sorts from highest to lowest.
highest_first = df.sort_values("Marks", ascending=False)
print(highest_first)

# Sort using more than one column.
multi_sort = df.sort_values(
    ["Department", "Salary"],
    ascending=[True, False]
)
print(multi_sort)


# ============================================================
# 11. GROUPBY
# ============================================================

# groupby() divides rows into groups based on the selected column.
# It creates a GroupBy object; an aggregation is then applied.
grouped = df.groupby("Department")

# Sum of Salary in each department.
print(grouped["Salary"].sum())

# Average salary in each department.
print(grouped["Salary"].mean())

# Maximum and minimum salary in each department.
print(grouped["Salary"].max())
print(grouped["Salary"].min())

# Count non-missing Salary values in each department.
print(grouped["Salary"].count())

# size() counts all rows in each group.
print(grouped.size())

# Group by multiple columns.
# Each unique Department + Age combination becomes a separate group.
multi_group = df.groupby(["Department", "Age"])
print(multi_group["Salary"].sum())

# Select more than one column from a GroupBy object.
print(grouped[["Salary", "Marks"]].mean())

# agg() applies one or more aggregation functions.
print(grouped["Salary"].agg(["mean", "max", "min"]))

# Apply different functions to different columns.
print(grouped.agg({
    "Salary": ["mean", "max"],
    "Age": ["min", "max"]
}))

# Perform separate calculations without agg().
print(grouped["Salary"].sum())
print(grouped["Marks"].mean())

# transform() returns a result with the same number of rows as the original.
# Here, each employee receives the average salary of their department.
df_transform = df.copy()
df_transform["Department Average"] = (
    df_transform.groupby("Department")["Salary"].transform("mean")
)
print(df_transform)

# filter() keeps or removes entire groups based on a condition.
# Keep departments that have more than one employee.
filtered_groups = grouped.filter(lambda group: len(group) > 1)
print(filtered_groups)

# get_group() retrieves one particular group.
print(grouped.get_group("IT"))

# apply() lets us perform a custom operation on each group.
# This calculates the salary range (maximum - minimum) in each department.
salary_range = grouped["Salary"].apply(
    lambda values: values.max() - values.min()
)
print(salary_range)

# reset_index() turns grouped index levels back into ordinary columns.
group_result = multi_group["Salary"].sum().reset_index()
print(group_result)


# ============================================================
# 12. COMBINING DATAFRAMES
# ============================================================

df2 = pd.DataFrame({
    "Name": ["Bilal", "Hina"],
    "Department": ["IT", "HR"],
    "Age": [28, 22],
    "Salary": [70000, 42000],
    "Marks": [78, 83]
})

# concat() combines DataFrames vertically (one below another).
vertical_concat = pd.concat([df, df2], axis=0, ignore_index=True)
print(vertical_concat)

# concat() combines DataFrames horizontally (side by side).
horizontal_concat = pd.concat(
    [df[["Name", "Marks"]], df2[["Name", "Marks"]]],
    axis=1
)
print(horizontal_concat)

# merge() combines DataFrames using a common column.
# on="Name" means match rows where the Name values are the same.
left_data = pd.DataFrame({
    "Name": ["Ali", "Sara", "Ahmed"],
    "Marks": [80, 90, 75]
})

right_data = pd.DataFrame({
    "Name": ["Ali", "Sara", "Ahmed"],
    "Age": [20, 21, 22]
})

merged = pd.merge(left_data, right_data, on="Name")
print(merged)

# When both DataFrames have a column with the same name (other than the
# merge key), suffixes distinguish the two versions.
left_data2 = pd.DataFrame({
    "Name": ["Ali", "Sara"],
    "Age": [20, 21]
})

right_data2 = pd.DataFrame({
    "Name": ["Ali", "Sara"],
    "Age": [22, 23]
})

merged_suffixes = pd.merge(
    left_data2,
    right_data2,
    on="Name",
    suffixes=("_x", "_y")
)
print(merged_suffixes)


# ============================================================
# 13. QUICK REFERENCE
# ============================================================

"""
CREATE:
    pd.DataFrame()

READ / WRITE:
    pd.read_csv()       df.to_csv()
    pd.read_excel()     df.to_excel()
    pd.read_json()      df.to_json()

INSPECT:
    df.head()
    df.shape
    df.ndim
    df.size
    df.columns
    df.dtypes
    df.info()
    df.describe()

SELECT:
    df["Column"]
    df[["Column1", "Column2"]]
    df.loc[]
    df.iloc[]
    df.at[]
    df.iat[]

FILTER:
    df[condition]
    df["Column"].isin([...])

EDIT:
    df.insert()
    df.pop()
    df.drop()
    df.copy()

MISSING DATA:
    df.isnull()
    df.isnull().sum()
    df.fillna()
    df.dropna()

CALCULATE:
    .sum()
    .mean()
    .median()
    .mode()
    .max()
    .min()
    .count()
    .nunique()
    .value_counts()
    .idxmax()

TRANSFORM / SORT:
    .map()
    .sort_values()

GROUP:
    .groupby()
    .agg()
    .transform()
    .filter()
    .get_group()
    .apply()
    .size()
    .reset_index()

COMBINE:
    pd.concat()
    pd.merge()
"""

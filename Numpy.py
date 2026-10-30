
import numpy as np

# ============================================================
# 1. CREATING NUMPY ARRAYS
# ============================================================

arr = np.array([10, 20, 30, 40, 50])
print("1. Array:")
print(arr)

# Creating a 2D array
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])

print("2D Array:")
print(arr2)

# Creating arrays containing zeros and ones
print(np.zeros((2, 3)))  # 2 rows and 3 columns of zeros
print(np.ones((2, 3)))   # 2 rows and 3 columns of ones

# Creating a sequence of numbers
print(np.arange(1, 11, 2))  # 1, 3, 5, 7, 9

# Generating equally spaced values
print(np.linspace(0, 10, 5))


# ============================================================
# 2. ARRAY ATTRIBUTES
# ============================================================

arr = np.array([[10, 20, 30],
                [40, 50, 60]])

print("Dimensions:", arr.ndim)  # Number of dimensions
print("Shape:", arr.shape)      # Number of rows and columns
print("Size:", arr.size)        # Total number of elements
print("Data type:", arr.dtype)  # Type of elements


# ============================================================
# 3. RESHAPE
# ============================================================

arr = np.arange(1, 13)

# Convert 12 elements into 3 rows and 4 columns
new_arr = arr.reshape(3, 4)

print("Reshaped Array:")
print(new_arr)

# Convert the same 12 elements into 2 rows and 6 columns
print(arr.reshape(2, 6))

# The total number of elements must remain the same.


# ============================================================
# 4. TRANSPOSE
# ============================================================

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

# Convert rows into columns and columns into rows
print("Transpose:")
print(arr.T)

# Another way to transpose
print(np.transpose(arr))


# ============================================================
# 5. STACKING ARRAYS
# ============================================================

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Join arrays end-to-end
print("Concatenate:")
print(np.concatenate((a, b)))

# Stack arrays vertically as rows
print("Vertical Stack:")
print(np.vstack((a, b)))

# Join arrays horizontally
print("Horizontal Stack:")
print(np.hstack((a, b)))

# Stack arrays along a new axis
print("Stack:")
print(np.stack((a, b)))

# The arrays must have compatible shapes for stacking.


# ============================================================
# 6. SPLITTING ARRAYS
# ============================================================

arr = np.array([10, 20, 30, 40, 50, 60])

# Split into 3 equal parts
print("Split:")
print(np.split(arr, 3))

# Split into 2 equal parts
print(np.split(arr, 2))

# Splitting a 2D array
arr2 = np.array([[1, 2, 3, 4],
                 [5, 6, 7, 8]])

# Split columns into 2 parts
print("Horizontal Split:")
print(np.hsplit(arr2, 2))

# Split rows into 2 parts
print("Vertical Split:")
print(np.vsplit(arr2, 2))


# ============================================================
# 7. AXIS
# ============================================================

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

# Sum of every element
print("Total Sum:", np.sum(arr))

# axis=0 calculates down the rows, giving column results
print("Sum along axis 0:", np.sum(arr, axis=0))

# axis=1 calculates across columns, giving row results
print("Sum along axis 1:", np.sum(arr, axis=1))

# Average of each column
print("Column Average:", np.mean(arr, axis=0))

# Average of each row
print("Row Average:", np.mean(arr, axis=1))


# ============================================================
# 8. BROADCASTING
# ============================================================

arr = np.array([10, 20, 30])

# Add 5 to every element
print(arr + 5)

# Multiply every element by 2
print(arr * 2)

arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])

# The 1D array is added to each row
print(arr2 + np.array([10, 20, 30]))

# Broadcasting allows compatible shapes to work together
# without manually repeating the smaller array.


# ============================================================
# 9. UFUNCS (UNIVERSAL FUNCTIONS)
# ============================================================

arr = np.array([4, 9, 16, 25])
b = np.array([1, 2, 3, 4])

# Mathematical operations on corresponding elements
print("Addition:", np.add(arr, b))
print("Subtraction:", np.subtract(arr, b))
print("Multiplication:", np.multiply(arr, b))
print("Division:", np.divide(arr, b))

# Mathematical functions
print("Square Root:", np.sqrt(arr))
print("Square:", np.square(b))
print("Absolute Values:", np.abs(np.array([-5, -2, 3])))

# Find the larger element at each position
print("Maximum Values:", np.maximum(arr, b))

# Find the smaller element at each position
print("Minimum Values:", np.minimum(arr, b))


# ============================================================
# 10. BOOLEAN INDEXING
# ============================================================

marks = np.array([45, 78, 90, 32, 66, 85])

# Check which values are greater than 60
print(marks > 60)

# Select only values greater than 60
print(marks[marks > 60])

# Select values less than 50
print(marks[marks < 50])

# Select values greater than or equal to 70
print(marks[marks >= 70])

# Multiple conditions: values greater than 50 and less than 90
print(marks[(marks > 50) & (marks < 90)])

# Use | for OR
print(marks[(marks < 40) | (marks > 80)])


# ============================================================
# 11. WHERE
# ============================================================

marks = np.array([45, 78, 90, 32, 66])

# Return indexes where the condition is True
print("Indexes:", np.where(marks > 60))

# Return Pass or Fail according to the condition
print(np.where(marks >= 50, "Pass", "Fail"))

# Replace values below 50 with zero in a new result
print(np.where(marks < 50, 0, marks))

# Syntax:
# np.where(condition, value_if_true, value_if_false)


# ============================================================
# 12. SORTING
# ============================================================

arr = np.array([40, 10, 30, 20, 50])

# Sort values in ascending order
print("Sorted:", np.sort(arr))

# Sort values in descending order
print("Descending:", np.sort(arr)[::-1])

# Sort each row separately
arr2 = np.array([[3, 1, 2],
                 [6, 4, 5]])

print("Sorted Rows:")
print(np.sort(arr2, axis=1))

# Sort each column separately
print("Sorted Columns:")
print(np.sort(arr2, axis=0))


# ============================================================
# 13. ARGSORT, ARGMAX, ARGMIN
# ============================================================

arr = np.array([40, 10, 30, 20])

# Return the indexes that would sort the array
print("Argsort:", np.argsort(arr))

# Return the index of the largest value
print("Argmax:", np.argmax(arr))

# Return the index of the smallest value
print("Argmin:", np.argmin(arr))

# Return the largest value itself
print("Maximum:", np.max(arr))

# Return the smallest value itself
print("Minimum:", np.min(arr))

# For a 2D array, find the index of the largest value
# along each column or row
arr2 = np.array([[10, 50, 30],
                 [40, 20, 60]])

print("Argmax along axis 0:", np.argmax(arr2, axis=0))
print("Argmax along axis 1:", np.argmax(arr2, axis=1))


# ============================================================
# 14. UNIQUE
# ============================================================

arr = np.array([2, 3, 2, 5, 3, 3, 1])

# Return distinct values only
print("Unique:", np.unique(arr))

# Return distinct values and their occurrence counts
values, counts = np.unique(arr, return_counts=True)

print("Unique Values:", values)
print("Counts:", counts)


# ============================================================
# 15. STATISTICAL FUNCTIONS
# ============================================================

marks = np.array([70, 80, 90, 60, 100])

print("Sum:", np.sum(marks))
print("Mean:", np.mean(marks))
print("Median:", np.median(marks))
print("Standard Deviation:", np.std(marks))
print("Variance:", np.var(marks))
print("Maximum:", np.max(marks))
print("Minimum:", np.min(marks))


# ============================================================
# 16. NaN VALUES AND NaN STATISTICS
# ============================================================

arr = np.array([10.0, 20.0, np.nan, 40.0, 50.0])

# NaN means Not a Number
print("Array:", arr)

# Normal mean returns NaN if the array contains NaN
print("Normal Mean:", np.mean(arr))

# These functions ignore NaN values
print("NaN Mean:", np.nanmean(arr))
print("NaN Sum:", np.nansum(arr))
print("NaN Maximum:", np.nanmax(arr))
print("NaN Minimum:", np.nanmin(arr))
print("NaN Standard Deviation:", np.nanstd(arr))


# ============================================================
# 17. DOT PRODUCT
# ============================================================

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Multiply corresponding values and add the results
# 1*4 + 2*5 + 3*6 = 32
print("Dot Product:", np.dot(a, b))

# Matrix multiplication
matrix_a = np.array([[1, 2],
                     [3, 4]])

matrix_b = np.array([[5, 6],
                     [7, 8]])

print("Matrix Multiplication:")
print(np.dot(matrix_a, matrix_b))


# ============================================================
# 18. RANDOM NUMBERS
# ============================================================

# A seed makes the random sequence reproducible
rng = np.random.default_rng(42)

# Generate 5 random integers from 1 to 10 inclusive
print("Random Integers:", rng.integers(1, 11, size=5))

# Generate 4 random decimal values between 0 and 1
print("Random Decimals:", rng.random(4))

# Generate random values from a normal distribution
# loc=0 is the mean; scale=1 is the standard deviation
print("Normal Distribution:", rng.normal(0, 1, size=5))

# Generate a 3x4 array of integers from 10 to 100
print("Random Matrix:")
print(rng.integers(10, 101, size=(3, 4)))


# ============================================================
# 19. FEATURE STANDARDIZATION
# ============================================================

features = np.array([10.0, 20.0, 30.0, 40.0, 50.0])

# Calculate the mean
mean_value = np.mean(features)

# Calculate the standard deviation
std_value = np.std(features)

# Subtract the mean and divide by the standard deviation
standardized = (features - mean_value) / std_value

print("Original Features:", features)
print("Mean:", mean_value)
print("Standard Deviation:", std_value)
print("Standardized Features:", standardized)

# Standardized data has mean approximately 0
# and standard deviation approximately 1.


# ============================================================
# 20. GRAYSCALE IMAGE MASKING
# ============================================================

# Each number represents a grayscale pixel intensity
# 0 = black and 255 = white
pixels = np.array([[20, 80, 150],
                   [200, 100, 30],
                   [90, 220, 170]])

# Create a Boolean mask for pixels above 100
mask = pixels > 100

print("Original Pixels:")
print(pixels)

print("Boolean Mask:")
print(mask)

# Select pixels greater than 100
print("Selected Pixels:", pixels[mask])

# Change pixels greater than 100 to 255
pixels[pixels > 100] = 255

print("Modified Pixels:")
print(pixels)


# ============================================================
# 21. SENSOR DATA STATISTICS
# ============================================================

# Generate a 4x3 array of sensor readings
rng = np.random.default_rng(7)
sensor_data = rng.integers(10, 101, size=(4, 3))

print("Sensor Data:")
print(sensor_data)

# Average of each column
print("Average of Each Column:", np.mean(sensor_data, axis=0))

# Average of each row
print("Average of Each Row:", np.mean(sensor_data, axis=1))

# Overall maximum and minimum
print("Maximum Reading:", np.max(sensor_data))
print("Minimum Reading:", np.min(sensor_data))

# Overall average
print("Overall Average:", np.mean(sensor_data))


# ============================================================
# 22. 10x5 MARKS ARRAY WITHOUT LOOPS
# ============================================================

# Generate marks for 10 students in 5 subjects
rng = np.random.default_rng(42)
marks = rng.integers(10, 101, size=(10, 5))

print("Marks of 10 Students:")
print(marks)

# Average marks of each student (across subjects)
print("Student Averages:", np.mean(marks, axis=1))

# Average marks of each subject (across students)
print("Subject Averages:", np.mean(marks, axis=0))

# Highest mark in each subject
print("Highest Mark Per Subject:", np.max(marks, axis=0))

# Lowest mark in each subject
print("Lowest Mark Per Subject:", np.min(marks, axis=0))

# Count marks greater than or equal to 50 for each student
print("Passing Subjects Per Student:", np.sum(marks >= 50, axis=1))

# Select all individual marks greater than 80
print("Marks Above 80:", marks[marks > 80])

# Find the highest mark in the entire array
print("Highest Overall Mark:", np.max(marks))


# ============================================================
# 23. 8x8 RANDOM ARRAY FROM 10 TO 100
# ============================================================

# Seed 42 ensures the same array is generated every run
rng = np.random.default_rng(42)

arr = rng.integers(10, 101, size=(8, 8))

print("8x8 Random Array:")
print(arr)

# Total number of elements
print("Size:", arr.size)

# Shape of the array
print("Shape:", arr.shape)

# Sum of each row
print("Row Sums:", np.sum(arr, axis=1))

# Sum of each column
print("Column Sums:", np.sum(arr, axis=0))

# Mean of the entire array
print("Overall Mean:", np.mean(arr))

# Values greater than 75
print("Values Greater Than 75:", arr[arr > 75])

# Replace values below 30 with zero
arr[arr < 30] = 0

print("After Replacing Values Below 30:")
print(arr)


# ============================================================
# 24. MATRIX OPERATIONS
# ============================================================

a = np.array([[1, 2],
              [3, 4]])

b = np.array([[5, 6],
              [7, 8]])

# Element-wise addition
print("Matrix Addition:")
print(a + b)

# Element-wise multiplication
print("Element-wise Multiplication:")
print(a * b)

# Matrix multiplication
print("Matrix Product:")
print(np.dot(a, b))

# Transpose
print("Transpose:")
print(a.T)

# Reshape
print("Reshaped Matrix:")
print(a.reshape(4, 1))

# Sum of all matrix elements
print("Matrix Sum:", np.sum(a))

# Sum of each row and column
print("Row Sums:", np.sum(a, axis=1))
print("Column Sums:", np.sum(a, axis=0))


# ============================================================
# END OF NUMPY PRACTICE FILE
# ============================================================

print("All NumPy topics completed!")

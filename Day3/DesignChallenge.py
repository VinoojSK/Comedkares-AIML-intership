import numpy as np
import pandas as pd

# Student names
names = ["Arun", "Bala", "Charan", "Deepa", "Esha"]

# Generate random marks between 60 and 100
python_marks = np.random.randint(60, 101, 5)
ai_marks = np.random.randint(60, 101, 5)
ml_marks = np.random.randint(60, 101, 5)

# Create DataFrame
df = pd.DataFrame({
    "Name": names,
    "Python": python_marks,
    "AI": ai_marks,
    "ML": ml_marks
})

# Calculate average
df["Average"] = (df["Python"] + df["AI"] + df["ML"]) / 3

# Add Result column
df["Result"] = np.where(df["Average"] >= 75, "Pass", "Fail")

# Display DataFrame
print("Student Marks")
print(df)

# Find the topper
topper = df.loc[df["Average"].idxmax()]

print("\nTopper:")
print("Name :", topper["Name"])
print("Average :", round(topper["Average"], 2))

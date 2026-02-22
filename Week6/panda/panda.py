import pandas as pd

data = {
    'Name': ["Alice", "Bob", "Charlie"],
    'Age': [25,30,35],
    'Score': [85,90,95]
}

# Data frame

df = pd.DataFrame(data)

print(f"Average Age:, {df['Age'].mean()}")
print(f"Max Score, {df['Score'].max()}")

# Filetering 

print(f"\n Students with score > 85: ")
print(f"{df[df["Score"] > 85]}")

# Quick Visualization

df.plot(x="Name", y = "Score", kind = 'bar', title = "Scores of students")
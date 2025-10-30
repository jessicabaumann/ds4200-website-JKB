import pandas as pd

# Load dataset
df = pd.read_csv("/Users/jessicabaumann/Desktop/ds4200/Homeworks/Homework 3/socialMedia.csv")

# Group by Platform and PostType, compute average Likes
avg_df = df.groupby(["Platform", "PostType"], as_index=False)["Likes"].mean()

# Round to 2 decimals and rename
avg_df["Likes"] = avg_df["Likes"].round(2)
avg_df = avg_df.rename(columns={"Likes": "AvgLikes"})

# Save summarized dataset
avg_df.to_csv("/Users/jessicabaumann/Desktop/ds4200/Homeworks/Homework 3/socialMediaAvg.csv", index=False)

print(avg_df.head())
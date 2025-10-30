import pandas as pd
# Load dataset
df = pd.read_csv("/Users/jessicabaumann/Desktop/ds4200/Homeworks/Homework 3/socialMedia.csv")

# group by date and compute average likes
time_df = df.groupby("Date", as_index=False)["Likes"].mean()

# Round to 2 decimals and rename
time_df["Likes"] = time_df["Likes"].round(2)
time_df = time_df.rename(columns={"Likes": "AvgLikes"})

# Save summarized dataset
time_df.to_csv("/Users/jessicabaumann/Desktop/ds4200/Homeworks/Homework 3/socialMediaTime.csv", index=False)

print(time_df.head())

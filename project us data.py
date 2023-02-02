# %%
# Dependencies
import pandas as pd
import scipy.stats as st
import numpy as np
import json
import matplotlib.pyplot as plt

# %%
# Store filepath in a variable
us_data_path= "archive/USvideos.csv"

# %%
# Read the datafile with the pandas library
us_data_df = pd.read_csv(us_data_path)

# %%
# Looking at the data
us_data_df.info()

# %%
# Looking at the data
us_data_df.describe()

# %%
## Obtaining the name of the category_id from the json file ###

# Getting the information out of the json file so we can give category_id a name
assignable_list =[]
id_list = []
title_list = []

with open ("US_category_id.json") as f:
    data = json.load (f)

for item in data["items"]:
    assignable_list.append(item["snippet"]["assignable"])
    id_list.append(item["id"])
    title_list.append(item["snippet"]["title"])
 
# Save to a new dataframe 
title_id_df=pd.DataFrame({"category_name": title_list, "category_id":id_list, "Assignable":assignable_list})

# Changing the data type of category_id to an integer so it's consistent with the file we will merge it with next
title_id_df = title_id_df.astype({"category_id" : int}, errors='raise')




# %%
# merging Title_Id_df to us_data_df to bring through the category_name
us_data_df = pd.merge(us_data_df, title_id_df[['category_id', 'category_name']], how='left', on='category_id')
us_data_df.head()


# %%
## ## 'trending_date' - chaninging the date format and pulling out key apsects needed for analysis ##

# Chaning the fromat of 'trending_date' from object to datetime
us_data_df['trending_date_formatted'] = pd.to_datetime(us_data_df['trending_date'], format='%y.%d.%m')

# Getting the day of the week the video trended and assigning it to a column
us_data_df["trending_day"] = us_data_df['trending_date_formatted'].dt.day_name()

# Getting the month the video trended and assigning it to a column
us_data_df["trending_month"] = us_data_df['trending_date_formatted'].dt.month_name()

# Getting the year the video trended and assigning it to a column
us_data_df["trending_year"] = us_data_df['trending_date_formatted'].dt.year

# Changing the order to day/month/year
us_data_df['trending_date_formatted_order'] = us_data_df['trending_date_formatted'].dt.strftime('%d/%m/%Y')

# %%
## 'publish_date' - changing date formats and pulling out key aspects required for analysis ##

# Changing 'publish_time' to datetime format
us_data_df['publish_time_formatted'] = pd.to_datetime(us_data_df["publish_time"])

# Getting the day of the week the video was published and assigning it to a column
us_data_df["publish_day"] = us_data_df['publish_time_formatted'].dt.day_name()

# Getting the month the video was published and assigning it to a column
us_data_df["publish_month"] = us_data_df['publish_time_formatted'].dt.month_name()

# Getting the year the video was published and assigning it to a column
us_data_df["publish_year"] = us_data_df['publish_time_formatted'].dt.year

# Checking that the above columns have been added to the dataframe
us_data_df.head()

# %%
# Ensuring the formatted dates dtype have changed
us_data_df.info()

# %%
# Counting the number of tags for each video and adding it to a new column
tag_count = []
tag = us_data_df['tags']
for word in tag:
    tag_split = word.split('|') 
    number_tags = len(tag_split)
    tag_count.append(number_tags)

us_data_df['tag_count'] = tag_count
us_data_df.head()

# %%
# Checking whether any video has no tag attached to it
no_tag = us_data_df.loc[us_data_df['tag_count'] == 0, :]
no_tag

# %%
# Filtering out those with a category_id = 43, as that category is not assignable
cleaned_us_data_df = us_data_df.loc[us_data_df['category_id'] != 43, :]

# Checking category_id = 43 has been filtered out
cleaned_us_data_df["category_id"].value_counts()

# %%
cleaned_us_data_df.info()

# %%
# Saving the cleaned file to a csv
cleaned_us_data_df.to_csv("output/cleaned_us_data.csv", index=False)

# %%
# read in csv file
cleaned_us_data_df = pd.read_csv('output/cleaned_us_data.csv')
# perform value counts on category name
category_counts = cleaned_us_data_df["category_name"].value_counts().sort_values()
# Plotting it
counts = category_counts.values
x_axis = category_counts.index.values
plt.figure(figsize=(9.5,7))
plt.barh(x_axis, counts, color='blue', alpha=1, align = "center")
plt.xticks(rotation=0)
plt.ylabel("YouTube category")
plt.xlabel("Number of trending videos")
plt.title("Number of trending videos by category")
plt.xlim(0, 10200);



# %%
unique_video_df =pd.DataFrame(category_counts)
unique_video_df


# %%
# Changing trending_date to date format it can be sorted by date
unique_video2 = pd.to_datetime(cleaned_us_data_df['trending_date'], format='%y.%d.%m')
# Sorting the dataframe by trending_date in ascending order
unique_video2 = cleaned_us_data_df.sort_values(by='trending_date', ascending=True)
# Taking the last row for each video_id
unique_video2 = cleaned_us_data_df.groupby('video_id').last()
unique_video2.reset_index(inplace = True)
unique_video2.info()

# %%
# perform value counts on category name
category_counts = unique_video2["category_name"].value_counts().sort_values()
counts = category_counts.values
x_axis = category_counts.index.values
plt.figure(figsize=(9.5,7))
plt.barh(x_axis, counts, color='red', alpha=1, align = "center")
plt.xticks(rotation=0)
plt.ylabel("YouTube category")
plt.xlabel("Number of trending videos")
plt.title("Number of trending videos by category")
plt.xlim(0, 1750);


# %%




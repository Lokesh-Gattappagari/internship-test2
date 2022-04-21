
import pandas as pd
grocery = pd.read_csv("/Users/nani/internship-test2/input/question-1/main.csv")
# /Users/nani/internship-test2/input/question-1/main.csv
# grocery.head()
# grocery.groupby('product_description')['price'].mean()
grocery["price_new"] = grocery['price'].fillna(
   grocery.groupby('product_description')['price'].transform("mean")
)
# print(grocery[grocery["price"].isna()].head())
grocery = grocery[grocery["price"].isna()]
print(grocery.head())
grocery.to_csv('main.csv')
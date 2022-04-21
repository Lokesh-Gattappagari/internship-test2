import pandas as pd
grocery = pd.read_csv("/Users/nani/internship-test2/input/question-2/main.csv")
# grocery.head()
grocery["sales_amount"]= grocery ["sales_quantity"].where( 
    grocery["unit"] != "pcs",
    grocery["product_description"].str.split("-", expand=True) [1].astype("float") *\
    grocery["sales_quantity"]
                                                                         )
grocery.to_csv('main.csv')
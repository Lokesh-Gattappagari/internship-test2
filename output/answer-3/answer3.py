import pandas as pd

csvData = pd.read_csv("/Users/nani/internship-test2/input/question-3/main.csv")
csvData.sort_values(["Red Cards"],
axis=0,
ascending=[False],
inplace=True)
csvData.sort_values(["Yellow Cards"],
axis=0,
ascending=[False],
inplace=True)
csvData.to_csv('main.csv')
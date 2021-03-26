import pandas
jobs = pandas.read_csv("DataAnalyst.csv")
print(jobs.head())
print(jobs.shape) # print(jobs.shape[0]) - pise jen radky 
print(jobs.iloc[9])
print(jobs.iloc[11:20,1:7]) # print(jobs.iloc[11:20,6]) - vypise jen lokaci

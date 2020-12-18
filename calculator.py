from typing import Union

import pandas as pd
import tkinter
from tkinter import *
from tkinter import messagebox
# import ttk
from datetime import *
import os

os.system("cd attendance & cd attendance & scrapy crawl spidyy -o attendance/final.csv")


data = pd.read_csv(r"C:\Users\Administrator\PycharmProjects\Sarthak_project\attendance\attendance\final.csv", parse_dates= [1])

# sorting data frame by Team and then By names
data.sort_values(["Subject", "Date"], axis=0,
                 ascending=True, inplace=True)
p = 0
a = 0
total = 0
attpercent = {}
temp = ""
#yyyy-dd-mm
data = data.infer_objects()
data = data.drop_duplicates()
#date = datetime(2020, 7, 25)

#data['Date'] = pd.to_datetime(data["Date"].dt.strftime('%Y-%m-%d'))
#data = data.loc[data['Date'] > date.strftime('%Y-%d-%m')]
data = data.groupby(['Subject', 'Attend']).size().reset_index() \
    .set_index(['Subject','Attend']) \
    .unstack(1).fillna(0).astype(int)
data.columns = data.columns.droplevel(0)
data['Attendance'] = data['Present'] * 100 / ( data['Present'] + data['Absent'])

# root = Tk()
# w = Label(root, text=data)
# w.pack()
# root.mainloop()
# x = 1
# for idx in data.iterrows():
#     if(x != 1):
#         print(data[idx])
#     x = x + 1

print(data)





    # print(data)

# 01-05-2020

#     if (temp == ""):
#         temp = row["Subject"]
#         if row["Attend"] == "Present":
#             p = p + 1
#         else:
#             a = a + 1
#     else:
#         if (temp == row["Subject"]):
#             if row["Attend"] == "Present":
#                 p = p + 1
#             else:
#                 a = a + 1
#         else:
#             total = a + p
#             attpercent[temp] = (p * 100) / total
#             a = 0
#             p = 0
#             temp = row["Subject"]
#             if row["Attend"] == "Present":
#                 p = p + 1
#             else:
#                 a = a + 1
#
# print(attpercent)
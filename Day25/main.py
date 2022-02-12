
# with open("Day25\weather_data.csv", 'r') as weather_data:
#     data = weather_data.readlines()
#     for row in data:
#         row.strip()
#     # data.append("Monday,20,Cloudy")
#         print(data)

# Way-2


# import csv
# with open("Day25\weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     salaries = []
#     for row in data:

#         salaries.append(row[1])
#     print(salaries[1:])


# Way 3 and most easy ( By using Pandas)

import pandas as pd

# file = pd.read_csv("./tt.csv")
df = pd.read_csv("./india-districts-census-2011.csv")

# Excel_writer_object = pd.ExcelWriter("W_excel.xlsx")
# df.to_excel(Excel_writer_object, index=False)
# Excel_writer_object.save()
# Excel_writer_object.close()

# df.to_excel("weather_Excel.xlsx", sheet_name="Testing", index=False)
# print(type(df))
# print(df[df.yoe == df.yoe.max()])

# max_yoe = df[df.yoe == df.yoe.max()]
# print(max_yoe.emp)

bsr_data = df[df["District name"] == "Bulandshahr"]
# print(bsr_data)
# print(df.columns)
# print(bsr_data.Literate)
# for col in df.columns:
#     print(col)

bsr_data.to_csv("./bsr_data.csv")

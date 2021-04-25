import pandas as pd
import xlrd
from pandas import ExcelWriter
import openpyxl
import numpy as np
type(pd)
import matplotlib.pyplot as plt

##Read existing excel file with only celsius temps
data = pd.read_excel(r'C:\Users\Owner PC\AppData\Local\Programs\Python\Python39\CelsiusTemps.xls')

##Setting RowID as the index of the file
data.head()
data = data.set_index("RowID")

print ("\n")

print("Printing the data from the original spreadsheet containing only Celsius temperatures: ")
print (data)

print ("\n")

##Function converting Celsius to Fahrenheit
def cel_to_fahr(temp_celsius):
   
    temp_fahrenheit = (temp_celsius * 1.8) + 32
    return temp_fahrenheit


print("Printing only the Celsius Column from the original spreadsheet: ")
df = pd.DataFrame(data, columns= ['Celsius'])

print (df)

print ("\n")

##Calling the function to read the Celsius values from the spreadsheet and convert to Fahrenheit
Temp_Fahrenheit = (cel_to_fahr(data["Celsius"]))

print("Printing the converted Fahrenheit values from the function: ")
print (Temp_Fahrenheit)

print ("\n")

##re-storing the original spreadsheet in the df and adding the new Fahrenheit column to the spreadsheet
df = data
df['Fahrenheit'] = Temp_Fahrenheit

##Creating a new spreadsheet with all columns and values including the new conversions to Fahrenheit
df.to_excel('NewTemps.xlsx')

print("Printing the new data that has been saved to the new spreadsheet to include a row for Fahrenheit: ")
print (df)

print ("\n")

##determine the average of the Celsius and Fahrenheit columns
df2 = pd.DataFrame(data, columns= ['Celsius', 'Fahrenheit'])
average_temp = df.mean(axis=0)

print("Average of the Temperature in Celsius and Fahrenheit is: ", (average_temp))

##Creating the Celsius and Fahrenheit comparison graph
plt.title("Temp Comparisons")
plt.xlabel('Celsius')
plt.ylabel('Fahrenheit')
plt.bar(data['Celsius'], data['Fahrenheit'], color="red", width=0.5)
##Saving the graph as PNG
plt.savefig("Temps.png")

print ("\n")

print("Printing the Celsius and Fahrenheit Comparison Graph: ")
plt.show()

print ("\n")

##Creating the Temperature per state graph
df1=pd.DataFrame(df,columns=["State","Celsius","Fahrenheit"])

y_pos = np.arange(len(df1["State"]))
df1.plot(x="State", y=["Celsius", "Fahrenheit"], kind="bar",figsize=(9,8))
plt.xticks(y_pos, df1["State"])
plt.title("Temps per State")

##Saving the graph as PNG
plt.savefig("States.png")

print ("\n")
print("Printing the Temperature per State Graph: ")
plt.show()





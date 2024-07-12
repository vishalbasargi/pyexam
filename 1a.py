import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
cs=pd.read_csv('cars.csv') 
cs.head() 
fuel=cs['Fuel_Type'] 
prices=cs['Price'] 
plt.bar(fuel,prices,color="skyblue") 
plt.xlabel("Fuel Type") 
plt.ylabel("Price($)") 
plt.title("[Price vs Fuel]") 
plt.xticks(rotation=45,ha="right") 
plt.tight_layout() 
plt.show() 



#sudo apt update
#sudo apt install python3 python3-pip
#pip3 install pandas numpy matplotlib

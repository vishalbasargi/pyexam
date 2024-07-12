import pandas as pd
from matplotlib import pyplot as plt 
df=pd.read_csv('flights.csv') 
carrier_counts=df['carrier'].value_counts() 
plt.pie(carrier_counts,labels=carrier_counts.index,autopct='%1.1f%%',startangle=80) 
plt.title("LAB eXAM") 
plt.show() 


#sudo apt update
#sudo apt install python3 python3-pip
#pip3 install pandas matplotlib


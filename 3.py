import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv("flights.csv") 
hour_data=df['hour'] 
plt.hist(hour_data, bins=24,edgecolor='c',alpha=1) 
plt.xlabel("Hour of the day") 
plt.ylabel("Frequency") 
plt.title("Lab exam") 
plt.grid(True) 
plt.show() 


#sudo apt update
#sudo apt install python3 python3-pip
#pip3 install pandas matplotlib

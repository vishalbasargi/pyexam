import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
cr=pd.read_csv("cars.csv") 
x=cr['Age'] 
y=cr['Price'] 
fig,ax=plt.subplots() 
plt.scatter(x,y,color="red",marker="^",s=20) 
plt.xlabel("Age") 
plt.ylabel("Price") 
plt.title("Lab Exam") 


#sudo apt update
#sudo apt install python3 python3-pip
#pip3 install pandas numpy matplotlib

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


sl=pd.read_csv("sales1.csv") 
sl.head() 
sns.regplot(x="Units",y="Unit 
Price",data=sl,color="r",marker="+",scatter_kws={'color':'green'}) 
plt.title("Regression Plot",fontsize=15) 
plt.xlabel("Units (ut)") 
plt.ylabel("Unit Price ($)") 

#sudo apt update
#sudo apt install python3 python3-pip
#pip3 install pandas numpy seaborn matplotlib


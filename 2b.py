import matplotlib.pyplot as plt
sub = ['Physics', 'Maths', 'C Language', 'Electronics', 'English'] 
marks = [91, 98, 87, 96, 86] 
plt.plot(sub, marks, marker='o', color='b', linestyle='-', linewidth=2) 
plt.xlabel('Subjects') 
plt.ylabel('Marks') 
plt.title('Lab exam') 
plt.show() 

#sudo apt update
#sudo apt install python3 python3-pip
#pip3 install matplotlib


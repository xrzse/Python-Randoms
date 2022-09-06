#Here i play around with matplotlib
from tkinter import Label
from matplotlib import pyplot as plt

x = [1,2,3,4,5,6,7]
y = [532,352,243,536,421,424,643]
plt.plot(x,y, color = '#444444', linewidth=3, linestyle = '--', label = 'Tes')
y1 = [231,421,233,421,111,222,115]
plt.plot(x, y1, color = '#221166', linewidth = 1, label = 'Louis' )
plt.xlabel('ages')
plt.ylabel('salary')
plt.title("Salary vs age")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

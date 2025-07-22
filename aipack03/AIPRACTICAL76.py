import matplotlib.pyplot as plt

x=[2,3,4,5,6,7]
y=[4,9,16,25,36,49]

plt.plot(x,y, marker='D' , markerfacecolor = 'red', markersize=15, linestyle='dashed',color='blue')

plt.title("Number with square values", fontsize = 14, color = 'red')
plt.xlabel("------Numbers------",fontsize=14,color='red')
plt.ylabel("------Squares------",fontsize=14,color='blue')
plt.axis([1,8,2,51])
plt.grid(True)


a=int(input("Enter you want to print a square number: "))

plt.annotate(f"Square of {a}",
             fontsize = 10 , color='red',
             xytext=(3,40), xy=(a,a*a),
             arrowprops=dict(facecolor='blue', shrink=.1))

plt.show()
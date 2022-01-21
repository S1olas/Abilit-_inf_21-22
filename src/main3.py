import numpy as np




a = np.array([[1,2],[2,2]])
a.shape
(2,2)
b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
b.shape
(2,2,2)
a.ndim
2
b.ndim
3

t = np.array([5,6,7,8,10,7,1])
p = np.arange(1,8)
h = t+p
print("Somma",t,"+",p,"=",h)
t+=1
print("Autoincrement t",t)


a1 = np.arange(5)
a2 = np.zeros_like(a1)

a2[:]=a1[:]
a2[3]=1000
a2==a1
print(a2==a1)

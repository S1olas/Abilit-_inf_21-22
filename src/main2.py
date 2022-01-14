import sys

lll =[]
with open('input1.txt','r')as kkk:
  for line in kkk:
    line = line.strip()
    if len(line)>0:
      lll.append(list(map(int,line.split(','))))
print(lll)



fin=open('input1.txt','r')
aaa=[]
for line in fin.readlines():
  aaa.append([int(tt) for tt in line.split(',')])


oo=[]
with open('input1.txt','r') as kk:
  for line in kk:
    line = line.strip()
    if len(line)>0:
      oo.append(list(map(int,line.split(','))))
print(oo)

x =[[12,7,3],
[4,5,6],
[7,8,9]]

y=[[5,8,1,2],
[6,7,3,0],
[4,5,9,1]]
result=[[0,0,0,0],
[0,0,0,0],
[0,0,0,0]]
for i in range(len(x)):
  for j in range (len(y[0])):
    for k in range(len(y)):
      result[i][j]+= x[i][k]*y[k][j]
for r in result:
  print(r)


def print_matrix(matrix):
  for i in range(len(matrix)):
    for j in range (len(matrix[i])):
      print(str((matrix[i][j]))+"\t","end =")
    print("\n")
  def matrix_x_matrix(x,y):
    result1 =[[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for i in range(len(x)):
     for j in range(len(y[0])):
      for k in range(len(y)):
        result1[i][j]+= x[i][k]*y[k][j]
  return result1




class Person:
 def __init__(self, name, age):
  self.name = name
  self.age = age
 def myfunc(self):
  print("Hello my name is "+ self.name)

p1 = Person("John",36)
p1.myfunc()

class Film:
 def __init__(scheda, titolo, uscita, regista):
  scheda.titolo = titolo
  scheda.uscita = uscita
  scheda.regista = regista
 def myfunc1(scheda):
  print("Io sono il film  "+ scheda.titolo)
t1 = Film("Joker","2019","Todd Philpips")
t1.myfunc1()



def divide(x,y):
  try:
    result = x/y
  except ZeroDivisionError:
    print("division by zero!")
  else:
    print("result is",result)
  finally:
    print("executing finally clause")

divide(2,1)

divide(2,0)






coordinate=['a','b','c']
value =[3,4,5]

result = zip(coordinate,value)
result_list = list(result)
print(result_list)

c,v = zip(*result_list)
print ('c=',c)
print('v=',v)

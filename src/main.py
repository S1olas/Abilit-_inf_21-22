import sys
a = 3
b = 5
a+b
print(a+b)

d = 3+5j
d+a
print(d+a)
print(type(d))


t = True
k = True

if(t and k):
  print(d)


  array=[1,3,8]
  if(9 in array): 
    print("ok")
  else:
    print("no")
    
    
import math
print(math.pi)

print(d**2)

math.sin(1)
print(math.sin(math.pi/2))
r = float(input("Raggio="))

def areacerchio(r):

 area =(r**2)*math.pi
 print(area)

areacerchio(r)


s = "hello"
s1 = "world"

print(s+s1)

#Programmi del 17/12/2021

m=[0,2,"ciao"]

print(m[2])

aa =range(10)
for x in [0,1,2,3,4,5,6,7,8,9]: print (aa[x])

bb=[y*2 for y in aa]
for x in [0,1,2,3,4,5,6,7,8,9]: print (bb[x])
aa1 = [1,2]
aa2 = [3,4]
aa3 = [5,'b']
f = [(x1,x2,x3) for x1 in aa1 for x2 in aa2 for x3 in aa3]
#stampa i primi 7 elementi
for x in range(0,7):    
  print (f[x])
# li stampa tutti
  print (f)

  #aa1.remove()
  print (' array modificato', aa1)

  import time

  i = list(range(10000))
  v = list(range(10000))
  T1 =time.perf_counter()
  s2 = i+v
  T2 =time.perf_counter()
  print('tempo di esecuzuione:', T2-T1,"s")

  prova=['a','b','c']
  print('lista iniziale', prova)
  prova.append('ag')
  print('Lista modificata',prova)
tup1 = (2,)
print(type(tup1))
tup2 = (4,)
print('tupla',tup1)
tup3 = tup1+tup2
print(tup3)

di = {'name':'prova', 'age':23,'home':'Trieste'}
print(di['home'])
#E' vero se c'è una locuzione di memoria con quel nome e non è il nome della variabile
#print ('name' in di)
#print ('Trieste' in di)
for i in di:
  print(di[i])


  #Istruzioni di controllo di flusso

bool1 = True

while(bool1 == True):
    print('Sono True')
    x5 = int(input("Continuo 0, Fermo 1"))
    #if(x5 == 1):
     # break
    if(x5==1):
     bool1 = False


aprova = iter(list(range(20)))
for i in aprova:
  print (i)

di2 ={1:'a',2:'k',8:'j'}
#Mi stampa il nome che ho dato alla locuzione di memoria, detto key
for i in di2.keys():
  print('Keys del dictionary di2',i)
#Mi stampa tutto l'elemento del dictionary
for i in di2.items():
  print('Item del dictionary di2',i)
#Mi stampa solo il valore contenuto della variabile
for t in di2.values():
  print('Item del dictionary di2',t)



#14/10

def arearettangolo():
  print('calcolo area rettangolo')
  base = float(input("base="))
  altezza = float(input("Altezza="))
  arearett = base*altezza*0.5
  print('Area del rettangolo è',arearett)

arearettangolo()


def f(y9):
 if y9>= 0.0:
   return y9**2*math.exp(-y9)
 else:
    return 0.0

infile ='mydata.dat'
outfile='myout.dat'

indata = open(infile, 'r')
linee=indata.readlines()
indata.close()
processati=[]
x9=[]
for el in linee:
  valori = el.split()
  x9.append(float(valori[0]))
  #y9=float(valori[1])
  #processati.append(f(y9))

outdata = open(outfile,'w')
i = 0
for el in processati:
  outdata.write('%g %12.5e\n' % (x9[i],el))
  i+=1
outdata.close




lll =[]
with open('input1.txt','r') as kkk:
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
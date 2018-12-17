'''

                            Robert Abel 
                            Python Exercises
                            Dr. Scharff


'''

#1
print(5/3)
print (5%3)
print(5.0/3)
print(5/3.0)
print(5.2%3)

#2
''' print (2000.3 **200)'''
#above function is invalid
print(1.0+1.0-1.0)
print (1.0 +1.0e20-1.0e20)
print(float(123))
print(float('123'))
print(float('123.23'))

#3
'''print(int('123.23'))'''
'''print(int('123.23')'''
#above function is invalid
print(int(float('123.23')))
print(str(12))
print(str(12.2))
print(bool('a'))
print(bool(0))
print(bool(0.1))

#5
number_found = 0
x = 11 
while number_found < 20:
  if x % 5 == 0 and x % 7 == 0 and x % 11 == 0:
    print(x)
    number_found += 1
  x+=1
  
 #6
def is_prime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):   
        if n%i==0:
            return False    
    return True
    
def is_prime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):   
        if n%i==0:
            return False    
    return True

def prime_spitter(n):
  while n > 0:
    if is_prime(n):
      print(n)
      n-=1
    else: n-=1
      
prime_spitter(7)

def is_prime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):   
        if n%i==0:
            return False    
    return True

def prime_spitter2(n):
  counted = 0;
  x = 2
  while counted < n:
    if is_prime(x):
      counted+=1
      print(x)
      x+=1
    else: x+=1
      
prime_spitter2(7)

#7
def list_printer(n):
  for i in n:
    print(i)
    
list_printer([1,2,3])

def list_printer(n):
  n.reverse()
  for i in n:
    print(i)
    
list_printer([1,2,3])


def list_size(n):
  counter = 0
  for i in n:
    counter+=1
  return counter
print(list_size([1,2,3,4]))

#8
a = ["a","b","c"]
b = a
b[1] = "d"
print(b[1])
c = a[:]
c[2] = "e"
print(c)

def set_first_lem_to_zero(a):
  a[0] = 0
  return a
a = ["a","b","c"]
set_first_lem_to_zero(a)
print(a)

#9

def list_maker(a):
  b = []
  for i in a:
    for x in i:
      b.append(x)
  return b;

list_maker([[1,3],[3,6]])

#10

#x = np.arange(0,2,0.1)   # start,stop,step
#y = np.sin(x)**2 * np.power(np.e,np.power(-x,2))
  
#plt.plot(x,y, color='red', linewidth =3)
#plt.title("Sine Graph")
#plt.xlabel('x values from 0 to 2')
#plt.ylabel('sin^2(x - 2) e^(-x^2)')
#plt.show()

#11


def iteration(x):
  z = 1;
  for y in x:
    z *=y
  return z
    
iteration([1,2,3,4,5])

def recursive(x):
  
  if (len(x)==1): 
    return x[0]
  else: 
    return recursive([x[0]]) * recursive(x[1:])
  
recursive([1,2,3,4,5])

#12

def Fib(n):

    if(n==0):
        return 0
    elif(n==1 or n==2):
        return 1
    else:
        return Fib(n-1) + Fib(n-2)
      
Fib(14)
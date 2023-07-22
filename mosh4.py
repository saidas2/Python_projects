# ------------ functions----------

def greet_user():
    print('Hi there')
    print('Welcome aboard')


print('Start!')
greet_user( )
print('finish')


#----------- parameters-----------
#https://youtu.be/_uQrJ0TkZlc?t=9331

def greet_user(name):
    print(f'Hi {name}')
    print('Welcome aboard')


print('Start!')
greet_user('saida')
greet_user('mary')
print('finish')
# can receive information in function
# out put will be for two names
# pparametres are the holes or placeholders that we define in our function for receiving information, 3
# arguments are the actual pieces of information that we supply to these function


def greet_user(first, last):
    print(f'Hi {first} {last}')
    print('Welcome aboard')


print('Start!')
greet_user('mary', 'saida')
print('finish')


# ---------------keyword arguments-----------------



def greet_userr(first_name, last):
    print(f'Hi {first_name} {last}')
    print('Welcome aboard')


print('Start!')
#greet_userr( 'ismoilova', first_name='saida') #having parametre argumente followed by it s value call a keyword argument
print('finish')

# --------------------- return statement----------------
def square(number):
   return number*number

print(square(3))
# be default all of the functions return none
# if you want return something you can use return statement 


#---------------- creating a reusable function-------------------

def emoji(message):
    words= message.split (' ')
    emojis={
        ':)' :'😊',
        ':(' : '😓'
    }
    output=''
    for word in words:
     output+= emojis.get( word, word)
    return output

message= input('>')
print(emoji(message))

# ------------------------exceptions-----------------------------
try:
    age=int(input('age'))
    income=20000
    risk=income/age
    print(age )
except ZeroDivisionError:
    print('age cannt be zero')
except ValueError:
    print('invalid value')


# ----------------- classes-----------------------



#upper case 'cause it is for naming classes  conventiol
# don't use an underscore, instead capitalize the first letter of the word
class Point :   # we used classes to define neew types
    def move(self): # this types can have methods like this
      print('move')  

    def draw (self):
        print('draw')


point1= Point()
point1.x=10 # and they also can have attributes taht we can set anywhere in our programs
point1.y=20
print(point1.x)
point1.draw()

point2=Point()
point2.x=30
print(point2.x)



#--------------------constructors-------------------

class Point :  
    def __init__(self, x, y): # init short from initialize
         self.x=x
         self.y=y
        
    def move(self): 
      print('move')  

    def draw (self):
        print('draw')


point=Point(10,20)
point.x=11
print(point.x)



class Person:
    def __init__(self, name):
        self.name=name
    def talk(self):
        print(f'hi, i am {self.name}')


john=Person("john smith")
john.talk()


bob= Person('bob smith')
bob.talk()


#----------  inheritance------------------

#    DRY-don't repeat yourself

class Mammal:
     def walk(self):
        print('walk')



class Dog(Mammal):
    def bark(self):
        print('bark')

class Cat(Mammal):
    pass # it means nothing just to make python happier


dog1=Dog()
dog1.bark()














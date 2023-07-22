#name= input('whats your name?')
#color= input('your favourite color')
#print (name, 'likes', color)  


#course= 'python for beginers' 
#        012345 
#print(course[0],course[-1], course[2:4], course[1:], course[:5])


#course= 'python for beginers' 
#another= course[:]
#print(another)


#name= 'Jennifer'
#print(name[1: -1])



#-----------formatted strings-----------


#first= 'john'
#last= 'smith'
#message= first + ' [ ' + last + '] is a coder'
#msg = f'{first} [{last}] is a coder'
#print(msg)

#---------------string methods---------
course='python For Beginners'
print(len(course))
print( course.upper())
print(course.lower())
print(course.find('p'))
  # will show 0, because p in zero position, sensative to uppercase and lowerccase
print(course.replace('Beginners', 'absolute'))
print( 'python' in course)
 # in is used for boolean it is true or false

greet='        hello bob        '
print(greet.lstrip()) # 'hello bob    '
print(greet.rstrip()) # '     hello bob'
print(greet.strip())  # 'hello bob'






#fcc----- prefixes------
line= 'Please have a nice day'
print(line.startswith('Please')) # is it starts with ??
print(line.startswith('p'))

#------------arithmetic operations---------------
print(10/3) # floating number
print (10//3) # will run integer
print(10%3)  # modules 
print(10**3) # to the power of 



x=10
x=x+3
x+=3 # argumented assignment operator
x-=3
print(x) 

x=10+3*2
print(x)
# orders of operations 
# parenthesis ()
# exponentiation 2**3
# multiplicationl or division
# addition or substraction

x=10+3*2**2
print(x)

x=(2+3)*10
print(x)

#---------------maths funtions-------
z=2.9
print(round(z))


print(abs(-2.9)) # always give positive numbers



import math
print (math.ceil(2.9))
print(math.floor(2.9))
# all info https://docs.python.org/3/library/math.html


#-------------  if statement-----------

is_hot=False
if is_hot:
 print("it's a hot day")
print ('Enjoy your day')
# now it shows ji=ust enjoy your day because is hot is false
# in ccase where it is true terminal wil show it is hot day too

is_hot=False
is_cold=False
if is_hot:
 print("it's a hot day")
 print('drinlk plenty water')
elif is_cold:
  print(' it is a cold day')
  print('wear warm clothes')
else:
  print('it is a lovely day')
print ('Enjoy your day')


price=100000
good_credit=True
if good_credit:
   down_payment= 0.1*price
else :
  down_payment= 0.2*price
print (f"down payment: {down_payment}")


#-------- logical operators-----------

has_high_income= True
has_good_credit=True

if has_high_income and has_good_credit: # will work only when two comditions are true   # this is a logical AND operator
  print('eligible for loan')


has_high_income= True
has_good_credit=False

if has_high_income or has_good_credit: # if one of them true 
  print('eligible for loan')


has_high_income= True
has_good_credit=False

if has_high_income and not has_good_credit: # if one of them true 
  print('eligible for loan')



 # ------- comparison operations---------

temp=30

if temp>30:
  print('hot day')
else:
  print('not so hot')
 # we also have >   <   <=   >=    =   ==  !=(not equal)

name= 'Sa'

if len(name)<3:
  print('must be at least 3')
elif len(name)>50:
  print('name can be maximum 50')
else :
  print('name loooks good')




#*------------- project weight converter------------
weight= int (input ('weight :')) # will return in integer to be multiplied
unit = input ('(L)bs or (K)g: ')

if unit.upper()=="L":
  converted=  weight * 0.45
  print(f"You are{converted} kilos")
else:
  converted = weight/0.45
  print(f'you are {converted} pounds')


#------------while loops-----------------

i = 1
while i<=5:
 print(i)
 i=i+1




#------- nested loops-----------------
# adding one loop inside another loop
for x in range (4):
    for y in range (3):
        print(f'({x}, {y})')


numbers=[5, 2, 5, 2, 2]
for x_count in numbers:
    print('x' * x_count)


numbers=[5, 2, 5, 2, 2]
for x_count in numbers:
    output=''
    for count in range (x_count):
      output += 'x'
    print(output)

num=[2, 2, 2, 2, 6]
for x_count in num:
    output=''
    for count in range (x_count):
      output += 'x'
    print(output)

#------------- lists-------------------------
names= ['john', 'bob', 'mosh', 'sarah', 'mary']
print(names[-2]) 

names= ['john', 'bob', 'mosh', 'sarah', 'mary']
print(names[2:4]) 

names= ['john', 'bob', 'mosh', 'sarah', 'mary']
print(names[:]) 


largest=1
for num in [9, 40, 50, 70, 5, 8]:
  if num>largest:
    largest=num
print(largest)


#--------------- 2d lists---------------


matrix= [
 [1,2,3],
 [4,5,6],
 [7,8,9]
]
for row in matrix:
  for item in row:
    print(item)


#--------------list methods------------------
numbers=[5, 2, 1, 7, 4]
numbers.append(20)
print(numbers)


numbers=[5, 2, 1, 7, 4]
numbers.insert(0,10)
print(numbers)


numbers=[5, 2, 1, 7, 4]
numbers.remove(5)
print(numbers)

numbers=[5, 2, 1, 7, 4]
numbers.clear
print(numbers)

numbers=[5, 2, 1, 7, 4]
numbers.pop()
print(numbers)


numbers=[5, 2, 1, 7, 4]
print(numbers.index(5))

numbers=[5, 2, 1, 7, 4]
print(50 in numbers)


numbers=[5, 2, 1, 5, 7, 4]
print(numbers.count(5))


numbers=[5, 2, 1, 5, 7, 4]
numbers.sort()
print(numbers)
 

numbers=[5, 2, 1, 5, 7, 4]
numbers.sort()
numbers.reverse()
print(numbers)


numbers=[5, 2, 1, 5, 7, 4]
num2= numbers.copy()
numbers.append(10)
print(num2)


number=[1, 1, 2, 3, 4, 5, 6]
uniques=[]
for numbers in number:
  if numbers not in uniques:
    uniques.append(numbers)
print(uniques)

#--------------tuples-----------------

#https://youtu.be/_uQrJ0TkZlc?t=8005

number=(1, 2, 3)
print(number[0])
#cant accidentally modify list

#-------------unpacking---------------
coordinates=(1, 2, 3)
#x= coordinates[0]
#y= coordinates[1]
#z= coordinates[2]
x,y,z= coordinates
print(x)

#---------- dictionaries--------------
customer={
  'name': 'john smith',
  'age': 30,
  'is_verified': True
}
print(customer.get('name'))
print(customer.get('birthday', 'oct 7'))


customer={
  'name': 'john smith',
  'age': 30,
  'is_verified': True
}
customer['name']='saidochka' # can change or add new value
print(customer['name'])




phone=input('Phone:')
numbers={
  '1': 'one',
  '2': 'two',
  '3': 'three'
}
output=''
for ch in phone:
  output+=numbers.get(ch, '!') + ' '
print(output)



#----------- emoji converter :)  ------------------------
message= input('>')
words= message.split (' ')
emojis={
    ':)' :'😊',
    ':(' : '😓'
}
output=''
for word in words:
  output+= emojis.get( word, word)
print(output)






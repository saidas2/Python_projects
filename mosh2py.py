#------------while loops-----------------

i = 1
while i<=5:
 print(i)
 i=i+1
print('done')

i = 1
while i<=5:
 print('*' * i)
 i=i+1
print('done')

#----------- guessing game-----------  https://www.youtube.com/watch?v=_uQrJ0TkZlc&t=2919s
secret_number=9
guess_count=0
guess_limit =3
while guess_count < guess_limit:
    guess =int (input ('guess:'))
    guess_count+=1
    if guess == secret_number:
        print('you won!')
        break
else:
        print('you failed1 !')

#--------------- car game---------------------

command=''
started=False
while True:
    command=input('> ')
    if command== 'start':
        if started:
            print('car is already started!')
        else:

            started = True
        print('car started..')
    elif command == 'stop':
        if not started:
          print('the car is already stopped')
        else :
            started= False
            print('car stopped')
    elif command=='help':
        print("""
start - to start the car 
stop - to stop the car 
quit - to quit 
        """)
    elif command == 'quit':
        break
    else:
      print("sorry dont understand it")


#----------for loops-----------------------------


for item in "python":
  print(item)

for item in ['sara', 'mosh', 'me']:
  print(item)

for item in [1, 2, 3, 4, 5]:
  print(item)

for item in range(10):
  print(item)

for item in range( 5, 10):
  print(item)

for item in range(5, 15, 2):
            #    5-strating number, 15-last one, 2- interval
  print(item)

prices=[10, 20, 30]
total=0

for price in prices:
   total += price
print(f"total: {total}")

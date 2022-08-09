#Exercise 1 <br>
#<p>Cube Number Test... Print out all cubed numbers up to the total value 1000. 
#Meaning that if the cubed number is over 1000 break the loop.</p>

number = list(range(1,1001))
cube = number**3
cubes.append(cube)
for cube in cubes:
        print(cube)


#Exercise #2
#Get first prime numbers up to 100
for n in range(1,101):
status = True
if n < 2:
    status = False
else:
    for i in range(2,n):
        if n % i == 0:
            status = False

    if status:
        print(n)

#Exercise 3
#Take in a users input for their age, if they are younger than 18 print kids, if they're 18 to 65 print adults, else print seniors

age = input("What is your age?")
if age is < 18:
    print("kids")
elif age is == 18 and < = 65:
    print(adults)
else:
    print(senior)
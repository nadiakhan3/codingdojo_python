for i in range(1, 10, 1):
    print(i)
    #this just means i=0 until i is 9
    #output would be 1, 2, 3, 4, 5, 6, 7, 8, 9

for t in range(1, 10,3):
    print (t)
    # this means t=1 add 3 each time you go through loop
    #output would be 1, 4, 7

for y in range(5):
    if y < 5:
        print(y)
    elif y == 3:
        print("y is 3")
        #output would be 1, 2, "y is 3" , 4

for j in range(20, 1, -3):
    print(j)
#output would be 20, 17, 11, 8, 5, 2

cities = ["London", "Paris", "Tokyo"]
for city in cities:
    print(city)
    #output would be London, Paris, Tokyo

numbers = [7, 13, 8, 42]
for x in range(0, len(numbers)):
    print(x)
    print(numbers[x])
if numbers[len(numbers) - 1] == 42:
    print("The answer to life, the universe, and everything.")
# out put would be 0, 7, 1,13,2,8,3,4. The answer to life, the universe, and everything. 

for num in range(10):
    if num % 2 == 0:
        print("Hello")
    elif num % 4 == 0:
        print("World")
    else:
        print(num)
        # x=0 ....hello
        # x=1 .... 1
        #x=2... hello
        #x=3...3
        #x=4....hello
        #x=5...5
        #x=6....hello
        #x=7....7
        #x=8....hello
        #x=9...9
for num in range(10):
    if num % 4 == 0:
        print("Hello")
    elif num % 2 == 0:
        print("World")
    else:
        print(num)

        #output: hello, 1, world, 3, hello, 5, world, 7, hello, 9

 pet_info = {
    "name": "Fido", 
    "age": 4, 
    "trick": "rolls over"
}
for key in pet_info:
    print(key)
    print(pet_info[key])
#output name, Fido, age, 4, trick, rolls over       

things_to_remember = {
    "First": "use the 20 minute rule and use the platform and other resources to find my answer",
    "Second": "ask my classmates for help, like how I would ask a fellow employee at my job",
    "Third": "ask an available TA in a public setting, so everyone can benefit from my question",
    "Fourth": "ask an available instructor"
}
for num, step in things_to_remember.items():
    print(num + ", I will " + step)
    #output: First I will use the 20 minute rule and use the platform and other resources to fnd my answer
    #output: Second I will ask my classmates for help, like how I would ask a fellow employee at my job
    #output: Third ask an available TA in a public setting so everyone can benefit from my question
    #output: Fourth ask an available instructor
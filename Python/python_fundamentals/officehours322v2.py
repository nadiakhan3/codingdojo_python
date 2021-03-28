import random
def randInt(min=0, max= 100):
    num = random.random()
    return num


def cool(list):
    return list[0]+len(list)
    
cool([1,5,6,8,3,5])
print(cool([1,5,6,8,3,5]))

my_dict = { "name": "Noelle", "language": "Python" }
for p in my_dict:
    print(p)
    print(my_dict["name"])

x = [[5,2,3], [10,8,9]]
x[1][0]=15
print(x)

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]

students[0]['last_name']= 'Bryant'
print(students)

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

sports_directory['soccer'][0]="Andres"
print(sports_directory)

z = [ {'x': 10, 'y': 20} ]
z[0]['y'] = 30
print(z)

def iteratedictionary(list):
    for i in list:
        print(i)

iteratedictionary([
    {'first_name': 'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ])
    
def iterateDictionary2(key_name, some_list):
    print(some_list[key_name])

iterateDictionary2([
    {'first_name': 'Nadia', 'last_name': 'Khan'}
    {'first_name': 'Nadia', 'last_name': 'Khan'}
])


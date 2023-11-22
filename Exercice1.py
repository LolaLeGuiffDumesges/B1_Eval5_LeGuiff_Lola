# EXERCICE 1
# 1.

def sum(a,b):
    sum = 0

    for i in (a, b):
        sum = sum + i

    print(sum)
#sum(1,5)


def substract(a, b):

    sub = 0

    for i in (a, b):
        sub = sub - i
    
    print(sub)
#substract(1,5)


def multiplication(a, b):

    mul = 1

    for i in (a, b):
        mul = mul * i
    
    print(mul)
#multiplication(6, 7)


def division(a, b):

    div = 1

    for i in (a, b):
        div = div / i 

    print (div)
#division(34, 9)





# 2.

def sum(*args):
    sum = 0

    for arg in args:
        sum = sum + arg

    print(sum)
#sum(3,8)


def substract(*args):

    sub = 0

    for arg in args:
        sub = sub - arg
    
    print(sub)
#substract(1,5)


def multiplication(*args):

    mul = 1

    for arg in args:
        mul = mul * arg
    
    print(mul)
#multiplication(6, 7)



def division(*args):

    div = 1

    for arg in args:
        div = div / arg

    print (div)
#division(34, 9)




# 3.

while True:

    opération =('addition', 'soustraction', 'multiplication', 'division')

    user = input("Quelle type d'opération voulez vous appliquer :" )
    nb = ("Entrer deux nombre : ")


    if user.lower() == 'stop':
        break
    
    
    if user == 'addition':
    
    # for i in opération:
        def sum(*args):
            sum = 0

            for arg in args:
                sum = sum + arg

            print(nb)

    if user == 'soustraction':

        def substract(*args):

            sub = 0

            for arg in args:
                sub = sub - arg
            
            print(nb)


    if user == 'multiplication':
        
        def multiplication(*args):

            mul = 1

            for arg in args:
                mul = mul * arg
            
            print(mul)


    if user == 'division':

        def division(*args):

            div = 1

            for arg in args:
                div = div / arg

            print (div)

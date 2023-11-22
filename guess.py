from random import randint

def guess1():
    secrete_number=randint(1,10)
    while True:
        guess=int(input("điền số"))
        if secrete_number==guess:
            print("you got it")
            break
        elif secrete_number<guess:
            print("nó quá cao")
        else:
            print("nó quá thấp")
            
def guess2():
    secret_number=7
    guess=int(input("What number am i thinking of?"))
    if secret_number=guess:
        print("Yay,you got it")
    else: 
        print("No,that not it")
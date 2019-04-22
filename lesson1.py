def is_integer(num):
    if int(num) != num:
        return False
    else:
        return True



def prime(x):
    for factor in range(2, x):
        div = x / factor
        if is_integer(div):
            print('It is composite; can be divided by %d'%factor)
            return
    print('It is prime') 


#Input source
print('Enter a number')
i = input()
fi = int(i)
prime(fi)
    

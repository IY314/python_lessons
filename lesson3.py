def print_table(x):
    for y in range(1,x+1):
        for z in range(1,x+1):
            if z >= y:
                print(y*z,end='\t')
            else:
                print(' ',end='\t')
        print('\n\n')
    
    
print_table(243)



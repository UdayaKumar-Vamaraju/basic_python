start=int(input("Enter starting number:"))

end=int(input("Enter ending number:"))



for i in range(start,end):
    if i<2:
        continue

    is_prime=True

    for j in range(2,i):
        if i%j==0:
            is_prime=False
            break


    if is_prime:
        print(i)
        
              

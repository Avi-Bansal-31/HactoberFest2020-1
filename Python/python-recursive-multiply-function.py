while(True):
    def multiply(m,n):
        if(n==1):
            return m
        else:
            return (m + multiply(m,n-1))
    
    M = int(input("Input M "))
    #gets input from user
    N = int(input("Input N "))
    print(multiply(M,N))

def prime_bellow_num(n):
   b=[]
   num=2
   j=0
   b.append(2)
   while len(b)-1<n:
        if all(num%i!=0 for i in range(2,int((num)**0.5)+1)):
            b.append(num)
        num += 1
   print b[n]
 
 prime_bellow_num(10001)

import prime
MAX = 10000
squares = dict.fromkeys((x*x for x in xrange(1, MAX)), 1)
prime._refresh(MAX)

for x in xrange(35, MAX, 2):
     if not prime.isprime(x):
        goldie = 0
        
        for p in prime.prime_list[1:]:
          if p >= x: 
            break
          if squares.has_key((x - p)/2):
            goldie = 1
            break
            
        if not goldie:
          print x
          break

from primitives.core import MERSENNE_PRIME, MERSENNE_EXPONENTS, EULERS_NUMBER, FERMAT_PRIME
from primitives.core import BasePseudorandomGenerator
from primitives.core import xor, mod, is_coprime

class LinearCongruentialGenerator(BasePseudorandomGenerator):
    def __init__(self, seed):        
        super().__init__(seed)
        self.seed = seed
        
        
    def __init__(self, seed, multiplier, increment, modulus):
        super().__init__(seed)
        
        ## Seed is also from parent class but here we initialize it anyway
        ## by requiring it as an argument
        self.seed = seed

        ## Initializing, modulus 'm', multiplier 'a', increment 'c'
        self.a = multiplier
        self.c = increment
        self.m = modulus

        ## Check if the constraints are met
        self.constraints()
        
        ## From parent class
        self.state = 0

    def constraints(self):
        return 0 <= self.m and 0 <= self.a < self.m and 0 <= self.c < self.m and 0 <= self.seed < self.m
    
    def lehmer(self, c=0, a=7**5, d=1, m=2**31-1):                
        if(not 1 < self.seed < self.m):
            raise ValueError("Seed must be in range 1 < seed < m")
        
        product = self.a * self.seed

        low = product & ((1 << MERSENNE_EXPONENTS[0]) - 1)
        high = product >> MERSENNE_EXPONENTS[0]

        reduced = low + high * d


        if(reduced >= self.m):
            reduced -= self.m
        
        if(high == 0):
            return reduced
    
        return self.lehmer()
        

    def lehmer_rng(self, x, a=48271, m=(2**31 - 1), e=31, d=1, depth=10):
        if depth == 0:
            return x
        
        # Calculate the product ax
        product = a * x
        
        # Split the product into high and low parts
        low = product & ((1 << e) - 1)  # equivalent to ax mod 2^e
        high = product >> e  # equivalent to floor(ax / 2^e)
        
        # Apply the reduction step
        reduced = low + high * d
        
        # Ensure the result is within the range by subtracting m if necessary
        if reduced >= m:
            reduced -= m
        
        # Recursively generate the next number
        return self.lehmer_rng(reduced, a, m, e, d, depth - 1)        


    def print_param(self):
        print(f"m: {self.m}, a: {self.a}, c: {self.c}")

    def next(self, seed):        
        self.state += 1 
        return mod(self.a * self.next(seed) + self.c, self.m) 
    




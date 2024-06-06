from primitives.core import MERSENNE_PRIME, MERSENNE_EXPONENTS, EULERS_NUMBER, FERMAT_PRIME
from primitives.core import BasePseudorandomGenerator
from primitives.core import xor, mod, is_coprime

class LinearCongruentialGenerator(BasePseudorandomGenerator):
    def __init__(self, seed):        
        super().__init__(seed)
        self.seed = seed
                
    # def __init__(self, seed, multiplier, increment, modulus):
    #     super().__init__(seed)
        
    #     ## Seed is also from parent class but here we initialize it anyway
    #     ## by requiring it as an argument
    #     self.seed = seed

    #     ## Initializing, modulus 'm', multiplier 'a', increment 'c'
    #     self.a = multiplier
    #     self.c = increment
    #     self.m = modulus

    #     ## Check if the constraints are met
    #     self.constraints()
        
    #     ## From parent class
    #     self.state = 0

    def constraints(self):
        return 0 <= self.m and 0 <= self.a < self.m and 0 <= self.c < self.m and 0 <= self.seed < self.m
    
    ##TODO self.seed should be replaced with name 'reduction', and appropiate assignments
    ##      of self.seed to reduction should be made especially for the line
    ##      instead of self.seed = low + high * d, it should be reduction = low + high * d
    ##      accordingly appropiate adjustments should be made in the function signature
    def lehmer(self, a=48271, m=(2**31 - 1), e=31, d=1, depth=10):
        if depth == 0:
            return self.seed
        
        # Calculate the product ax
        product = a * self.seed
        
        # Split the product into high and low parts
        low = product & ((1 << e) - 1)  # equivalent to ax mod 2^e
        high = product >> e  # equivalent to floor(ax / 2^e)
        
        # Apply the reduction step
        self.seed = low + high * d
        
        # Ensure the result is within the range by subtracting m if necessary
        if self.seed >= m:
            self.seed -= m
        
        # Recursively generate the next number
        return self.lehmer(a, m, e, d, depth - 1)        


    def print_param(self):
        print(f"m: {self.m}, a: {self.a}, c: {self.c}")

    def next(self, seed):        
        self.state += 1 
        return mod(self.a * self.next(seed) + self.c, self.m) 
    




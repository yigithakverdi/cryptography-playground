## This script contains the core building block of mathemtical definitions
## it contains one way functions and other cryptographic primitives
##
## Note that this script is not meant to be run as a standalone script and
## it is recommended that this code should not be changed without any mathematical
## evidence or proofs. 
## 
## Accordingly each functions has a mathematical definition and a reference
## given to make the playground function correctly.

## Globals
MERSENNE_PRIME = 2 ** 31 - 1

## List of Mersenne Exponents from the source - https://oeis.org/A000043
MERSENNE_EXPONENTS = [	2, 3, 5, 7, 13, 17, 19, 31, 61, 89, 107, 127, 521, 607, 1279,
                      2203, 2281, 3217, 4253, 4423, 9689, 9941, 11213, 19937, 21701, 23209,
                      44497, 86243, 110503, 132049, 216091, 756839, 859433, 1257787, 1398269, 2976221,
                      3021377, 6972593, 13466917, 20996011, 24036583, 25964951, 30402457,
                      32582657, 37156667, 42643801, 43112609, 57885161]

FERMAT_PRIME = 2 ** 16 + 1

EULERS_NUMBER = 2.71828182845904523536028747135266249775724709369995

def xor(a, b):
    return a ^ b

def left_shift(a, b):
    return a << b


def right_shift(a, b):
    return a >> b

def mod(a, b):
    return a % b

def zero_pad(a, b):
    return a + b

def extract_middle_digits(number, n_digits):
    number_str = str(number)
    mid = len(number_str) // 2
    return int(number_str[mid-n_digits//2 : mid+n_digits//2])

## Implement following - https://en.wikipedia.org/wiki/Randomness_test
def is_random():
    pass

def gcd(p, q):
    while q != 0:
        p, q = q, p % q
    return p

def is_coprime(a, b):
    if(gcd(a, b) == 1):
        return True

class BasePseudorandomGenerator():
    def __init__(self, seed):
        self.seed = seed
        self.state = seed
    
    def seed(self, seed):
        self.seed = seed
        self.state = seed
    
    def next(self):
        raise NotImplementedError("Subclasses must implement this method")
    
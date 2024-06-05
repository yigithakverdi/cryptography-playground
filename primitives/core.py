## This script contains the core building block of mathemtical definitions
## it contains one way functions and other cryptographic primitives
##
## Note that this script is not meant to be run as a standalone script and
## it is recommended that this code should not be changed without any mathematical
## evidence or proofs. 
## 
## Accordingly each functions has a mathematical definition and a reference
## given to make the playground function correctly.

## Global Variables
## Prime numbers
MERSENNE_PRIME = 2 ** 31 - 1

## Proof Link --> 
## A one way function is a function that is easy to compute on every input, 
## but hard to invert given the image of a random input.
def owf(prime1, prime2, x):
    
    ## Do not provide the same prime numbers
    if(prime1 == prime2):
        return False
    
    ## Do not provide prime numbers less than lambda a security parameter
    if(prime1 or prime2 < 10 ** 10):
        return False

    ## One way function implementation
    return (x * prime1 + prime2) % (2 ** 256)
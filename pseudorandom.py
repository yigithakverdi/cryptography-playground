from core import MERSENNE_PRIME

class PRG:
    def __init__(self):
        pass

    ## Proof Link -->
    ## Mersenne Twister is a pseudorandom number generator (PRNG) that is based on the
    ## MT19937 algorithm. It was designed by Makoto Matsumoto and Takuji Nishimura in 1997.
    ## It is not suitable for cryptographic purposes, but it is great for simulations and
    ## other applications where a deterministic random number generator is needed.
    def MT19937(self, seed):
        return (seed * MERSENNE_PRIME) % (2 ** 256)
class PRF:
    def __init__(self):
        pass





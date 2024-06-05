from primitives.pseudorandom import LinearCongruentialGenerator

import random

def main():
    seed = random.randint(0, 100)
    LCG = LinearCongruentialGenerator(seed)
    num = LCG.lehmer()
    print(num)

if __name__ == "__main__":
    main()
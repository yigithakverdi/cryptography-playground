from primitives.pseudorandom import LinearCongruentialGenerator

def main():
    seed = 10
    LCG = LinearCongruentialGenerator()
    LCG.lehmer(seed)

if __name__ == "__main__":
    main()
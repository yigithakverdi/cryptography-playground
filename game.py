## Base class for all type of games
class Game:
    def __init__(self):
        pass

## Chosen Plaintext Attack (CPA) game
class CPA(Game):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "CPA Game"
    
    def state(self):
        pass

    def run(self, A, n):
        pass

class CCA(Game):
    def __init__(self):
        pass

    def __str__(self):
        return "CCA Game"
    
    def state(self):
        pass

    def run(self, A, n):
        pass

class CMA(Game):
    def __init__(self):
        pass

    def __str__(self):
        return "CMA Game"
    
    def state(self):
        pass

    def run(self, A, n):
        pass

class RO(Game):
    def __init__(self):
        pass

    def __str__(self):
        return "RO Game"
    
    def state(self):
        pass

    def run(self, A, n):
        pass

# class EUF(CPA):
#     def __init__(self):
#         super().__init__()

# class IND(CPA):
#     def __init__(self):
#         super().__init__()
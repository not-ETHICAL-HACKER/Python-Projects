import random,math
random.seed(1)

class Player:
    def __init__(self,name:str,mode:str="bat",ai=False):
        self.name = name
        self.mode = mode
        self.score = 0
        self.moves = []
        self.weights = {
            1 : 1,
            2 : 1,
            3 : 1,
            4 : 1,
            5 : 1,
            6 : 1,
            7 : 1,
            8 : 1,
            9 : 1,
            10 : 1
        }
        self.ai = ai
    
    def choose(self,other:"Player"):
        if not self.ai:
            i = int(input(f"{self.name}, enter your move (1-10): "))
            other.moves.append(i)
        else:
            if self.moves:
                self.weights[self.moves[-1]] += 1
            i = random.choices(list(self.weights.keys()), weights=list(self.weights.values()))[0]
            other.moves.append(i)
    
    def wicket(self):
        self.score = 0
        self.moves = []
        self.weights = {
            1 : 1,
            2 : 1,
            3 : 1,
            4 : 1,
            5 : 1,
            6 : 1,
            7 : 1,
            8 : 1,
            9 : 1,
            10 : 1
        }
    
    def calculate_score(self):
        if self.mode == "bat" and self.mode != "bowl":
            self.score += self.moves[-1]
    
p = Player("Player 1")
ai = Player("AI", ai=True,mode = "bowl")
for _ in range(10):
    p_move = p.choose(ai)
    ai_move = ai.choose(p)

    if p_move == ai_move:
        print(f"{p.name} got out!")
        break
    else:
        p.score += p_move
        print(f"{p.name} scored {p_move} runs!")

    print(f"Scores: {p.name}: {p.score}, {ai.name}: {ai.score}\n")
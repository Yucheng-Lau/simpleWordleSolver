from wordleQuestion import Wordle
from wordleSolver import WordleGeneticSolver

def main():
    game = Wordle()
    game.start()
    print(f"Target word (hidden): {game.target_word}")  # You can comment this line to play "blind"
    
    solver = WordleGeneticSolver(game)
    solver.evolve()

if __name__ == '__main__':
    main()
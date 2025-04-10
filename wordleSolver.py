import random

class WordleGeneticSolver:
    def __init__(self, game, population_size=100, mutation_rate=0.1):
        self.game = game
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.word_list = game.word_list.copy()
        self.population = random.sample(self.word_list, self.population_size)

    def fitness(self, guess):
        feedback = self.game.evaluate_guess(guess)
        score = sum(2 if r == 'correct' else 1 if r == 'present' else 0 for r in feedback)
        return score

    def select_parents(self):
        scored = [(word, self.fitness(word)) for word in self.population]
        scored.sort(key=lambda x: x[1], reverse=True)
        self.population = [word for word, _ in scored]
        return self.population[:self.population_size // 2]

    def crossover(self, parent1, parent2):
        split = random.randint(1, 4)
        child = parent1[:split] + parent2[split:]
        return child if child in self.word_list else random.choice(self.word_list)

    def mutate(self, word):
        if random.random() < self.mutation_rate:
            pos = random.randint(0, 4)
            letter = random.choice('abcdefghijklmnopqrstuvwxyz')
            mutated = word[:pos] + letter + word[pos+1:]
            return mutated if mutated in self.word_list else random.choice(self.word_list)
        return word

    def evolve(self):
        generation = 0
        while True:
            generation += 1
            best_guess = self.population[0]
            feedback = self.game.evaluate_guess(best_guess)
            print(f"Gen {generation}: Best guess = {best_guess}, Feedback = {feedback}")

            if self.game.is_correct(feedback):
                print(f"\n✅ Solved in {generation} generations! Word was: {self.game.target_word}")
                break

            parents = self.select_parents()
            next_gen = []

            while len(next_gen) < self.population_size:
                p1, p2 = random.sample(parents, 2)
                child = self.crossover(p1, p2)
                child = self.mutate(child)
                next_gen.append(child)

            self.population = next_gen
            self.population.sort(key=self.fitness, reverse=True)
import random

class Wordle:
    def __init__(self, dictionary_path='dictionary.txt'):
        self.word_list = []
        with open(dictionary_path, 'r') as file:
            for word in file:
                clean_word = word.strip().lower()
                if len(clean_word) == 5:
                    self.word_list.append(clean_word)
        self.target_word = None
        self.guesses = []
        self.result = []
        self.attempts = 0

    def start(self):
        self.target_word = random.choice(self.word_list)
        self.guesses = []
        self.result = []
        self.attempts = 0

    def make_guess(self, guess):
        guess = guess.lower()
        if guess not in self.word_list:
            return {'error': 'Guess not in dictionary'}
        elif len(guess) != 5:
            return {'error': 'Guess must be 5 letters'}
        
        self.attempts += 1
        result = self.evaluate_guess(guess)
        self.guesses.append(guess)
        self.result.append(result)
        return result

    def evaluate_guess(self, guess):
        list_guess = list(guess)
        list_target = list(self.target_word)
        result = [None] * 5

        # First pass: correct positions
        for i in range(5):
            if list_guess[i] == list_target[i]:
                result[i] = 'correct'
                list_target[i] = None

        # Second pass: present/absent
        for i in range(5):
            if result[i] is None:
                if list_guess[i] in list_target:
                    result[i] = 'present'
                    list_target[list_target.index(list_guess[i])] = None
                else:
                    result[i] = 'absent'
        return result

    def is_correct(self, result):
        return result == ['correct'] * 5
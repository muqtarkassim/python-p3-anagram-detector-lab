# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, possible_anagrams):
        word_sorted = sorted(self.word)
        return [anagram for anagram in possible_anagrams if self.is_anagram(anagram, word_sorted)]

    def is_anagram(self, candidate, sorted_word):
        candidate_lower = candidate.lower()
        return candidate_lower != self.word and sorted(candidate_lower) == sorted_word

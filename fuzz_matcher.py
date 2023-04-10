from rapidfuzz import fuzz

class FuzzyMatcher:
    def __init__(self, threshold=80):
        self.threshold = threshold
    
    def match(self, string, choices):
        """Returns the closest match to the input string from a list of choices."""
        best_match = None
        highest_ratio = 0
        for choice in choices:
            ratio = fuzz.partial_ratio(string.lower(), choice.lower())
            if ratio > highest_ratio and ratio >= self.threshold:
                highest_ratio = ratio
                best_match = choice
        return best_match

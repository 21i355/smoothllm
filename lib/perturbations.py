# import random
# import string

# class Perturbation:

#     """Base class for random perturbations."""

#     def __init__(self, q):
#         self.q = q
#         self.alphabet = string.printable

# class RandomSwapPerturbation(Perturbation):

#     """Implementation of random swap perturbations.
#     See `RandomSwapPerturbation` in lines 1-5 of Algorithm 2."""

#     def __init__(self, q):
#         super(RandomSwapPerturbation, self).__init__(q)

#     def __call__(self, s):
#         list_s = list(s)
#         sampled_indices = random.sample(range(len(s)), int(len(s) * self.q / 100))
#         for i in sampled_indices:
#             list_s[i] = random.choice(self.alphabet)
#         return ''.join(list_s)

# class RandomPatchPerturbation(Perturbation):

#     """Implementation of random patch perturbations.
#     See `RandomPatchPerturbation` in lines 6-10 of Algorithm 2."""

#     def __init__(self, q):
#         super(RandomPatchPerturbation, self).__init__(q)

#     def __call__(self, s):
#         list_s = list(s)
#         substring_width = int(len(s) * self.q / 100)
#         max_start = len(s) - substring_width
#         start_index = random.randint(0, max_start)
#         sampled_chars = ''.join([
#             random.choice(self.alphabet) for _ in range(substring_width)
#         ])
#         list_s[start_index:start_index+substring_width] = sampled_chars
#         return ''.join(list_s)

# class RandomInsertPerturbation(Perturbation):

#     """Implementation of random insert perturbations.
#     See `RandomPatchPerturbation` in lines 11-17 of Algorithm 2."""

#     def __init__(self, q):
#         super(RandomInsertPerturbation, self).__init__(q)

#     def __call__(self, s):
#         list_s = list(s)
#         sampled_indices = random.sample(range(len(s)), int(len(s) * self.q / 100))
#         for i in sampled_indices:
#             list_s.insert(i, random.choice(self.alphabet))
#         return ''.join(list_s)

import random
import string
from collections import Counter

class Perturbation:

    """Base class for random perturbations."""

    def __init__(self, q):
        self.q = q
        self.alphabet = string.printable

    def summarize(self, s):
        """Simple summarization function based on keyword frequency.
        This returns a summary by keeping the most frequent words in the text."""
        
        # Tokenize the input string into words
        words = s.split()

        # Get the frequency of each word
        word_counts = Counter(words)
        
        # Sort words by frequency (most common first)
        most_common_words = [word for word, _ in word_counts.most_common(len(words) // 2)]
        
        # Reconstruct the summary from the most common words
        summary = ' '.join(most_common_words)
        
        return summary


class RandomSwapPerturbation(Perturbation):

    """Implementation of random swap perturbations with semantic summarization.
    See `RandomSwapPerturbation` in lines 1-5 of Algorithm 2."""

    def __init__(self, q):
        super(RandomSwapPerturbation, self).__init__(q)

    def __call__(self, s):
        # Apply Random Swap Perturbation
        list_s = list(s)
        sampled_indices = random.sample(range(len(s)), int(len(s) * self.q / 100))
        for i in sampled_indices:
            list_s[i] = random.choice(self.alphabet)
        perturbed_string = ''.join(list_s)
        
        # Apply Summarization on the perturbed result
        summarized_string = self.summarize(perturbed_string)
        
        return summarized_string


class RandomPatchPerturbation(Perturbation):

    """Implementation of random patch perturbations.
    See `RandomPatchPerturbation` in lines 6-10 of Algorithm 2."""

    def __init__(self, q):
        super(RandomPatchPerturbation, self).__init__(q)

    def __call__(self, s):
        list_s = list(s)
        substring_width = int(len(s) * self.q / 100)
        max_start = len(s) - substring_width
        start_index = random.randint(0, max_start)
        sampled_chars = ''.join([
            random.choice(self.alphabet) for _ in range(substring_width)
        ])
        list_s[start_index:start_index+substring_width] = sampled_chars
        return ''.join(list_s)


class RandomInsertPerturbation(Perturbation):

    """Implementation of random insert perturbations.
    See `RandomInsertPerturbation` in lines 11-17 of Algorithm 2."""

    def __init__(self, q):
        super(RandomInsertPerturbation, self).__init__(q)

    def __call__(self, s):
        list_s = list(s)
        sampled_indices = random.sample(range(len(s)), int(len(s) * self.q / 100))
        for i in sampled_indices:
            list_s.insert(i, random.choice(self.alphabet))
        return ''.join(list_s)




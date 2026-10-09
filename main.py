"""First step: load a corpus and explore its characters."""
"""

AI agents were used to assist the production of this code.
core implrementation(s) remains the work of the author.
"""

from pathlib import Path


CORPUS_PATH = Path(__file__).parent / "data" / "corpus.txt"

text = CORPUS_PATH.read_text(encoding="utf-8")
print(text)

# TODO: Build a sorted list of its unique characters.
# Pseudocode:
#   collect each distinct character from text (only once)
#   sort those characters into a predictable order
#   save the result as sorted_list
sorted_list = sorted(text)

#print(sorted_list) # for understanding purposes

# TODO: Build both character-to-integer and integer-to-character dictionaries.
# Pseudocode:
#   for each character and its position in chars:
#       store character -> position in char_to_int
#       store position -> character in int_to_char
char_to_int = {char: idx for idx, char in enumerate(set(sorted_list))}
int_to_char = {idx: char for char, idx in char_to_int.items()}

# TODO: Encode a sample string, decode it, and verify it matches exactly.
# Pseudocode:
#   choose a sample made only from characters in the corpus
#   replace each sample character with its integer ID
#   replace each integer ID with its character
#   check that the decoded string equals the original sample
test_string = "what is the meaning of life"
encode = [char_to_int[char] for char in test_string]
decode = "".join(int_to_char[idx] for idx in encode)
# below for testing
"""

# -----------------------------------------------------------------------------
# BIGRAM MODEL: use neighboring characters to learn which character tends to
# come next. Fill in these steps one at a time.
# -----------------------------------------------------------------------------

# TODO: Encode the entire corpus as integer IDs.
# Pseudocode:
#   create an empty list called encoded_text
#   for each character in text:
#       look up its ID in char_to_int
#       append that ID to encoded_text
encoded_text = for char in text:
    encoded_text.append(char_to_int[char])

# TODO: Count every adjacent-character pair (bigram).
# Pseudocode:
#   create a counter for pairs, starting all counts at zero
#   for each position i where both text[i] and text[i + 1] exist:
#       current_char = text[i]
#       next_char = text[i + 1]
#       increase the count for (current_char, next_char) by one
#   (Or do this with encoded_text, using neighboring integer IDs.)
count = 0
while

# TODO: Put the pair counts into a square count table.
# Pseudocode:
#   make a table with one row and one column for every character ID
#   initialize every cell to zero
#   for each counted pair (current_char, next_char):
#       find their integer IDs
#       put that pair's count in the corresponding row and column
#   a row represents the current character; a column represents the next one

# TODO: Convert counts into next-character probabilities.
# Pseudocode:
#   for each row in the count table:
#       add the counts in that row to get its total
#       if the total is greater than zero:
#           divide each count in the row by the total
#   each resulting row should sum to about 1

# TODO: Generate text from the learned bigram probabilities.
# Pseudocode:
#   choose a starting character ID
#   repeat for the desired number of characters:
#       use the current character's probability row to choose a next ID
#       append that ID to the generated sequence
#       make that next ID the current ID
#   convert the generated IDs back to characters with int_to_char
#   join the characters together and print the generated text

# TODO: Check the model's behavior.
# Pseudocode:
#   generate several samples and inspect whether they look plausible
#   try a few different starting characters and sample lengths
#   optionally compare generated bigram frequencies with corpus frequencies
print(f"Original: {test_string}")
print(f"Encoded: {encode}")
print(f"Decoded: {decode}")
"""

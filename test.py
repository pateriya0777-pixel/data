# from collections import Counter

# def find_anagrams(input_string):
#     # A small sample dictionary. In a real app, you'd load a full word list.
#     dictionary = ["race", "dog", "cat", "acted", "care", "racecar", "dogged", "cared"]
    
#     # Normalize the input
#     input_string = input_string.lower()
#     input_counts = Counter(input_string)
    
#     found_words = []
    
#     for word in dictionary:
#         word_counts = Counter(word)
#         # Check if the word can be built using the available letters
#         # all() ensures every letter in the word exists in the input with enough frequency
#         if all(word_counts[char] <= input_counts[char] for char in word_counts):
#             found_words.append(word)
            
#     return found_words

# # Your specific string
# my_string = "caredogcat"
# results = find_anagrams(my_string)

# print(f"Words found in '{my_string}':")
# print(results)



s = "zeoro one two three four five six seven eight"
sp = s.split()
li = []
for i in range(len(sp)-1):

    if i % 2 == 0:
        li.append(sp[i])
    else:
        li.append(sp[i][::-1])
print(li)

sentence = "the cat sat on the mat the cat"

freq = {}
for word in sentence.split():
    freq[word] = freq.get(word, 0) + 1

print(freq)
def word_frequency(text):
    freq = {}
    words = text.split()
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq
text = input("Enter text:")
print(word_frequency(text))
    
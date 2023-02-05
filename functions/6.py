def func(sentence):
    words = sentence.split()
    words.reverse()
    return ' '.join(words)
inp = input()
print(func(inp))
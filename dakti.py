def dak(words):
    words = words.split()
    line = sorted(words, key =lambda word: sorted(word))
    lines = [''.join([char for char in word if not char.isdigit()]) for word in line]
    print(' '.join(lines))
size = int(input())
for _ in range(size):
    words = input()
    dak(words)

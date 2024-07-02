def countLetters(text):
    letters = {}
    for c in text:
        c = c.lower()
        if c.isalpha():
            letters[c] = letters.get(c, 0) + 1
    return letters

with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    print("--- Begin report of books/frankenstein.txt ---")
    print("{count} words found in the document".format(count=len(file_contents)))
    print("\n")
    lettersCounts = list(countLetters(file_contents).items())
    letterCounts = sorted(lettersCounts, key= lambda i : i[1], reverse=True)
    for c, n in letterCounts:
            print("The '{c}' character was found {n} times".format(c=c, n=n))
    print("--- End report ---")

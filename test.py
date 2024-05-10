
def isPrefixOfWord(sentence: str, searchWord: str) -> int:
    arr = sentence.split()
    n = len(searchWord)
    for i in range(len(arr)):
        s = arr[i]
        if len(s) >= n and searchWord == s[:n]:
            return i + 1
    return -1

sentence = "i love eating burger"
searchWord = "burg"
print(isPrefixOfWord(sentence,searchWord))
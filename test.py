

arr = ["app","apple","hello","abc","d"]
arr.sort(key=lambda x:(len(x),x))
print(arr)


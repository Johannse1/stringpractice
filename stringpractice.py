#evan Johanns
#2/6
# string practice

words = str(input("please enter words with commas between, no spaces:"))

print("there are ",len(words), "characters in this string.")
print("the first letter of the string is " , words[0])
print("the last letter of the string is " , words[-1])
print("the third letter of the string is " , words[2])
print("the string capitalized looks like this" , words.upper())
print("the string title cased looks like this " , words.title())
print("is this alpha?:")
print(words.isalpha())
y = words.split(",")
print(y)
print(words.zfill(50))


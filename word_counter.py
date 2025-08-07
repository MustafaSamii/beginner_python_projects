

with open ("sample.txt", "r") as file:
    file_text = file.read()
    words = file_text.split()

word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print (f"Word count: {word_count}")
    

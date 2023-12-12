sentence = input("Sentence: ")
sentence = sentence.strip()

print('?' in sentence)

print(sentence.find("?"))

if sentence[-1] == "?":
    print("It is a question")
else:
    print('It is not a question')

if sentence.endswith("?"):
    print("It is a question")
else:
    print('It is not a question')

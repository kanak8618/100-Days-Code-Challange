# Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].

subject = ["I", "You"]
verb = ["Play", "Love"]
objects = ["Hockey","Football"]
sentences = []

for sub in subject:
    for ver in verb:
        for obj in objects:
            sentence = f"{sub} {ver} {obj}"
            sentences.append(sentence)

for sentence in sentences:
    print(sentence)
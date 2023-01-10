def spin_words(sentence):
    text = sentence.split(" ")
    result = ""
    for word in text:
        if len(word) < 5:
            result += word + " "
        else:
            result += word[::-1]+" "
        x=list(result)
        x.pop()
        x="".join(x)
    return x


print(spin_words("Welcome to Codewars"))

def removeNames(message):
    recievers = []
    strippedMessage = []
    word_list = message.split(" ")
    for word in word_list:
        if word[0] == "@":
            recievers.append(word[1:])
        strippedMessage.append(word)
    print(f"Recievers: {recievers}")
    print(f"Message: {' '.join(strippedMessage)}")

removeNames(input("Enter message: "))

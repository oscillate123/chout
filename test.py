def findRecievers(message):
    recievers = []
    word_list = message.split(" ")
    for word in word_list:
        if word[0] == "@":
            recievers.append(word[1:])
    return recievers


message = input("Enter message: ")
recievers = findRecievers(message)
print(f"Recievers: {recievers}")
print(f"message: {message}")
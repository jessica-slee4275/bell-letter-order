word1 = raw_input("Enter word1: ")
word2 = raw_input("Enter word2: ")
def stringEquals():
    if word1 == word2:
        return 'false'
    if len(word1) != len(word2):
        return 'false'
    for letter1 in word1:
        temp_result = 'false'
        for letter2 in word2:
            if(letter1 == letter2):
                temp_result = 'true'
        if(temp_result == 'false'):
                return 'false'
    return 'true'
print(stringEquals())

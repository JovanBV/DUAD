my_word = input('Write a word that will be spelled backwards: ')

for i in range(len(my_word)-1, -1, -1):
    print(my_word[i])

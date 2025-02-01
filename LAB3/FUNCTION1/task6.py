# def reverse_words():
#     words = input("Введите предложение: ").split()  # Ввод и разбиение на слова
#     print(" ".join(words[::-1]))  # Переворот слов и вывод

# reverse_words()

def reverse_words():
    words = input("Enter a sentence: ").split()
    newlist = ""
    for word in words[::-1]:
        newlist += word + " "
    print(newlist.strip())   # strip() ---> removes the extra space at the end.

reverse_words()
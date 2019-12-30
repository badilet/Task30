# Напишите функцию которая определит сколько раз встречаеться элемент в списке.

def count_element():
    text = input("Enter a word or text: ")
    element = input("Which element do you want to count?: ")

    a = [i for i in text if element in text]
    num_element = a.count(element)
    print(num_element)

count_element()

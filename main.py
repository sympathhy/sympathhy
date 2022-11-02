def text_lower(text):
    return text.lower()

def length_text(text):
    print("Вызов функции length_text")
    return len(text)


if __name__ == '__main__':
    n = 'ПЕРВЫЙ РЕПОЗИТОРИЙ НА ГИТЕ'
    print(text_lower(n))
    print(length_text(n))
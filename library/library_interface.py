from library.library_functions import del_book, library_load_from_json, library_load_to_json, search_book


def input_my(k: int):
    s = input(f'Введите число от 1 до {k}:\n')
    while s.isdigit() is False or (int(s) <= 0 or int(s) > k):
        s = input(f'Не верно. Введите число от 1 до 4:\n')
    return int(s)


def menu():
    print(f'Выберете дествие\n')
    print(f'1) Добавить книгу\n')
    print(f'2) Удалить книгу\n')
    print(f'3) Найти книгу\n')


def add_():
    new_book = {'name': input(f'Введите название книги\n'), 'year': input(f'Введите год издания книги\n'),
                'pages': input(f'Введите колличество страниц в книге\n'), 'author': input(f'Введите автора книги\n')}
    library = library_load_from_json('books.json')
    number = str(len(library) + 1)
    library[number] = new_book
    library_load_to_json('books.json', library)


def del_():
    number = int(input(f'Введите номер книги для удаления\n'))
    del_book('books.json', number)


def search_():
    print(f'Выберете параметр, по которому нужно искать книгу\n')
    print(f'1) Название\n')
    print(f'2) Год\n')
    print(f'3) Колличество страниц\n')
    print(f'4) Автор\n')
    param_search = input_my(4)
    if param_search == 1:
        print(search_book('books.json', name=input(f'Введите название книги\n'), year=None, pages=None, author=None))
    elif param_search == 2:
        print(search_book('books.json', name=None, year=input(f'Введите год издания книги\n'), pages=None, author=None))
    elif param_search == 3:
        print(search_book('books.json', name=None, year=None, pages=input(f'Введите колличество страниц книги\n'),
                          author=None))
    elif param_search == 4:
        print(search_book('books.json', name=None, year=None, pages=None, author=input(f'Введите автора книги\n')))


def main():
    library = library_load_from_json('books.json')
    print(f'Книги в библиотеке\n')
    print(library)
    menu()

    command = input_my(3)
    if command == 1:
        add_()
    elif command == 2:
        del_()
    elif command == 3:
        search_()


if __name__ == '__main__':
    main()

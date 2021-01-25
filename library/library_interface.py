import re
from library.library_functions import del_book, library_load_from_json, library_load_to_json, search_book, edit_book


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
    print(f'4) Редактировать книгу\n')


def menu_for_search():
    print(f'Выберете параметр, по которому нужно искать книгу\n')
    print(f'1) Название\n')
    print(f'2) Год\n')
    print(f'3) Колличество страниц\n')
    print(f'4) Автор\n')


def menu_for_edit():
    print(f'Выберете параметр для редактирования\n')
    print(f'1) Название\n')
    print(f'2) Год издания\n')
    print(f'3) Колличество страниц\n')
    print(f'4) Автор книги\n')


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
    library = library_load_from_json('books.json')
    i = 0
    menu_for_search()
    param_search = input_my(4)
    if param_search == 1:
        name = input(f'Введите название книги\n')
        print(search_book('books.json', name))
    elif param_search == 2:
        year = input(f'Введите год издания книги\n')
        print(search_book('books.json', year))
    elif param_search == 3:
        pages = input(f'Введите колличество страниц книг\n')
        print(search_book('books.json', pages))
    elif param_search == 4:
        author = input(f'Введите автора книги\n')
        print(search_book('books.json', author))


def edit_():
    library = library_load_from_json('books.json')
    print(f'Введите номер книги для редактирования\n')
    number_book = input_my(len(library))
    menu_for_edit()
    param_number = input_my(4)
    if (number_book == 1 and param_number == 1) or (number_book == 2 and param_number == 1) or \
            (number_book == 3 and param_number == 1) or (number_book == 4 and param_number == 1):
        print(edit_book('books.json', number=number_book, name=input(f'Введите новое название книги\n'),
                        year=None, pages=None, author=None))
    elif (number_book == 1 and param_number == 2) or (number_book == 2 and param_number == 2) \
            or (number_book == 3 and param_number == 2) or (number_book == 4 and param_number == 2):
        print(edit_book('books.json', number=number_book, name=None, year=input(f'Введите год издания книги\n'),
                        pages=None, author=None))
    elif (number_book == 1 and param_number == 3) or (number_book == 2 and param_number == 3) \
            or (number_book == 3 and param_number == 3) or (number_book == 4 and param_number == 3):
        print(edit_book('books.json', number=number_book, name=None, year=None,
                        pages=input(f'Введите колличество страниц книги\n'), author=None))
    elif (number_book == 1 and param_number == 4) or (number_book == 2 and param_number == 4) \
            or (number_book == 3 and param_number == 4) or (number_book == 4 and param_number == 4):
        print(edit_book('books.json', number=number_book, name=None, year=None, pages=None,
                        author=input(f'Введите автора книги\n')))
    p = input(f'Продолжить редактирование? Y/N:\n').capitalize()
    if re.search('Y/*', p):
        return edit_()
    else:
        return print(f'Изменения сохранены\n')


def main():
    library = library_load_from_json('books.json')
    print(f'Книги в библиотеке\n')
    print(library)
    menu()

    command = input_my(4)
    if command == 1:
        add_()
    elif command == 2:
        del_()
    elif command == 3:
        search_()
    elif command == 4:
        edit_()


if __name__ == '__main__':
    main()

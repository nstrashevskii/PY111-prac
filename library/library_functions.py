import json


def library_load_from_json(lib: json) -> dict:
    """
    загрузка библиотеки из файла json
    :param lib: файл библиотеки
    :return: словарь с библиотекой из файла
    """
    with open(lib, 'r') as f:
        library: dict = json.load(f)
    return library


def library_load_to_json(lib: json, library: dict) -> json:
    """
    загрузка библиотеки в файла json
    :param library: словарь с библиотекой
    :param lib: файл библиотеки
    :return: файла json с библиотекой из словаря
    """
    with open(lib, 'w') as f:
        json.dump(library, f, indent=4)
    return lib


def del_book(lib: json, number: int) -> json:
    """
    :param lib: файл библиотеки
    :param number: номер книги для удаления
    :return: новый файл библиотеки, после удаления книги
    """
    new_key = 0
    new_library = {}
    library = library_load_from_json(lib)
    del library[str(number)]
    for key, value in library.items():
        new_key += 1
        new_library[new_key] = value
    new_lib = library_load_to_json(lib, new_library)
    return new_lib


def search_book(lib: json, name: (str, None) = None, year: (int, None) = None,
                pages: (int, None) = None, author: (str, None) = None) -> (dict, None):
    library = library_load_from_json(lib)
    library_new = {}
    if name is not None:
        for key, value in library.items():
            for key_, value_ in value.items():
                if name == value_:
                    library_new[key] = library[key]
    elif year is not None:
        for key, value in library.items():
            for key_, value_ in value.items():
                if year == value_:
                    library_new[key] = library[key]
    elif pages is not None:
        for key, value in library.items():
            for key_, value_ in value.items():
                if pages == value_:
                    library_new[key] = library[key]
    elif author is not None:
        for key, value in library.items():
            for key_, value_ in value.items():
                if author == value_:
                    library_new[key] = library[key]
    return library_new


def edit_book(lib: json, number: int, name: (str, None), year: (int, None), pages: (int, None), author: (str, None))\
        -> json:
    library = library_load_from_json(lib)
    book = library[str(number)]
    if name is not None:
        book["name"] = name
    elif year is not None:
        book["year"] = year
    elif pages is not None:
        book["pages"] = pages
    elif author is not None:
        book["author"] = author

    library[str(number)] = book
    return library_load_to_json(lib, library)

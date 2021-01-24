import json


def library_load_from_json(lib: json) -> dict:
    with open(lib, 'r') as f:
        library = json.load(f)
    return library


def library_load_to_json(lib: json, library: dict) -> json:
    with open(lib, 'w') as f:
        json.dump(library, f, indent=4)
    return lib


def del_book(lib: json, number: int) -> json:
    new_key = 0
    new_library = {}
    library = library_load_from_json(lib)
    del library[str(number)]
    for key, value in library.items():
        new_key += 1
        new_library[new_key] = value
    new_lib = library_load_to_json(lib, new_library)
    return new_lib


def get_key(val_):
    library = library_load_from_json('books.json')
    for key, value in library.items():
        for key_, value_ in value.items():
            if val_ == value_:
                return key
    return "book doesn't not exist"


def search_book(lib: json, name: (str, None), year: (int, None), pages: (int, None), author: (str, None))\
        -> (dict, None):
    library = library_load_from_json(lib)
    if name is not None:
        return library[get_key(name)]
    elif year is not None:
        return library[get_key(year)]
    elif pages is not None:
        return library[get_key(pages)]
    elif author is not None:
        return library[get_key(author)]
    else:
        return None

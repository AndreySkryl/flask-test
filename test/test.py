import json
import os
import re


def slugify(s: str) -> str:
    modified_s = re.sub(r'[^\w+]', '-', s.lower())
    modified_s = re.sub(r'-+', '-', modified_s)

    dic = {'ь': '', 'ъ': '', 'а': 'a', 'б': 'b', 'в': 'v',
           'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh',
           'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l',
           'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
           'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h',
           'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'sch', 'ы': 'yi',
           'э': 'e', 'ю': 'yu', 'я': 'ya'}
    table = str.maketrans(dic)
    modified_s = modified_s.translate(table)

    if modified_s.startswith('-'):
        modified_s = modified_s[1:]
    if modified_s.endswith('-'):
        modified_s = modified_s[:-1]

    return modified_s


def main():
    category_names = ['Масла и автохимия', 'Шины и диски', 'Автоэлектроника']
    filename = 'spare_parts.json'
    slugs = []
    for category_name in category_names:
        full_filename = os.path.join('..', 'data', 'categories', category_name, filename)
        if os.path.isfile(full_filename):
            with open(full_filename, 'rt', encoding='utf-8') as json_file:
                json_spare_parts = json.load(json_file)
                slugs.extend([json_spare_part['title'] for json_spare_part in json_spare_parts])
                slugs.append('')

    tests = category_names[:]
    tests.append('')
    tests.extend(slugs)

    for test in tests:
        slug = slugify(test)
        if slug:
            print(f'test("{test}") -> slug("{slug}")')
        else:
            print()


if __name__ == '__main__':
    main()

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
    tests = [
        'двигате,./a/',
        'коленвал',
        'asdaq   woo        '
    ]

    for test in tests:
        res = slugify(test)
        print(f'test("{test}") -> res("{res}")')


if __name__ == '__main__':
    main()

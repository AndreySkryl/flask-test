import re


def slugify(slug: str) -> str:
    slug = re.sub(r'[^\w+]', '-', slug.lower())
    slug = re.sub(r'-+', '-', slug)

    dic = {'ь': '', 'ъ': '', 'а': 'a', 'б': 'b', 'в': 'v',
           'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh',
           'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l',
           'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
           'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h',
           'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'sch', 'ы': 'yi',
           'э': 'e', 'ю': 'yu', 'я': 'ya'}
    table = str.maketrans(dic)
    slug = slug.translate(table)

    if slug.startswith('-'):
        slug = slug[1:]
    if slug.endswith('-'):
        slug = slug[:-1]

    return slug

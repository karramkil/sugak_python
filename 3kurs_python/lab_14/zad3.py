def transliterate_char(char):
    translit_dict = {
        'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E',
        'Ж': 'ZH', 'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M',
        'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U',
        'Ф': 'F', 'Х': 'KH', 'Ц': 'TC', 'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH',
        'Ы': 'Y', 'Ъ': '', 'Ь': '', 'Э': 'E', 'Ю': 'IU', 'Я': 'IA',
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e',
        'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'i', 'к': 'k', 'л': 'l', 
        ...
    }
    return translit_dict.get(char, char)

def transliterate_text(text):
    return ''.join(transliterate_char(char) for char in text)

text = input("Введите текст на русском: ")
transliterated_text = transliterate_text(text)
print("Транслитерированный текст: ", transliterated_text)

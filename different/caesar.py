text = input('Введите ваш текст: \n')
def caesar_list(text):
    '''Преобразует текст в список из слов и символов'''
    text.replace('', '')
    caesat_list_ = []
    res = ''
    for e in text:
        if e.isalpha():
            res += e
        else:
            caesat_list_.append(res)
            caesat_list_.append(e)
            res = ''
    caesat_list_.append(res)
    while '' in caesat_list_:
        caesat_list_.remove('')
    return caesat_list_
def caesar_cipher(text):
    '''Шифрует текст модернезированным шифром Цезаря'''
    letters ='abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    for e in caesar_list(text):
        if e.isalpha():
            word = ''
            shift = len(e)
            for l in e:
                word += letters[(letters.index(l)+shift)]
            result += word
        else:
            result += e
    return result.strip()


print(caesar_cipher(text))
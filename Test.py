import re

dic = {
    'S': ['aaSb','Sa',''],
}

answers = set()


def possiblities(word, lim):
    if (len(word) > lim):
        return

    match = re.search('[S]', word)
    if match:
        for i in list(word):
            if i == 'S':
                for j in dic.get(i):
                    possiblities(word.replace(i, j), lim)
    else:
        if word not in answers:
            answers.add(word)


possiblities(dic.get('S')[0-2],8)
for i in answers:
    print(i)
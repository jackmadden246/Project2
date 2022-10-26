import re


def change_format(paragraph):
    result = re.findall('[0-9]{3}[-]{1}[0-9]{2}[-]{1}[0-9]{4}', paragraph)
    print(result)
    for num in result:
        split_1 = num.split('-')
        split_1 = str(f'{split_1[0]}/{split_1[2]}/{split_1[1]}')
        paragraph = re.sub(num, split_1, paragraph)
    return paragraph


print(change_format('Please quote your policy number: 112-39-8552.'))

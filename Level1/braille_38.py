from bs4 import BeautifulSoup
import requests

webpage_response = requests.get('https://en.wikipedia.org/wiki/Braille_ASCII#:~:text=Braille%20ASCII%20(or%20more%20formally,combinations%20in%20six%2Ddot%20Braille.')
soup = BeautifulSoup(webpage_response.content, 'html.parser')

l1 = [i.text.rstrip() for table in soup('table', class_='wikitable') for i in table.select('tr > td:nth-of-type(2)')]
l2 = [i.text.rstrip() for table in soup('table', class_='wikitable') for i in table.select('tr > td:nth-of-type(3)')]
dict1 = {x: y for (x, y) in zip(l1, l2)}
# print(dict1)
dict1[' '] = dict1.pop('(space)')
# print(dict1)
for k, v in dict1.items():
    dict1[k] = ''.join([y for x, y in enumerate(v, 1) if x % 2 == 1]+[y for x, y in enumerate(v, 1) if x % 2 == 0])
print(dict1)


# test1 = '011011'
#
# print(''.join([y for x, y in enumerate(test1, 1) if x % 2 == 1]+[y for x, y in enumerate(test1, 1) if x % 2 == 0]))


def braille(word):
    output = ''
    for letter in word:
        if letter.isupper():
            output += '000001'
        output += dict1[letter.upper()]
    return output


v1 = braille('The quick brown fox jumps over the lazy dog')
v2 = '000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110'

print(v1)
print(v2)
print(v1 == v2)

'''test_lst = [[1, 2, 3], [4, 5, 6]]
flat = [x for y in test_lst for x in y]
print(*flat)'''
# dict = {}
# # for table in soup.find('table', class_='wikitable'):
# for row in soup('table', class_='wikitable')('tr'):
#     print(row)
#         # dict[tr.text.rstrip('\n')] = tr.find_next_sibling('td').text.rstrip('\n')
# print(dict)

    # for td in tr.find_all('td', limit=2):
    #     print(td.text)
# letters = [td.find_all('td', limit=2) for tr in main_table.find_all('tr') for td in tr]
# print(*letters)
# print(main_table.prettify())
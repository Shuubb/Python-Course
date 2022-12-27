
str1 = "es aris satesto stringi aeiou"

xmovnebi = ['a', 'e', 'i', 'o', 'u']

for x in xmovnebi:
    str1 = str1.replace(x, '$')

print('\n', str1, '\n')
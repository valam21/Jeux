width = int(input('Entrez la largeur : '))
height = int(input('Entrez la hauteur : '))

for y in range(height):
    line = ''
    if y == 0 or y == height - 1:
        if width > 0:
            line += '+'
        line += '-' * (width - 2)
        if width > 1:
            line += '+'
"""    else:
        if width > 0:
            line += '|'
        line += ' ' * (width - 2)
        if width > 1:
            line += '|'
    print(line)

height = int(input('Entrez la hauteur : '))
max_len = 2 * height - 1
width = 1

for y in range(height):
    padding = (max_len - width) // 2
    line = ' ' * padding

    if width > 2 and y != height - 1:
        line += '*' + ' ' * (width - 2) + '*'
    else:
        line += '*' * width
    print(line)
    width += 2
"""
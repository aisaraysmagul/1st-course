prefixes='JKLMNOPQ'
suffix='ack'
for letter in prefixes[::-1]:
    if letter=='O' or letter=='Q':
        print(letter+'u'+suffix, end=' ')
    else:
        print(letter+suffix, end=' ')


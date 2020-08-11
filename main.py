import operator


def word_counter():
    """
    Count the word in a text file and output the result in another text file
    :return:
    """
    print('=================================================================')
    filename = input('Enter the name of the text file to count: ')
    output = input('Enter the name of the file to save the word count result: ')
    print('Working...')

    counts = dict()
    junk_characters = '`~@#$%^&*()-_=+/?.>,<""'';:{[}]'

    with open(filename, 'r') as f:
        lines = f.readlines()
        f.close()

    for line in lines:
        new_line = str()
        for character in line:
            if character not in junk_characters:
                new_line += character.lower()
            else:
                continue
        words = new_line.split(' ')
        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1

    try:
        del counts[""]
        counts["I"] = counts["i"]
        counts["I'm"] = counts["i'm"]
        counts["I'll"] = counts["i'll"]
        counts["I've"] = counts["i've"]
        counts["I'd"] = counts["i'd"]
        del counts["i"]
        del counts["i'm"]
        del counts["i'll"]
        del counts["i've"]
        del counts["i'd"]

    except KeyError:
        pass

    sort = sorted(counts.items(), key=operator.itemgetter(1))
    sort.reverse()

    with open(output, 'w') as o:
        for item in sort:
            o.write(item[0] + ' ' + str(item[1]) + '\n')
        o.close()

    print('Done writing the file' + output)

    print('=================================================================')


word_counter()


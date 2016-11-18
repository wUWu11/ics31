
#-------F---------
l = [ "Four score and seven years ago, our fathers brought forth on",
  "this continent a new nation, conceived in liberty and dedicated",
  "to the proposition that all men are created equal.  Now we are",
  "   engaged in a great 		civil war, testing whether that nation, or any",
  "nation so conceived and so dedicated, can long endure.        " ]

#-------F1---------
def print_line_numbers(a:'list of strings'):
    '''print out each string preceded by a line number
    '''
    for i in range(len(a)):
        print("{:<5d}:{} ".format(i+1,l[i]))
        
print_line_numbers(l)

#-------F2---------

def stats(a:'list of strings'):
    '''takes a list of strings and prints statistics '''
    num_of_lines = len(a)
    num_of_empty_lines = 0
    num_of_chara = 0
    for i in a:
        i = i.strip()
        print(i)
        num_of_chara += len(i)
        if len(i) == 0:
            num_of_empty_lines += 1
    print('{:<6}'.format(num_of_lines),  'lines in the list')
    print('{:<6}'.format(num_of_empty_lines),   'empty lines')
    print('{:<6}'.format(num_of_chara/num_of_lines) ,"average characters per line")
    print('{:<6}'.format(num_of_chara/(num_of_lines-num_of_empty_lines)),'average characters per non-empty')     

stats(l)
#-------F3---------
def list_of_words(a:'list of strings')->'list of strings':
    ''' takes a list of strings as above and returns a list of individual words
        with all white space and punctuation removed (except for apostrophes/single quotes
    '''
    result = []
    table = str.maketrans('",./<>?[]{}:;~!@\t\n','                  ')
    for i in a:
        i = i.translate(table)
        i = i.replace(' ','')
        i = i.lstrip()
        for n in i:
            result.append(n)
    return result

print(list_of_words(l))




# given a list of string, finding "similar" string of them
# similar means the distance of all character pair in the string is the same


input = ['ababab', 'cdcdcd', 'abc', 'cdf', 'a', 'b', 'ba', 'kj']




def main(lst):
    table = {}
    for st in lst:
        key = ''
        f = ord(st[0])   # get the int coressponding to the first char

        for char in st:  # convert the string into the distance of each char with the first char    
            key += str(ord(char)-f) 

        if key not in table:  # each value of the hash table is a list
            table[key] = [st]  # create a new list in case there is no
        else:
            table[key].append(st)  # append the similar string into existing group
    return list(table.values())


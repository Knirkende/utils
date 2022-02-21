"""
A script that checks the solution to a (small cardinality) set closure problem.
"""

def make_tex(arr):
    """
    accepts a set of tuples and returns a .tex formatted set of tuples.
    """
    pairs_per_line = 13
    counter = 0
    tex_str = '$\\{'
    for pair in arr:
        tex_str += '\\langle ' + str(pair[0]) + ', ' + str(pair[1]) + '\\rangle, '
        counter += 1
        if counter == pairs_per_line:
            tex_str += ' \\\\ '
            counter = 0
    return tex_str + '\\}$'

def transitive_closure(arr):
    """
    returns True if one change was made to arr.
    returns False if no changes were made to arr.
    """
    for pair in arr:
        for second in arr:
            # if a two-step path is found, and a one-step path is not found, add one-step path
            if (pair != second) and (pair[1] == second[0]) and (tuple((pair[0], second[1])) not in arr):
                arr.add(tuple((pair[0], second[1])))
                return True
    return False

def create_closure(arr, func):
    """
    creates the closure of arr under function func in-place.
    repeatedly calls function until no changes have been made.
    """
    change = True
    while change:
        change = func(arr)

if __name__ == '__main__':
    my_arr = {(1, 2), (2, 3), (3, 4)}
    #create_closure(my_arr, transitive_closure)
    #expected: {(1, 2), (2, 3), (1, 3)}
    #print(my_arr)
    my_arr = {
        ('o', 'l'),
        ('l', 'st'),
        ('st', 'o'),
        ('sk', 'd'),
        ('sk', 'so'),
        ('sk', 'o'),
        ('d', 'so'),
        ('y', 'b'),
        ('y', 'st'),
    }
    create_closure(my_arr, transitive_closure)
    print(my_arr)
    my_solution = {
        ('o', 'l'),
        ('l', 'st'),
        ('st', 'o'),
        ('sk', 'd'),
        ('sk', 'so'),
        ('sk', 'o'),
        ('d', 'so'),
        ('y', 'b'),
        ('y', 'st'),
        ('sk', 'l'),
        ('sk', 'st'),
        ('o', 'st'),
        ('st', 'st'),
        ('o', 'o'),
        ('l', 'o'),
        ('l', 'l'),
        ('y', 'o'),
        ('y', 'l'),
        ('st', 'l')
    }
    diff = my_arr ^ my_solution
    print(diff) #empty set? Success!
    print(make_tex(my_arr))
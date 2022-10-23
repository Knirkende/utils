from copy import deepcopy

def find_clause(inp: set) -> set:
    for clause in inp:
        for other_clause in inp:
            for atom in clause:
                for other_atom in other_clause:
                    if (other_atom == 'NOT ' + atom):
                        clause_cp = set(deepcopy(clause))
                        other_cp = set(deepcopy(other_clause))
                        other_cp.remove(other_atom)
                        clause_cp.remove(atom)
                        new_clause = clause_cp.union(other_cp)
                        new_clause = frozenset(new_clause)
                        if new_clause not in inp:
                            return new_clause
    return None

def expand_expression(inp: set) -> set:
    new_clause = find_clause(inp)
    new_set = deepcopy(inp)
    while new_clause is not None:
        print(tex_generator(new_set))
        new_set.add(new_clause)
        new_clause = find_clause(new_set)
    return new_set

def tex_generator(inp: set) -> str:
    tex_str = r'$\{'
    for clause in inp:
        clause_str = '('
        for atom in clause:
            clause_str += atom.replace('NOT', r'\neg') + ', '
        clause_str = clause_str[:-2]
        clause_str += '), '
        tex_str += clause_str
    tex_str = tex_str[:-2]
    tex_str += r'\}$\par'
    return tex_str

if __name__ == '__main__':
    ex = {
        frozenset({'NOT q', 'p'}),
        frozenset({'NOT p', 'q'}),
        frozenset({'NOT p'}),
        frozenset({'NOT q', 'r'}),
        frozenset({'NOT r'}),
    }
    ex2 = {
        frozenset({'NOT p', 'q'}),
        frozenset({'NOT r', 'q'}),
        frozenset({'q', 'NOT r'}),
        frozenset({'NOT p', 'r', 'NOT q'}),
    }

    ex3 = {
        frozenset({'NOT p', 'q', 'r'}),
        frozenset({'NOT q', 'p'}),
        frozenset({'NOT r', 'p'}),
        frozenset({'q', 'NOT r'}),
        frozenset({'NOT q', 'NOT p'}),
        frozenset({'NOT p'}),
    }
    ex4 = {
        frozenset({'r', 'NOT q'}),
        frozenset({'NOT p', 'NOT q'}),
        frozenset({'NOT r', 'p'}),
        frozenset({'p', 'NOT r', 'r'}),
        frozenset({'q', 'NOT p'}),
    }
    thing = expand_expression(ex4)
    print(len(thing))

    test = {frozenset({'NOT s', 'r', 'NOT p', 'p'}), frozenset({'NOT r', 'q', 's', 'NOT p'}), frozenset({'NOT p', 'NOT s', 'q', 's', 'p'})}
    #print(tex_generator(test))
    #print(thing)
    #print(len(thing))
    #print(tex_generator(thing))

    #(p, q, \neg p), (\neg q, q, \neg p)
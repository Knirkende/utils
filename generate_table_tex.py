def generate_compound():
    """ Generates some .tex code to speed up setting up truth tables. """
    comp = []
    while (expr:=input('Add part of expression, blank to end: ')) != '':
        comp.append(generate_atomic(expr))
    return ' & '.join(comp)

def generate_atomic(expr):
    tokens = {
        'and': '\\land',
        'or': '\\lor',
        'not': '\\neg',
        '->': '\\rightarrow'
    }
    for key, val in tokens.items():
        expr = expr.replace(key, val)
    return '$' + expr + '$'     

if __name__ == '__main__':
    print(generate_compound())
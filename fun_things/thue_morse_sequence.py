def flip_bits(seq: str) -> str:
    """
    flips the bits of seq and returns a string representation
    of the resulting binary number.
    """
    # exclusive or of 1, 1 = 0; 0, 1 = 1, so do xor of each bit and 1
    mask = int(('1' * len(seq)), 2)
    result = (bin(int(seq, 2) ^ mask)).replace('0b', '')
    leading = len(seq) - len(result)
    result = ('0' * leading) + result
    return result

def t_m_sequence(z: int, n: str) -> str:
    """
    returns the inductively defined Thue-Morse sequence to z steps.
    let T be a set such that x E T, and if X E T, X!X E T
    """
    print(n)
    if z < 1:
        return n
    return n + t_m_sequence(z - 1, n + flip_bits(n))

if __name__ == '__main__':
    print(t_m_sequence(5, '1'))
    
    """
    1
    01
    01 10
    0110 1001
    01101001 10010110
    """
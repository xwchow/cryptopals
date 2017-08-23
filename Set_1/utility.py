import codecs
import unittest
import string


def hex_decode(hex_str):
    """
    (hex str) -> bytes
    """
    return codecs.decode(hex_str, 'hex')


def hex_to_base64(hex_str):
    """
    (hex str) -> base64 str
    """
    return codecs.encode(hex_decode(hex_str), 'base64')


def xor_of_buffers(str_1, str_2):
    """
    (bytes, bytes) -> hex str
    """
    # padding
    n = len(str_1)
    m = len(str_2)
    if n < m:
        str_1, str_2 = str_2, str_1
        n, m = m, n
    str_2 += ((n - m) // m) * str_2
    str_2 += str_2[:(n - m) % m]

    xor_val = int(str_1, 16) ^ int(str_2, 16)
    ans = '{:x}'.format(xor_val)
    return '0' * (n - len(ans)) + ans


def repeat_key_xor(message, key):
    n, m = len(message), len(key)
    result = []
    for i in range(n):
        byte = ord(message[i]) ^ ord(key[i % m])
        result.append('{:02x}'.format(byte))
    return ''.join(result)


def scoring_function(S):
    letters = "ETAOIN SHRDLU"
    scores = [x for x in range(len(letters), 0, -1)]

    score = 0
    for ch in S:
        if ch not in string.printable:
            return -1
        if ch.upper() in letters:
            score += scores[letters.index(ch.upper())]
    return score


def popcount(x):
    return bin(x).count('1')


def hamming_distance(A, B):
    """
    (str, str) -> int
    Returns the hamming distance between strings A and B.
    """
    assert len(A) == len(B), 'lengths of 2 strings are not equal.'

    distance = sum(popcount(ord(x) ^ ord(y)) for x, y in zip(A, B))
    return distance


class TestUtilityFunctions(unittest.TestCase):
    def test_hamming_distance(self):
        act = hamming_distance('this is a test', 'wokka wokka!!!')
        exp = 37
        self.assertEqual(act, exp)


if __name__ == '__main__':
    unittest.main(exit=False)

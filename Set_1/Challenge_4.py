import utility


def best_guess(bytes_line):
    """
    (byte str) -> float, byte str
    """
    max_score = None
    answer = None

    for guess in range(256):
        bytes_xor = utility.repeat_key_xor(bytes_line, bytes([guess]))

        score = utility.score_english(bytes_xor)
        if score is not None and (max_score is None or score > max_score):
            max_score = score
            answer = bytes_xor

    return max_score, answer


if __name__ == '__main__':
    with open('4.txt', 'r') as fin:
        max_score = None
        answer = None

        for hexs_line in fin:
            hexs_line = hexs_line.rstrip()
            score, ans = best_guess(utility.hex_decode(hexs_line))
            if score and (max_score is None or score > max_score):
                max_score = score
                answer = ans

        if max_score is not None:
            print(
                'Score is {}.\nDecoded string = {}'.format(max_score, answer))

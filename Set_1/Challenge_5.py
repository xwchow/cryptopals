import utility

stanza = '''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''

key = 'ICE'

expected = (b'0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a262263'
            b'24272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b2028'
            b'3165286326302e27282f')

actual = utility.hex_encode(
    utility.repeat_key_xor(stanza.encode(), key.encode()))

assert actual == expected, 'Act = {}\nExp = {}'.format(actual, expected)

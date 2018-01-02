from utils import *

def cipher_tests():
    assert(cipher(0, 'a') == 'a')
    assert(cipher(0, 'A') == 'A')
    assert(cipher(3, 'D') == 'G')
    assert(cipher(10, 'e') == 'o')
    assert(cipher(4, 'z') == 'd')
    assert(cipher(3, 'Z') == 'C')

def encode_tests():
    assert(encode('hi', key=1) == 'ij')
    assert(encode("oh hai!", key=5) == 'tm mfn!')
    assert(encode(" ") == " ")


def all_tests():
    print("Running cipher tests...")
    cipher_tests()
    print("Running encode tests...")
    encode_tests()
    print("All tests passed!")

all_tests()

import numpy as np
import random
from bitstring import BitArray
from functools import reduce

def transmission_error(data):
    """
    Randomly choose to introduce a single bit error
    """

    bad_data = []
    for b in data:
        new_b = b
        if random.random() > 0.5:
            new_b[random.randint(0,6)] ^= 1
        
        bad_data.append(new_b)
    return bad_data

def ham_enc_7_4(data):
    """
    (7,4)-hamming code

    Encodes given bytes with a Hamming code
    """

    dlen = len(data)    # length of data
    elen = 4            # bits per encode

    nout = (dlen // elen)
    output = []

    gMatr = np.array([
        [1, 0, 0, 0, 1, 1, 0],
        [0, 1, 0, 0, 0, 1, 1],
        [0, 0, 1, 0, 1, 0, 1],
        [0, 0, 0, 1, 1, 1, 1]
    ])

    for i in range(nout):
        d = np.array(data[i*elen : i*elen + elen])
        if d.shape[0] != 4:
            padding = np.array([0] * ( 4 - len(d) ))
            np.append(d, padding)
        
        output.append(np.dot(d, gMatr) % 2)

    return output

# Decoder
with open("flag.txt", 'rb') as f:
    flag = f.read().strip()

flag_bits = BitArray(flag)
tx = ham_enc_7_4(flag_bits)
rx = transmission_error(tx)
rx = list(map(lambda a: BitArray(a), rx))
v = BitArray(reduce(lambda a,b: a + b, rx))

with open("tes.txt", 'wb') as f:
    v.tofile(f)

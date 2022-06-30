# 
# Fast discrete cosine transform algorithms (Python)
# 
# Copyright (c) 2020 Project Nayuki. (MIT License)
# https://www.nayuki.io/page/fast-discrete-cosine-transform-algorithms
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
# - The above copyright notice and this permission notice shall be included in
#   all copies or substantial portions of the Software.
# - The Software is provided "as is", without warranty of any kind, express or
#   implied, including but not limited to the warranties of merchantability,
#   fitness for a particular purpose and noninfringement. In no event shall the
#   authors or copyright holders be liable for any claim, damages or other
#   liability, whether in an action of contract, tort or otherwise, arising from,
#   out of or in connection with the Software or the use or other dealings in the
#   Software.
# 

import math
import numpy as np


def transform(vector):
    v0 = vector[0] + vector[7]
    v1 = vector[1] + vector[6]
    v2 = vector[2] + vector[5]
    v3 = vector[3] + vector[4]
    v4 = vector[3] - vector[4]
    v5 = vector[2] - vector[5]
    v6 = vector[1] - vector[6]
    v7 = vector[0] - vector[7]
    
    v8 = v0 + v3
    v9 = v1 + v2
    v10 = v1 - v2
    v11 = v0 - v3
    v12 = -v4 - v5
    v13 = (v5 + v6) * A[3]
    v14 = v6 + v7
    
    v15 = v8 + v9
    v16 = v8 - v9
    v17 = (v10 + v11) * A[1]
    v18 = (v12 + v14) * A[5]
    
    v19 = -v12 * A[2] - v18
    v20 = v14 * A[4] - v18
    
    v21 = v17 + v11
    v22 = v11 - v17
    v23 = v13 + v7
    v24 = v7 - v13
    
    v25 = v19 + v24
    v26 = v23 + v20
    v27 = v23 - v20
    v28 = v24 - v19

    return [
        v15,
        2 * S[1] * v26,
        2 * S[2] * v21,
        2 * S[3] * v28,
        2 * S[4] * v16,
        2 * S[5] * v25,
        2 * S[6] * v22,
        2 * S[7] * v27,
    ]

# DCT type III, scaled. A straightforward inverse of the forward algorithm.
def inverse_transform(vector):
    v15 = vector[0]
    v26 = vector[1] / S[1] / 2
    v21 = vector[2] / S[2] / 2
    v28 = vector[3] / S[3] / 2
    v16 = vector[4] / S[4] / 2
    v25 = vector[5] / S[5] / 2
    v22 = vector[6] / S[6] / 2
    v27 = vector[7] / S[7] / 2
    
    v19 = (v25 - v28) / 2
    v20 = (v26 - v27) / 2
    v23 = (v26 + v27) / 2
    v24 = (v25 + v28) / 2
    
    v7  = (v23 + v24) / 2
    v11 = (v21 + v22) / 2
    v13 = (v23 - v24) / 2
    v17 = (v21 - v22) / 2
    
    v8 = (v15 + v16) / 2
    v9 = (v15 - v16) / 2
    
    v18 = (v19 - v20) * A[5]  # Different from original
    v12 = (v19 * A[4] - v18) / (A[2] * A[5] - A[2] * A[4] - A[4] * A[5])
    v14 = (v18 - v20 * A[2]) / (A[2] * A[5] - A[2] * A[4] - A[4] * A[5])
    
    v6 = v14 - v7
    v5 = v13 / A[3] - v6
    v4 = -v5 - v12
    v10 = v17 / A[1] - v11
    
    v0 = (v8 + v11) / 2
    v1 = (v9 + v10) / 2
    v2 = (v9 - v10) / 2
    v3 = (v8 - v11) / 2
    
    return [
        (v0 + v7) / 2,
        (v1 + v6) / 2,
        (v2 + v5) / 2,
        (v3 + v4) / 2,
        (v3 - v4) / 2,
        (v2 - v5) / 2,
        (v1 - v6) / 2,
        (v0 - v7) / 2,
    ]
# ---- End of Source code ----
# ---- New code ----
def dct_ref(vector):
    dct_vector = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(8):
        dct_vector[0] = dct_vector[0] + vector[i]
        dct_vector[1] = dct_vector[1] + vector[i] * math.cos(math.pi / 16 * (2 * i + 1))
        dct_vector[2] = dct_vector[2] + vector[i] * math.cos(math.pi / 16 * (2 * i + 1) * 2)
        dct_vector[3] = dct_vector[3] + vector[i] * math.cos(math.pi / 16 * (2 * i + 1) * 3)
        dct_vector[4] = dct_vector[4] + vector[i] * math.cos(math.pi / 16 * (2 * i + 1) * 4)
        dct_vector[5] = dct_vector[5] + vector[i] * math.cos(math.pi / 16 * (2 * i + 1) * 5)
        dct_vector[6] = dct_vector[6] + vector[i] * math.cos(math.pi / 16 * (2 * i + 1) * 6)
        dct_vector[7] = dct_vector[7] + vector[i] * math.cos(math.pi / 16 * (2 * i + 1) * 7)
    return dct_vector


def transform_As_Verilog(vector, sigbit):   # sigbit: significant bits
    S_fix_bef_round = np.multiply(S, math.pow(2, sigbit + 1))
    A_fix_bef_round = np.multiply(A[1:], math.pow(2, sigbit))
    S_fix = np.round(S_fix_bef_round)
    A_fix = np.round(A_fix_bef_round)

    v00 = vector[0] + vector[7]
    v01 = vector[1] + vector[6]
    v02 = vector[2] + vector[5]
    v03 = vector[3] + vector[4]
    v04 = vector[3] - vector[4]
    v05 = vector[2] - vector[5]
    v06 = vector[1] - vector[6]
    v07 = vector[0] - vector[7]
    
    v08 = v00 + v03
    v09 = v01 + v02
    v10 = v01 - v02
    v11 = v00 - v03
    v12 = -v04 - v05
    v13 = round((v05 + v06) * A_fix[2] / math.pow(2, sigbit))
    v14 = v06 + v07
    
    v15 = v08 + v09
    v16 = v08 - v09
    v17 = round((v10 + v11) * A_fix[0] / math.pow(2, sigbit))
    v18 = round((v12 + v14) * A_fix[4] / math.pow(2, sigbit))
    
    v19 = round(-v12 * A_fix[1] / math.pow(2, sigbit) - v18)
    v20 = round(v14 * A_fix[3] / math.pow(2, sigbit) - v18)
    
    v21 = v17 + v11
    v22 = v11 - v17
    v23 = v13 + v07
    v24 = v07 - v13
    
    v25 = v19 + v24
    v26 = v23 + v20
    v27 = v23 - v20
    v28 = v24 - v19

    # print(v15/8)

    return [
        v15,
        round((int(S_fix[1] * v26)) >> (sigbit)),
        round((int(S_fix[2] * v21)) >> (sigbit)),
        round((int(S_fix[3] * v28)) >> (sigbit)),
        round((int(S_fix[4] * v16)) >> (sigbit)),
        round((int(S_fix[5] * v25)) >> (sigbit)),
        round((int(S_fix[6] * v22)) >> (sigbit)),
        round((int(S_fix[7] * v27)) >> (sigbit)),
    ]


C = [math.cos(math.pi / 16 * i) for i in range(8)]
S = [1 / (4 * val) for val in C]
S[0] = 1 / (2 * math.sqrt(2))
A = [
    None,
    C[4],
    C[2] - C[6],
    C[4],
    C[6] + C[2],
    C[6],
]
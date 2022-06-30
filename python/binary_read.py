import numpy as np
import math

def read_txt_binary(filename, bits, mode):
    f_data = open(filename, 'r')
    i = 0
    data_bin_txt = np.zeros(65536)
    data_bin_txt = f_data.read().splitlines()
    # while True:
    #     data[i] = f_data.readline()
    #     if not data[i]:
    #         break
    #     i += 1
    f_data.close()
    
    data = np.zeros(65536)
    for i in range(65536):
        # print(str(data_bin_txt[i]))
        # print(int(str(data_bin_txt[i]), base=2))
        data[i] = int(str(data_bin_txt[i]), base=2)
        if data[i] > math.pow(2, bits-1):
            data[i] -= math.pow(2, bits)

    data_np_8x8x1024 = np.zeros(shape=(8,8,1024))
    if mode == 0:   # for 1d dct test
        for j in range(1024):
            for k in range(8):
                for l in range(8):
                    data_np_8x8x1024[k, l, j] = data[l + k*8 + j*64]
                    if l == 0:
                        data_np_8x8x1024[k, l, j] *= 2
    elif mode == 1: # for 2d dct test
        for j in range(1024):
            for k in range(8):
                for l in range(8):
                    data_np_8x8x1024[k, l, j] = data[l + k*8 + j*64]
                    if l == 0:
                        data_np_8x8x1024[k, l, j] *= 2
                    if k == 0:
                        data_np_8x8x1024[k, l, j] *= 2
    return data_np_8x8x1024

out = read_txt_binary("data_2d_out.txt", 12, 1)
print(out[0,0,1023])
# print(out[0,:,0])
# print(out[7,:,1023])
# print(np.min(out[:,1,:]))
# print(np.min(out[:,2,:]))
# print(np.min(out[:,3,:]))
# print(np.min(out[:,4,:]))
# print(np.min(out[:,5,:]))
# print(np.min(out[:,6,:]))
# print(np.min(out[:,7,:]))

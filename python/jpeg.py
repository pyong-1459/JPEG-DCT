import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import fastdct8
import binary_read
import math


image = Image.open("Lenna.png").resize((256,256))
# plt.imshow(image)
# plt.show()
imgData = np.asarray(image)
# print(image.mode)
# print(image.size)
# print(imgData.size)
newImageArray = np.round(np.dot(imgData[:,:,:3], [0.2126, 0.7152, 0.0722]))
newImageArray -= 128
newImageArray_8x8 = np.zeros(shape=(8, 8, 1024))
for i in range(32): # col of chunks
    for j in range(32): # row of chunks
        for k in range(8): # row
            idx_row = j*8 + k
            idx_col = i*8
            newImageArray_8x8[k, :, i*32 + j] = newImageArray[idx_row, idx_col:idx_col+8]
# print(newImageArray_8x8[1, :, 0])

# text file generation
# f_img = open("data1.txt", 'w')
# f_raw = open("data_raw.txt", 'w')
# for kk in range(1024):
#     for ii in range(8):
#         for jj in range(8):
#             data = int(newImageArray_8x8[ii, jj, kk])
#             if data < 0:
#                 data += 256
#             data_bin = f'{data:08b}'
#             f_raw.write(str(data) + " ")
#             f_img.write(data_bin + "\n")
#         f_raw.write("\n")
# f_img.close()
# f_raw.close()
# generation end

def dct_1d_1(newImg_8x8x1024):
    newImg_dct_1d = np.zeros(shape=(8, 8, 1024))
    # newImg_dct_1d_trans = np.zeros(shape=(8, 8, 1024))
    for m in range(1024):
        for l in range(8):
            newImg_dct_1d[l, :, m] = fastdct8.transform(newImg_8x8x1024[l, :, m])
    newImg_dct_1d_trans = np.transpose(newImg_dct_1d, (1, 0, 2))
    return newImg_dct_1d_trans

def dct_1d_v(newImg_8x8x1024, sigbits):
    newImg_dct_1d = np.zeros(shape=(8, 8, 1024))
    # newImg_dct_1d_trans = np.zeros(shape=(8, 8, 1024))
    for m in range(1024):
        for l in range(8):
            newImg_dct_1d[l, :, m] = fastdct8.transform_As_Verilog(newImg_8x8x1024[l, :, m], sigbits)
    newImg_dct_1d_trans = np.transpose(newImg_dct_1d, (1, 0, 2))
    return newImg_dct_1d_trans

# newImg_dct1_1d = np.zeros(shape=(8, 8, 1024))
# newImg_dct2_1d = np.zeros(shape=(8, 8, 1024))
# newImg_dct1_1d_trans = np.zeros(shape=(8, 8, 1024))
# newImg_dct2_1d_trans = np.zeros(shape=(8, 8, 1024))
# for m in range(1024):
#     for l in range(8):
#         newImg_dct1_1d[l, :, m] = fastdct8.transform(newImageArray_8x8[l, :, m])
#         newImg_dct2_1d[l, :, m] = fastdct8.transform_As_Verilog(newImageArray_8x8[l, :, m], 3)
newImg_dct3_1d = binary_read.read_txt_binary("data_1d_out.txt", 10, 0)
newImg_dct1_1d_trans = dct_1d_1(newImageArray_8x8)
newImg_dct2_1d_trans = dct_1d_v(newImageArray_8x8, 3)
newImg_dct3_1d_trans = np.transpose(newImg_dct3_1d, (1, 0, 2))

# print(newImg_dct2_1d_trans[3,0,0:64] 
#     - newImg_dct3_1d_trans[3,0,0:64])
# print(newImg_dct2_1d_trans[1:8,0,2])
# print(newImg_dct3_1d_trans[1:8,0,2])
print(newImg_dct3_1d_trans[1,:,0])
# print(fastdct8.transform_As_Verilog([21, 23, 23, 21, 23, 24, 24, 26], 3))
# print(newImg_dct1_1d_trans[0,0,256:256+256] 
#     - newImg_dct3_1d_trans[0,0,256:256+256])
# print(newImg_dct1_1d_trans[0,0,512:512+256] 
#     - newImg_dct3_1d_trans[0,0,512:512+256])
# print(newImg_dct1_1d_trans[0,0,768:768+256] 
#     - newImg_dct3_1d_trans[0,0,768:768+256])
maxs1d = np.max(newImg_dct2_1d_trans)
maxwithAC = newImg_dct2_1d_trans[1:7, :, :]
maxs1dAC = np.max(maxwithAC)
mins1dAC = np.min(maxwithAC)
# print(maxs1dAC)
# print(mins1dAC)

# newImg_dct1_2d = np.zeros(shape=(8, 8, 1024))
# newImg_dct2_2d = np.zeros(shape=(8, 8, 1024))
# # newImg_dct1_2d_trans = np.zeros(shape=(8, 8, 1024))
# # newImg_dct2_2d_trans = np.zeros(shape=(8, 8, 1024))
# for n in range(1024):
#     for o in range(8):
#         newImg_dct1_2d[o, :, n] = fastdct8.transform(newImg_dct1_1d_trans[o, :, n])
#         newImg_dct2_2d[o, :, n] = fastdct8.transform_As_Verilog(newImg_dct2_1d_trans[o, :, n], 3)
newImg_dct1_2d_trans = dct_1d_1(newImg_dct1_1d_trans)
newImg_dct2_2d_trans = dct_1d_v(newImg_dct2_1d_trans, 3)
newImg_dct3_2d_trans = dct_1d_v(newImg_dct3_1d_trans, 3)
newImg_dct4_2d_trans = binary_read.read_txt_binary("data_2d_out.txt", 12, 1)
# print(newImg_dct3_2d_trans[7,:,1023])

print(newImg_dct3_2d_trans[0,0,0:64] 
    - newImg_dct4_2d_trans[0,0,0:64])
print(newImg_dct3_2d_trans[0:8,0,1023])
print(newImg_dct4_2d_trans[0:8,0,1023])
print(newImg_dct3_2d_trans[0,:,1023])

# maxs2dAC = np.min(newImg_dct3_2d_trans[1:7,:,:])
# print(maxs2dAC)
# ---- dct end ----
quant_matrix = np.array([[16, 11, 10, 16, 24,  40,  51,  61],
                         [12, 12, 14, 19, 26,  58,  60,  55],
                         [14, 13, 16, 24, 40,  57,  69,  56],
                         [14, 17, 22, 29, 51,  87,  80,  62],
                         [18, 22, 37, 56, 68,  109, 103, 77],
                         [24, 35, 55, 64, 81,  104, 113, 92],
                         [49, 64, 78, 87, 103, 121, 120, 101],
                         [72, 92, 95, 98, 112, 100, 103, 99]])

# add verilog output

# verilog output added

newImg_quant1_bef_round = np.zeros(shape=(8, 8, 1024))
newImg_quant2_bef_round = np.zeros(shape=(8, 8, 1024))
newImg_quant3_bef_round = np.zeros(shape=(8, 8, 1024))
newImg_quant4_bef_round = np.zeros(shape=(8, 8, 1024))
for p in range(1024):
    newImg_quant1_bef_round[:, :, p] = np.divide(newImg_dct1_2d_trans[:, :, p], quant_matrix)
    newImg_quant2_bef_round[:, :, p] = np.divide(newImg_dct2_2d_trans[:, :, p], quant_matrix)
    newImg_quant3_bef_round[:, :, p] = np.divide(newImg_dct3_2d_trans[:, :, p], quant_matrix)
    newImg_quant4_bef_round[:, :, p] = np.divide(newImg_dct4_2d_trans[:, :, p], quant_matrix)
newImg_quant1 = np.round(newImg_quant1_bef_round)
newImg_quant2 = np.round(newImg_quant2_bef_round)
newImg_quant3 = np.round(newImg_quant3_bef_round)
newImg_quant4 = np.round(newImg_quant4_bef_round)

newImg_dequant1 = np.zeros(shape=(8, 8, 1024))
newImg_dequant2 = np.zeros(shape=(8, 8, 1024))
newImg_dequant3 = np.zeros(shape=(8, 8, 1024))
newImg_dequant4 = np.zeros(shape=(8, 8, 1024))
for x in range(1024):
    newImg_dequant1[:, :, x] = np.multiply(newImg_quant1[:, :, x], quant_matrix)
    newImg_dequant2[:, :, x] = np.multiply(newImg_quant2[:, :, x], quant_matrix)
    newImg_dequant3[:, :, x] = np.multiply(newImg_quant3[:, :, x], quant_matrix)
    newImg_dequant4[:, :, x] = np.multiply(newImg_quant4[:, :, x], quant_matrix)

# newImg_dequant1_trans = np.transpose(newImg_dequant1, (1, 0, 2))
# newImg_dequant2_trans = np.transpose(newImg_dequant2, (1, 0, 2))

def Idct_1d_1(newImg_8x8x1024):
    newImg_Idct_1d = np.zeros(shape=(8, 8, 1024))
    for q in range(1024):
        for r in range(8):
            newImg_Idct_1d[r, :, q] = fastdct8.inverse_transform(newImg_8x8x1024[r, :, q])
    newImg_Idct_1d_trans = np.transpose(newImg_Idct_1d, (1, 0, 2))
    return newImg_Idct_1d_trans

# newImg_Idct1_1d = np.zeros(shape=(8, 8, 1024))
# newImg_Idct2_1d = np.zeros(shape=(8, 8, 1024))
# for q in range(1024):
#     for r in range(8):
#         newImg_Idct1_1d[r, :, q] = fastdct8.inverse_transform(newImg_dequant1[r, :, q])
#         newImg_Idct2_1d[r, :, q] = fastdct8.inverse_transform(newImg_dequant2[r, :, q])
newImg_Idct1_1d_trans = Idct_1d_1(newImg_dequant1)
newImg_Idct2_1d_trans = Idct_1d_1(newImg_dequant2)
newImg_Idct3_1d_trans = Idct_1d_1(newImg_dequant3)
newImg_Idct4_1d_trans = Idct_1d_1(newImg_dequant4)

# newImg_Idct1_2d = np.zeros(shape=(8, 8, 1024))
# newImg_Idct2_2d = np.zeros(shape=(8, 8, 1024))
# for s in range(1024):
#     for t in range(8):
#         newImg_Idct1_2d[t, :, s] = fastdct8.inverse_transform(newImg_Idct1_1d_trans[t, :, s])
#         newImg_Idct2_2d[t, :, s] = fastdct8.inverse_transform(newImg_Idct2_1d_trans[t, :, s])
newImg_Idct1_2d_trans = Idct_1d_1(newImg_Idct1_1d_trans)
newImg_Idct2_2d_trans = Idct_1d_1(newImg_Idct2_1d_trans)
newImg_Idct3_2d_trans = Idct_1d_1(newImg_Idct3_1d_trans)
newImg_Idct4_2d_trans = Idct_1d_1(newImg_Idct4_1d_trans)

# ---- image restore ----
newImg_restore1 = np.zeros(shape=(256, 256))
newImg_restore2 = np.zeros(shape=(256, 256))
newImg_restore3 = np.zeros(shape=(256, 256))
newImg_restore4 = np.zeros(shape=(256, 256))
for u in range(8): # row
    for v in range(32):
        for w in range(32):
            restore_row = u + v*8
            restore_col = w * 8
            newImg_restore1[restore_row, restore_col:restore_col+8] = newImg_Idct1_2d_trans[u, :, w*32 + v]
            newImg_restore2[restore_row, restore_col:restore_col+8] = newImg_Idct2_2d_trans[u, :, w*32 + v]
            newImg_restore3[restore_row, restore_col:restore_col+8] = newImg_Idct3_2d_trans[u, :, w*32 + v]
            newImg_restore4[restore_row, restore_col:restore_col+8] = newImg_Idct4_2d_trans[u, :, w*32 + v]

newImg_restore1 = newImg_restore1.astype('int')
newImg_restore2 = newImg_restore2.astype('int')
newImg_restore3 = newImg_restore3.astype('int')
newImg_restore4 = newImg_restore4.astype('int')

newImg_restore1 += 128
newImg_restore2 += 128
newImg_restore3 += 128
newImg_restore4 += 128
newImageArray += 128

newImg1 = Image.fromarray(newImg_restore1)
newImg2 = Image.fromarray(newImg_restore2)
newImg3 = Image.fromarray(newImg_restore3)
newImg4 = Image.fromarray(newImg_restore4)

def MSE_PSNR(ref, img):
    MSE = 0
    for y in range(256):
        for z in range(256):
            MSE += math.pow((ref[y,z] - img[y,z]), 2)
    MSE = MSE / 65536
    PSNR = 10 * math.log10(65536 / MSE)
    return PSNR

# MSE1 = 0
# for y in range(256):
#     for z in range(256):
#         MSE1 += math.pow((newImageArray[y,z] - newImg_restore1[y,z]), 2)
# MSE1 = MSE1 / 65536
# PSNR1 = 10 * math.log10(65536 / MSE1)
PSNR1 = MSE_PSNR(newImageArray, newImg_restore1)

# MSE2 = 0
# for y in range(256):
#     for z in range(256):
#         MSE2 += math.pow((newImageArray[y,z] - newImg_restore2[y,z]), 2)
# MSE2 = MSE2 / 65536
# PSNR2 = 10 * math.log10(65536 / MSE2)
PSNR2 = MSE_PSNR(newImageArray, newImg_restore2)
PSNR3 = MSE_PSNR(newImageArray, newImg_restore3)
PSNR4 = MSE_PSNR(newImageArray, newImg_restore4)

print(PSNR1)
print(PSNR2)
print(PSNR3)
print(PSNR4)

rows = 1
cols = 4

ax1 = plt.subplot(rows, cols, 1)
ax1.imshow(newImg1)
ax1.set_xlabel('ref')
ax1.set_xticks([]), ax1.set_yticks([])

ax2 = plt.subplot(rows, cols, 2)
ax2.imshow(newImg2)
ax2.set_xlabel('mine')
ax2.set_xticks([]), ax2.set_yticks([])

ax3 = plt.subplot(rows, cols, 3)
ax3.imshow(newImg3)
ax3.set_xlabel('verilog')
ax3.set_xticks([]), ax3.set_yticks([])

ax4 = plt.subplot(rows, cols, 4)
ax4.imshow(newImg4)
ax4.set_xlabel('verilog-final')
ax4.set_xticks([]), ax4.set_yticks([])

plt.show()

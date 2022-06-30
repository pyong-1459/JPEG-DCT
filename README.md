# JPEG-DCT
DCT implement with Verilog and Python

## Python files
Mainly works at jpeg.py

jpeg.py에서 돌아감
### jpeg.py
#### code flow
DCT -> Quantization -> Dequantization -> IDCT -> image plot

Test four cases of DCT - Normal DCT, Verilog-like DCT, Verilog 1d DCT output, Verilog 2d DCT output

4가지 DCT를 수행함 - 일반 DCT, python에서 돌아가는 Verilog-like DCT, 베릴로그 1d DCT 출력, 베릴로그 2d DCT 출력

##### Each PSNR of DCT results:
40.30, 34.00, 34.17, 34.27

Quantization으로 손실 압축 구현

### fastdct8.py
https://www.nayuki.io/page/fast-discrete-cosine-transform-algorithms

Algorithms at the link used to implement DCT. 

해당 링크에서 알고리즘 참고함

Input data text file generation included at line 27~41. That used at Verilog simulation

27~41줄에 베릴로그를 위한 입력 벡터 파일을 만드는 코드 포함됨. 주석처리되어 있음.

#### Added code
Transform like verilog(integer implementation) added. 

DCT를 정수 연산으로 구현한 Transform like Verilog가 추가됨

In Verilog, there are no coded with IDCT, so inverse transform with verilog not included.

베릴로그 파일은 DCT만 구현했기 때문에, IDCT를 python으로 구현하지는 않아 integer inverse transform 코드는 없음.

#### Changed point
transform return result multiplied by 2

일반적인 DCT 결과값과 같게 하기 위해 스케일링 제거(2를 곱함)

inverse transform input divied by 2

IDCT에 스케일링을 위해 입력 값을 2로 나눔
### binary_read.py
Code with reading binary text file

2진수 텍스트 파일을 읽는 코드

Handle the data from verilog

베릴로그에서 출력된 데이터를 다룸

## Verilog files
### dct_1d.v
Implement the first 1-dimensional DCT

첫번째 1d DCT 구현
### tb_dct_1d.v
1d DCT verification code

첫 DCT 동작을 확인하기 위한 테스트벤치

Generate a text file with binary value

이진수 텍스트 파일 생성됨
### dct_2d.v
Implement the second 1-demensional DCT

두번째 1d DCT 구현
### tp_mem.v
Transpose memory implementation
### tb_tp_mem.v
Tests tp_mem module

tp_mem 모듈 테스트벤치

제대로 돌아가는지 실험하는 코드
### dct_top.v
Two 1d DCT modules included

transpose memory module included
### tb_dct_top.v
Tests entire DCT computation

전체 DCT 연산 테스트벤치

Generate a text file with binary value

2진수 텍스트 파일 생성됨

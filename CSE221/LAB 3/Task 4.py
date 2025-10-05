MOD = 10**9 + 7

def mat_mult(A, B):
     return [
         [
             (A[0][0]*B[0][0] + A[0][1]*B[1][0]) % MOD,
             (A[0][0]*B[0][1] + A[0][1]*B[1][1]) % MOD
         ],
         [
             (A[1][0]*B[0][0] + A[1][1]*B[1][0]) % MOD,
             (A[1][0]*B[0][1] + A[1][1]*B[1][1]) % MOD
         ]
     ]

def mat_pow(A, power):
     result = [[1, 0], [0, 1]]
     while power > 0:
         if power % 2 == 1:
             result = mat_mult(result, A)
         A = mat_mult(A, A)
         power //= 2
     return result

T = int(input())
for _ in range(T):
     a11, a12, a21, a22 = map(int, input().split())
     X = int(input())
     A = [[a11, a12], [a21, a22]]
     AX = mat_pow(A, X)
     print(AX[0][0], AX[0][1])
     print(AX[1][0], AX[1][1])
def fib_fast(n: int) -> int:
    def matmul(A, B):
        return (
            A[0] * B[0] + A[1] * B[2],
            A[0] * B[1] + A[1] * B[3],
            A[2] * B[0] + A[3] * B[2],
            A[2] * B[1] + A[3] * B[3],
        )

    def matpow(M, n):
        result = (1, 0, 0, 1)  # identity matrix
        while n > 0:
            if n % 2 == 1:
                result = matmul(result, M)
            M = matmul(M, M)
            n //= 2
        return result

    if n <= 0:
        return 0
    M = (1, 1, 1, 0)
    r = matpow(M, n - 1)
    return r[0]
import timeit

setup = "from __main__ import fib_fast"
def longest_word_checker(txt: str, l: list) -> bool:
    is_longest = all(len(txt) >= len(word) for word in l)

    if not is_longest:
        print(f"{txt} is not the longest word in {' '.join(l)}")

    l.append(txt)
    return is_longest

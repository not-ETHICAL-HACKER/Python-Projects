#If the number is even, divide it by 2.
#If the number is odd, multiply it by 3 and add 1.
def collatz_sequence(n:int)->tuple[list[int],int]:
    """
    The function `collatz_sequence` generates a Collatz sequence starting from a given number and
    returns the sequence along with the number of iterations taken to reach 1.
    
    :param n: The function `collatz_sequence` takes an integer `n` as input and generates a Collatz
    sequence starting from that number. The Collatz sequence is generated based on the following rules:
    :type n: int
    :return: The function `collatz_sequence` returns a tuple containing two elements:
    1. A list of integers representing the Collatz sequence starting from the input number `n`.
    2. An integer representing the number of iterations taken to reach the value 1 in the Collatz
    sequence.
    """
    seq:list[int]=[]
    seq.append(n)
    iter:int=0
    while True:
        if n%2==0:
            n//=2
        elif n%2==1:
            n=3*n+1    
        iter+=1
        seq.append(n)
        if 1 == n:
            return seq,iter
print(collatz_sequence(2**32-1)[0])
import argparse
import math
import sys
from typing import Generator, Iterable, List

#!/usr/bin/env python3
"""
Prime number generator utilities.

Usage examples:
    python anime.py                # prints first 10 primes
    python anime.py --count 20     # prints first 20 primes
    python anime.py --limit 100    # prints primes <= 100
    python anime.py --range 50 150 # prints primes in [50,150]
"""



def is_prime(n: int) -> bool:
        if n < 2:
                return False
        if n in (2, 3):
                return True
        if n % 2 == 0:
                return False
        r = int(math.isqrt(n))
        i = 3
        while i <= r:
                if n % i == 0:
                        return False
                i += 2
        return True


def prime_generator(start: int = 2) -> Generator[int, None, None]:
        """Infinite prime generator starting at >= start. Uses incremental trial division."""
        if start <= 2:
                yield 2
                candidate = 3
        else:
                candidate = start if start % 2 == 1 else start + 1
                # if candidate is 2 (start==2 handled), otherwise candidate is odd
        primes: List[int] = [2]
        # If starting above 3, seed primes list with known primes up to sqrt(candidate).
        # We'll grow the primes list on the fly.
        while True:
                if candidate == 3 and 3 not in primes:
                        primes.append(3)
                is_p = True
                r = int(math.isqrt(candidate))
                for p in primes:
                        if p > r:
                                break
                        if candidate % p == 0:
                                is_p = False
                                break
                if is_p:
                        primes.append(candidate)
                        if candidate >= start:
                                yield candidate
                candidate += 2


def first_n_primes(n: int) -> List[int]:
        if n <= 0:
                return []
        gen = prime_generator(2)
        out = []
        for _ in range(n):
                out.append(next(gen))
        return out


def primes_upto(limit: int) -> List[int]:
        if limit < 2:
                return []
        gen = prime_generator(2)
        out = []
        for p in gen:
                if p > limit:
                        break
                out.append(p)
        return out


def primes_in_range(a: int, b: int) -> List[int]:
        if b < a:
                a, b = b, a
        if b < 2:
                return []
        start = max(2, a)
        gen = prime_generator(start)
        out = []
        for p in gen:
                if p > b:
                        break
                if p >= start:
                        out.append(p)
        return out


def main(argv: Iterable[str]) -> int:
        parser = argparse.ArgumentParser(prog="anime.py", description="Prime number generator")
        group = parser.add_mutually_exclusive_group()
        group.add_argument("-c", "--count", type=int, help="print first COUNT primes")
        group.add_argument("-l", "--limit", type=int, help="print primes <= LIMIT")
        group.add_argument("-r", "--range", nargs=2, type=int, metavar=("START", "END"), help="print primes in [START,END]")
        parser.add_argument("--comma", action="store_true", help="output as comma-separated line")
        args = parser.parse_args(list(argv))

        if args.count is not None:
                result = first_n_primes(args.count)
        elif args.limit is not None:
                result = primes_upto(args.limit)
        elif args.range is not None:
                a, b = args.range
                result = primes_in_range(a, b)
        else:
                result = first_n_primes(10)

        if args.comma:
                print(", ".join(map(str, result)))
        else:
                for p in result:
                        print(p)
        return 0


if __name__ == "__main__":
        raise SystemExit(main(sys.argv[1:]))
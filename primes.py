""" 
Primes - compares the performance of 2 different prime number generators
"""

import timeit


MAX_PRIME = 5000
NUM_ITERATIONS = 1000


def slow_primes_generator() -> int:
    """
    Prime number generator that conserves resources at the expense of performance

    Yields:
        int: the next prime number
    """
    yield 1
    yield 2
    for maybe_prime in range(3, MAX_PRIME):
        for divisor in range(2, (maybe_prime >> 1) + 1):
            if (maybe_prime % divisor) == 0:
                break
        else:
            yield maybe_prime


def slow_primes():
    """
    Test function to iterate over all of the prime numbers returned by the
    slow_primes_generator function
    """
    p_gen = slow_primes_generator()
    for _ in p_gen:
        pass


def fast_primes_generator() -> int:
    """
    Prime number generator that consumes resources (memory) to achieve better performance

    Yields:
        int: the next prime number
    """
    primes = [1, 2]
    yield primes[-2]
    yield primes[-1]
    for maybe_prime in range(3, MAX_PRIME):
        for prime in primes[1:]:
            if (maybe_prime % prime) == 0:
                break
        else:
            primes.append(maybe_prime)
            yield maybe_prime


def fast_primes():
    """
    Test function to iterate over all of the prime numbers returned by the
    fast_primes_generator function
    """
    p_gen = fast_primes_generator()
    for _ in p_gen:
        pass


if __name__ == "__main__":
    print(
        "timeit slow_primes: ",
        timeit.timeit(
            "slow_primes()", setup="pass", number=NUM_ITERATIONS, globals=globals()
        ),
    )
    print(
        "timeit fast_primes: ",
        timeit.timeit(
            "fast_primes()", setup="pass", number=NUM_ITERATIONS, globals=globals()
        ),
    )

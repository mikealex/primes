"""
Unit tests for primes.py
"""


from primes import slow_primes_generator, fast_primes_generator


def test_slow_primes_generator():
    """
    Unit test for slow_primes_generator
    """
    p_gen = slow_primes_generator()
    assert next(p_gen) == 1
    assert next(p_gen) == 2
    assert next(p_gen) == 3
    assert next(p_gen) == 5
    assert next(p_gen) == 7
    assert next(p_gen) == 11
    assert next(p_gen) == 13


def test_fast_primes_generator():
    """
    Unit test for fast_primes_generator
    """
    p_gen = fast_primes_generator()
    assert next(p_gen) == 1
    assert next(p_gen) == 2
    assert next(p_gen) == 3
    assert next(p_gen) == 5
    assert next(p_gen) == 7
    assert next(p_gen) == 11
    assert next(p_gen) == 13

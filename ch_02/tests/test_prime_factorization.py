from ..prime_factorization import calc_prime_factors
import pytest

@pytest.mark.parametrize("value, prime_factors", [
    (8, [2, 2, 2]),
    (14, [2, 7]),
    (42, [2, 3, 7]),
    (1001, [7, 11, 13]),
    (1155, [3, 5, 7, 11]),
    (2222, [2, 11, 101]),
])
def test_calc_prime_factors(value, prime_factors):
    assert calc_prime_factors(value) == prime_factors
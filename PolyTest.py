import pytest
from Polynomial import Polynomial  # Import the Polynomial class from your module


def test_init():
    poly = Polynomial([3, 0, 2])
    assert poly.coefficients == [3, 0, 2]


def test_str():
    poly = Polynomial([3, 0, 2])
    assert str(poly) == "3x^2 + 2"

    poly2 = Polynomial([1, -1])
    assert str(poly2) == "1x + -1"

    poly3 = Polynomial([0, 0, 0])
    assert str(poly3) == "0" or str(poly3) == ""


def test_add():
    poly1 = Polynomial([3, 0, 2])
    poly2 = Polynomial([1, -1])

    poly_sum = poly1 + poly2
    assert poly_sum.coefficients == [3, 1, 1]


def test_sub():
    poly1 = Polynomial([3, 0, 2])
    poly2 = Polynomial([1, -1])

    poly_diff = poly1 - poly2
    assert poly_diff.coefficients == [3, -1, 3]


def test_mul():
    poly1 = Polynomial([3, 0, 2])
    poly2 = Polynomial([1, -1])

    poly_product = poly1 * poly2
    assert poly_product.coefficients == [3, -3, 2, -2]


def test_first_degree_polynomial():
    poly = Polynomial([2, -3])  # Represents 2x - 3
    root = poly.find_root_bisection(0, 5)
    assert abs(root - 1.5) < 1e-6


def test_second_degree_polynomial():
    poly = Polynomial([1, 0, -2])  # Represents x^2 - 2
    root = poly.find_root_bisection(1, 2)
    assert abs(root - 2.0 ** 0.5) < 1e-6


def test_third_degree_polynomial():
    poly = Polynomial([1, 0, -2, 0])  # Represents x^3 - 2x
    root = poly.find_root_bisection(-2, 2)
    assert abs(root - 0.0) < 1e-6


def test_mutate_coefficients():
    poly = Polynomial([3, 0, 2])
    mutated = poly.mutate_coefficients()
    assert poly.coefficients != mutated.coefficients

def test_shuffle_coefficients():
    poly = Polynomial([3, 0, 2])
    shuffled = poly.shuffle_coefficients()
    assert poly.coefficients != shuffled.coefficients

def test_reverse_polynomial():
    poly = Polynomial([3, 0, 2])
    reversed_poly = poly.reverse_polynomial()
    assert poly.coefficients != reversed_poly.coefficients

def test_multiply_by_constant():
    poly = Polynomial([3, 0, 2])
    multiplied = poly.multiply_by_constant()
    assert poly.coefficients != multiplied.coefficients

def test_divide_by_constant():
    poly = Polynomial([3, 0, 2])
    divided = poly.divide_by_constant()
    assert poly.coefficients != divided.coefficients

def test_shift_coefficients_left():
    poly = Polynomial([3, 0, 2])
    shifted_left = poly.shift_coefficients_left()
    assert poly.coefficients != shifted_left.coefficients

def test_shift_coefficients_right():
    poly = Polynomial([3, 0, 2])
    shifted_right = poly.shift_coefficients_right()
    assert poly.coefficients != shifted_right.coefficients

def test_add_fixed_number():
    poly = Polynomial([3, 0, 2])
    added = poly.add_fixed_number()
    assert poly.coefficients != added.coefficients

def test_subtract_fixed_number():
    poly = Polynomial([3, 0, 2])
    subtracted = poly.subtract_fixed_number()
    assert poly.coefficients != subtracted.coefficients

def test_remove_zeros():
    poly = Polynomial([3, 0, 2, 0, 0])
    non_zero = poly.remove_zeros()
    assert poly.coefficients != non_zero.coefficients

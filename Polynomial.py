class Polynomial:
    def __init__(self, coefficients):
        """
        Initialize a polynomial with a list of coefficients. The coefficients list should be in descending order of
        the exponent, for example: [3, 0, 2] represents 3x^2 + 2.
        """
        self.coefficients = coefficients

    def __str__(self):
        """
        Return a string representation of the polynomial.
        """
        if len(self.coefficients) == 0:
            return "0"

        terms = []
        for i, coef in enumerate(self.coefficients):
            if coef == 0:
                continue
            term = str(coef)
            if i < len(self.coefficients) - 1:
                if i == len(self.coefficients) - 2:
                    term += "x"
                else:
                    term += "x^" + str(len(self.coefficients) - i - 1)
            terms.append(term)
        return " + ".join(terms)

    def __add__(self, other):
        """
        Add two polynomials and return a new polynomial.
        """
        max_length = max(len(self.coefficients), len(other.coefficients))
        padded_self = [0] * (max_length - len(self.coefficients)) + self.coefficients
        padded_other = [0] * (max_length - len(other.coefficients)) + other.coefficients
        result_coefficients = [a + b for a, b in zip(padded_self, padded_other)]
        return Polynomial(result_coefficients)

    def __sub__(self, other):
        """
        Subtract another polynomial from this polynomial and return a new polynomial.
        """
        max_length = max(len(self.coefficients), len(other.coefficients))
        padded_self = [0] * (max_length - len(self.coefficients)) + self.coefficients
        padded_other = [0] * (max_length - len(other.coefficients)) + other.coefficients
        result_coefficients = [a - b for a, b in zip(padded_self, padded_other)]
        return Polynomial(result_coefficients)

    def __mul__(self, other):
        """
        Multiply this polynomial by another polynomial and return a new polynomial.
        """
        result_deg = len(self.coefficients) + len(other.coefficients) - 1
        result_coefficients = [0] * result_deg
        for i in range(len(self.coefficients)):
            for j in range(len(other.coefficients)):
                result_coefficients[i + j] += self.coefficients[i] * other.coefficients[j]
        return Polynomial(result_coefficients)

    def evaluate(self, x):
        """
        Evaluate the polynomial for a given value of x.
        """
        result = 0
        for i, coef in enumerate(self.coefficients):
            result += coef * (x ** (len(self.coefficients) - i - 1))
        return result

    def get_derivative_coefficients(self):
        """
        Return the coefficients of the derivative polynomial.
        """
        return [i * coeff for (i, coeff) in enumerate(list(reversed(self.coefficients))[:-1])]

    def find_root_bisection(self, a, b, epsilon=1e-6, max_iterations=100):
        """
        Find a root (zero) of the polynomial using the bisection method within the interval [a, b].
        :param a: Left boundary of the interval.
        :param b: Right boundary of the interval.
        :param epsilon: Tolerance for the root approximation.
        :param max_iterations: Maximum number of iterations.
        :return: Approximated root within the specified interval.
        """
        if self.evaluate(a) * self.evaluate(b) > 0:
            raise ValueError("The chosen interval does not contain a root.")

        for _ in range(max_iterations):
            c = (a + b) / 2
            print(c)
            if abs(self.evaluate(c)) < epsilon:
                return c
            if self.evaluate(c) * self.evaluate(a) < 0:
                b = c
            else:
                a = c

        raise ValueError("Bisection method did not converge within the maximum number of iterations.")

    def mutate_coefficients(self):
        """
        Mutate coefficients by changing them to fixed values.
        """
        mutated_coefficients = [coef + 1 for coef in self.coefficients]
        return Polynomial(mutated_coefficients)

    def shuffle_coefficients(self):
        """
        Shuffle coefficients by reversing the order.
        """
        shuffled_coefficients = list(reversed(self.coefficients))
        return Polynomial(shuffled_coefficients)

    def reverse_polynomial(self):
        """
        Reverse the entire polynomial.
        """
        reversed_poly = Polynomial(list(reversed(self.coefficients)))
        return reversed_poly

    def multiply_by_constant(self):
        """
        Multiply all coefficients by a fixed constant.
        """
        multiplied_coefficients = [coef * 2 for coef in self.coefficients]
        return Polynomial(multiplied_coefficients)

    def divide_by_constant(self):
        """
        Divide all coefficients by a fixed constant.
        """
        divided_coefficients = [coef // 2 for coef in self.coefficients]
        return Polynomial(divided_coefficients)

    def shift_coefficients_left(self):
        """
        Shift all coefficients one place to the left.
        """
        shifted_coefficients = self.coefficients[1:] + [0]
        return Polynomial(shifted_coefficients)

    def shift_coefficients_right(self):
        """
        Shift all coefficients one place to the right.
        """
        shifted_coefficients = [0] + self.coefficients[:-1]
        return Polynomial(shifted_coefficients)

    def add_fixed_number(self):
        """
        Add a fixed number to all coefficients.
        """
        added_coefficients = [coef + 5 for coef in self.coefficients]
        return Polynomial(added_coefficients)

    def subtract_fixed_number(self):
        """
        Subtract a fixed number from all coefficients.
        """
        subtracted_coefficients = [coef - 3 for coef in self.coefficients]
        return Polynomial(subtracted_coefficients)

    def remove_zeros(self):
        """
        Remove trailing zeros in the coefficients.
        """
        non_zero_coefficients = self.coefficients[::-1]
        non_zero_coefficients = non_zero_coefficients[non_zero_coefficients.index(
            next(filter(lambda x: x != 0, non_zero_coefficients))):]
        non_zero_coefficients.reverse()
        return Polynomial(non_zero_coefficients)


# Example usage:
poly1 = Polynomial([3, 0, 2])  # Represents 3x^2 + 2
poly2 = Polynomial([1, -1])  # Represents x - 1

print("poly1:", poly1)
print("poly2:", poly2)

poly_sum = poly1 + poly2
print("Sum:", poly_sum)

poly_diff = poly1 - poly2
print("Difference:", poly_diff)

poly_product = poly1 * poly2
print("Product:", poly_product)

x_value = 2
result = poly1.evaluate(x_value)
print(f"Evaluation of poly1 at x={x_value}: {result}")

poly = Polynomial([1, 0, -2])  # Represents x^2 - 2
print(f"Evaluation of poly at a,b: {poly.evaluate(0)}, {poly.evaluate(5)}")
root = poly.find_root_bisection(0, 5)
print(f"Root of {poly} within [0, 5]: {root}")

print()
print("Mutation Operations")
print()
# Assume the Polynomial class and mutation functions are defined

poly = Polynomial([3, 0, 2])  # Represents 3x^2 + 2

print("Original Polynomial:", poly)

# Applying mutation functions
mutated_1 = poly.mutate_coefficients()
print("Mutated Coefficients:", mutated_1)

shuffled = poly.shuffle_coefficients()
print("Shuffled Coefficients:", shuffled)

reversed_poly = poly.reverse_polynomial()
print("Reversed Polynomial:", reversed_poly)

multiplied = poly.multiply_by_constant()
print("Multiplied Coefficients:", multiplied)

divided = poly.divide_by_constant()
print("Divided Coefficients:", divided)

shift_left = poly.shift_coefficients_left()
print("Shifted Left Coefficients:", shift_left)

shift_right = poly.shift_coefficients_right()
print("Shifted Right Coefficients:", shift_right)

added = poly.add_fixed_number()
print("Coefficients After Adding:", added)

subtracted = poly.subtract_fixed_number()
print("Coefficients After Subtracting:", subtracted)

no_zeros = poly.remove_zeros()
print("Coefficients Without Trailing Zeros:", no_zeros)

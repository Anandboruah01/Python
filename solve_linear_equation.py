def solve_linear_equation(a, b):
    # ax + b = 0
    if a == 0:
        if b == 0:
            return "Infinite solutions (any value of x satisfies the equation)."
        else:
            return "No solution (inconsistent equation)."
    else:
        x = -b / a
        return f"The solution is x = {x}"

# Example usage:
print(solve_linear_equation(2, -4))  # Solves 2x - 4 = 0
print(solve_linear_equation(0, 0))   # Infinite solutions
print(solve_linear_equation(0, 5))   # No solution

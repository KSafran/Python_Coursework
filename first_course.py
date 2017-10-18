# Compare square root algorithms

# Global Parameters
epsilon = 0.00001
square = float(input('What number would you like to find the square root of? :'))
if square <= 1:
    print('Number must be > 1')

# Bisectional search - works for square < 1
root = 0.0
left_bound = 0.0
right_bound = square
count = 0

while abs(square - root**2) > epsilon and count < 1000:
    count += 1
    if root**2 < square:
        left_bound = root
    else:
        right_bound = root
    root = left_bound + (right_bound - left_bound)/2

print('Bisectional Search: The square root of %.3f is %.5f and it took %d rounds to guess this.' % (square, root, count))

# Other algorithm
root_b = square/2.0
count_b = 0

while abs(square - root_b**2) > epsilon and count_b < 1000:
    count_b += 1
    root_b = (square/root_b + root_b)/2

print('Other Algorithm: The square root of %.3f is %.5f and it took %d rounds to guess this.' % (square, root_b, count_b))

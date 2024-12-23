# MATLAB Program 2-1

import control as ct

# Define numerators and denominators
num1 = [10]
den1 = [1, 2, 10]
num2 = [5]
den2 = [1, 5]

# Define G1(s) and G2(s) -sys1 and sys2, respectively-
sys1 = ct.tf(num1, den1)
sys2 = ct.tf(num2, den2)

# Calculate the series, parallel and feedback for G1(s) and G2(s)
series = ct.series(sys1, sys2)
parallel = ct.parallel(sys1, sys2)
feedback = ct.feedback(sys1, sys2)

print("Series: ", series)
print("Parallel: ", parallel)
print("Feedback: ", feedback)

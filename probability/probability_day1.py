import numpy as np
import pandas as pd

# Dice probability
outcomes = np.array([1, 2, 3, 4, 5, 6])

even_numbers = outcomes[
    outcomes % 2 == 0
]

probability_even = (
    len(even_numbers) /
    len(outcomes)
)

print("Probability of even:", probability_even)

# Probability of rolling a 5
probability_five = (
    np.sum(outcomes == 5) /
    len(outcomes)
)

print("Probability of rolling 5:", probability_five)
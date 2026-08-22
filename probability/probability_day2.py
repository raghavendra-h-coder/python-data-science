import numpy as np

outcomes = np.array([
    1, 2, 3, 4, 5, 6
])

even = outcomes[
    outcomes % 2 == 0
]

greater_than_four = outcomes[
    outcomes > 4
]

intersection = np.intersect1d(
    even,
    greater_than_four
)

union = np.union1d(
    even,
    greater_than_four
)

print("Even:", even)
print("Greater than 4:", greater_than_four)
print("Intersection:", intersection)
print("Union:", union)

p_even = len(even) / len(outcomes)
p_greater_than_four = (
    len(greater_than_four) /
    len(outcomes)
)

p_intersection = (
    len(intersection) /
    len(outcomes)
)

p_union = len(union) / len(outcomes)

print("\nP(Even):", p_even)
print("P(>4):", p_greater_than_four)
print("P(Even AND >4):", p_intersection)
print("P(Even OR >4):", p_union)
import numpy as np

# Independent events
# probability of two heads
p_head_first = 1 / 2
p_head_second = 1 / 2

p_two_heads = (
    p_head_first *
    p_head_second
)

print("P(two heads):", p_two_heads)

#probability of dice
p_six_first = 1 / 6
p_six_second = 1 / 6

p_two_sixes = (
    p_six_first *
    p_six_second
)

print("P(two sixes):", p_two_sixes)

#dependent events
# 4 red balls, 6 green balls

p_first_red = 4/6
p_second_red = 3/9

p_both_red = p_first_red * p_second_red

print("Probability of both red:", p_both_red)
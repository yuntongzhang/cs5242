from math import sqrt

lr = 0.001
beta_one = 0.9
beta_two = 0.999
m = 0 # biased first moment estimate
v = 0 # biased second raw moment estimate
w = 0 # parameter
t = 0

# region A
gradient = -1
while w <= 1:
    t = t + 1
    m = beta_one * m + (1 - beta_one) * gradient
    v = beta_two * v + (1 - beta_two) * gradient * gradient
    m_p = m / (1 - pow(beta_one, t))
    v_p = v / (1 - pow(beta_two, t))
    w = w - lr * (m_p / sqrt(v_p))
print(f"Entering region B with --- w={w}, t={t}, m={m}, v={v}")

# Now entering region B
gradient = 1
while True:
    t = t + 1
    m = beta_one * m + (1 - beta_one) * gradient
    v = beta_two * v + (1 - beta_two) * gradient * gradient
    m_p = m / (1 - pow(beta_one, t))
    v_p = v / (1 - pow(beta_two, t))
    delta_w = -lr * (m_p / sqrt(v_p))
    if delta_w <= 0:
        break
    w = w + delta_w
print(f"Going to move w to the left with --- w={w}, t={t}, m={m}, v={v}")
h_max = w - 1
print(f"Max heigth h is : {h_max}")

"""
Execution result of the above code:

Entering region B with --- w=1.0000000000000007, t=1000, m=-0.9999999999999994, v=0.6323045752290364
Going to move w to the left with --- w=1.0024340620000007, t=1007, m=0.04340620000000016, v=0.6348707344549913
Max heigth h is : 0.0024340620000007362
"""

symptoms = {
    "fever": 0.8,
    "cough": 0.7,
    "fatigue": 0.6
}

prior = 0.3
not_disease = 0.7

likelihood = 1

for value in symptoms.values():
    likelihood *= value

posterior = (prior * likelihood) / (
    (prior * likelihood) + (not_disease * 0.1)
)

print("Probability of Disease:", round(posterior, 4))

if posterior > 0.5:
    print("Possible Disease Detected")
else:
    print("Disease Probability is Low")
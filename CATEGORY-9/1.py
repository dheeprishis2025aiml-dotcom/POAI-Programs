prior = 0.2
evidence = 0.9
not_evidence = 0.3

posterior = (prior * evidence) / (
    (prior * evidence) + ((1 - prior) * not_evidence)
)

print("Obstacle Probability:", round(posterior, 4))

if posterior > 0.5:
    print("Obstacle Detected")
    print("Vehicle Stops")
else:
    print("No Obstacle Detected")
    print("Vehicle Continues")
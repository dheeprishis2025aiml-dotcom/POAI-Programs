prior = 0.1
sensor_data = 0.85
normal_data = 0.2

posterior = (prior * sensor_data) / (
    (prior * sensor_data) + ((1 - prior) * normal_data)
)

print("Machine Failure Probability:", round(posterior, 4))

if posterior > 0.5:
    print("Machine Failure Detected")
    print("Maintenance Required")
else:
    print("Machine Operating Normally")
facts = {
    "obstacle_detected",
    "red_signal",
    "vehicle_moving"
}

rules = {
    "apply_brake": ["obstacle_detected"],
    "stop_vehicle": ["red_signal"],
    "slow_down": ["apply_brake"],
    "safe_stop": ["stop_vehicle", "slow_down"]
}

def forward_chaining():
    new_fact = True

    while new_fact:
        new_fact = False

        for conclusion, conditions in rules.items():
            if all(condition in facts for condition in conditions):
                if conclusion not in facts:
                    facts.add(conclusion)
                    new_fact = True

    print("Facts:", facts)

def backward_chaining(goal):
    if goal in facts:
        return True

    if goal not in rules:
        return False

    return all(backward_chaining(condition)
               for condition in rules[goal])

forward_chaining()

goal = "safe_stop"
print("Backward Chaining:", backward_chaining(goal))
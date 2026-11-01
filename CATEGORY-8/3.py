facts = {
    "raw_material_available",
    "machine_ready",
    "worker_available"
}

rules = {
    "production_started": [
        "raw_material_available",
        "machine_ready"
    ],
    "quality_check": ["production_started"],
    "product_ready": [
        "quality_check",
        "worker_available"
    ],
    "dispatch_product": ["product_ready"]
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

goal = "dispatch_product"
print("Backward Chaining:", backward_chaining(goal))
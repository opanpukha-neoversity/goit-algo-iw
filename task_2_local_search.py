import random
import math


def sphere_function(x):
    return sum(xi ** 2 for xi in x)


def random_point(bounds):
    return [random.uniform(low, high) for low, high in bounds]


def clip(x, bounds):
    return [
        max(min(xi, bounds[i][1]), bounds[i][0])
        for i, xi in enumerate(x)
    ]


def hill_climbing(func, bounds, iterations=1000, epsilon=1e-6):
    current = random_point(bounds)
    current_value = func(current)

    step_size = 0.1

    for _ in range(iterations):
        neighbor = [
            xi + random.uniform(-step_size, step_size)
            for xi in current
        ]
        neighbor = clip(neighbor, bounds)
        neighbor_value = func(neighbor)

        if neighbor_value < current_value:
            if abs(current_value - neighbor_value) < epsilon:
                break
            current, current_value = neighbor, neighbor_value

    return current, current_value


# Random Local Search
def random_local_search(func, bounds, iterations=1000, epsilon=1e-6):
    best = random_point(bounds)
    best_value = func(best)

    for _ in range(iterations):
        candidate = random_point(bounds)
        candidate_value = func(candidate)

        if candidate_value < best_value:
            if abs(best_value - candidate_value) < epsilon:
                break
            best, best_value = candidate, candidate_value

    return best, best_value


def simulated_annealing(func, bounds, iterations=1000, temp=1000, cooling_rate=0.95, epsilon=1e-6):
    current = random_point(bounds)
    current_value = func(current)

    temperature = temp

    for _ in range(iterations):
        if temperature < epsilon:
            break

        neighbor = [
            xi + random.uniform(-1, 1)
            for xi in current
        ]
        neighbor = clip(neighbor, bounds)
        neighbor_value = func(neighbor)

        delta = neighbor_value - current_value

        if delta < 0 or random.random() < math.exp(-delta / temperature):
            if abs(current_value - neighbor_value) < epsilon:
                break
            current, current_value = neighbor, neighbor_value

        temperature *= cooling_rate

    return current, current_value


if __name__ == "__main__":
    bounds = [(-5, 5), (-5, 5)]

    print("Hill Climbing:")
    hc_solution, hc_value = hill_climbing(sphere_function, bounds)
    print("Розв'язок:", hc_solution)
    print("Значення:", hc_value)

    print("\nRandom Local Search:")
    rls_solution, rls_value = random_local_search(sphere_function, bounds)
    print("Розв'язок:", rls_solution)
    print("Значення:", rls_value)

    print("\nSimulated Annealing:")
    sa_solution, sa_value = simulated_annealing(sphere_function, bounds)
    print("Розв'язок:", sa_solution)
    print("Значення:", sa_value)

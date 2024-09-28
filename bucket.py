from collections import deque

# Function to check if the current state contains exactly 4 liters in any bucket
def is_goal(state):
    return 4 in state

# Function to get all possible moves (transitions) from the current state
def get_next_states(state):
    x, y, z = state
    capacities = (8, 5, 3)
    next_states = set()

    # Fill each bucket
    next_states.add((capacities[0], y, z))  # Fill 8-liter bucket
    next_states.add((x, capacities[1], z))  # Fill 5-liter bucket
    next_states.add((x, y, capacities[2]))  # Fill 3-liter bucket

    # Empty each bucket
    next_states.add((0, y, z))  # Empty 8-liter bucket
    next_states.add((x, 0, z))  # Empty 5-liter bucket
    next_states.add((x, y, 0))  # Empty 3-liter bucket

    # Pour from one bucket into another
    # Pour from 8-liter to 5-liter
    pour = min(x, capacities[1] - y)
    next_states.add((x - pour, y + pour, z))

    # Pour from 8-liter to 3-liter
    pour = min(x, capacities[2] - z)
    next_states.add((x - pour, y, z + pour))

    # Pour from 5-liter to 8-liter
    pour = min(y, capacities[0] - x)
    next_states.add((x + pour, y - pour, z))

    # Pour from 5-liter to 3-liter
    pour = min(y, capacities[2] - z)
    next_states.add((x, y - pour, z + pour))

    # Pour from 3-liter to 8-liter
    pour = min(z, capacities[0] - x)
    next_states.add((x + pour, y, z - pour))

    # Pour from 3-liter to 5-liter
    pour = min(z, capacities[1] - y)
    next_states.add((x, y + pour, z - pour))

    return next_states

# BFS to find the solution with the minimal number of moves
def water_bucket_puzzle():
    initial_state = (8, 0, 0)  # Start with the 8-liter bucket full
    queue = deque([(initial_state, [])])  # Store (state, path)
    visited = set([initial_state])

    while queue:
        current_state, path = queue.popleft()

        # Check if the current state meets the goal
        if is_goal(current_state):
            return path + [current_state]  # Return the path to the solution

        # Explore the next possible states
        for next_state in get_next_states(current_state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [current_state]))

    return None  # No solution found

# Run the puzzle solver and print the solution path
solution = water_bucket_puzzle()
if solution:
    print("Solution found with the following steps:")
    for step in solution:
        print(step)
else:
    print("No solution found.")

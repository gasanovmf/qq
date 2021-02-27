def world_physics(state):
    if state["y"] <= 0:
        state["y"] = 0

    return state
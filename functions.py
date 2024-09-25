def detect_backtracking(steps):
    return (steps.diff() < 0).any()

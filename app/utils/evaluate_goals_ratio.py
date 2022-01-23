from app.utils.get_ratio import get_ratio


def evaluate_goals_ratio(reached_goals: int, required_goals: int) -> float:
    """
    Obtain the goals ratio. If the reached goals are greater than or equals to
    the required, it means that 100% of available points for current topic
    (individual or team) has been reached.
    """
    if reached_goals >= required_goals:
        return 1
    else:
        goals_ratio = get_ratio(reached_goals, required_goals)
        return goals_ratio

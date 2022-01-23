def calculate_bonus(
    base_bonus_salary: int,
    individual_goals_ratio: float,
    team_goals_ratio: float
) -> int:
    """
    Calculate the bonus salary.
    Formula:
    `base_bonus_salary` * (`individual_goals_ratio` + `team_goals_ratio`) / 2
    """
    if base_bonus_salary == 0:
        return 0
    average_goals_ratio = (individual_goals_ratio + team_goals_ratio) / 2
    base_bonus_salary = int(base_bonus_salary * average_goals_ratio)
    return base_bonus_salary

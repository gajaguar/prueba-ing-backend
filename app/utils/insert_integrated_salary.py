from app.models import Player


def insert_integrated_salary(
    player: Player,
    calculated_bonus: int,
) -> Player:
    """
    Calculate the integrated salary and add to the player.
    """
    integrated_salary = player.player_base_salary + calculated_bonus
    player.player_integrated_salary = integrated_salary
    return player

from typing import Callable

def teleport(target: str, power: int) -> str:
    return f"{target} has been teleported for {power} HP"

def invisibility(target: str, power: int) -> str:
    return f"{target} went invisible for {power} hp"

def vortex(target: str, power: int) -> str:
    return f"{target} created a protection vortex for {power} HP"

def control(target: str, power: int) -> str:
    return f"{target} took control of another target for {power} hp"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    return lambda: (spell1, spell2)

combined = spell_combiner(teleport("dragon", 12), vortex("monster", 10))
print(combined())
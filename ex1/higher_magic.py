from collections.abc import Callable


def teleport(target: str, power: int) -> str:
    return f"{target} has been teleported for {power} HP"


def invisibility(target: str, power: int) -> str:
    return f"{target} went invisible for {power} HP"


def vortex(target: str, power: int) -> str:
    return f"{target} created a protection vortex for {power} HP"


def control(target: str, power: int) -> str:
    return f"{target} took control of another target for {power} HP"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple:
        return spell1(target, power), spell2(target, power)

    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)

    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def caster(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"

    return caster


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> list:
        return [spell(target, power) for spell in spells]

    return sequence


if __name__ == "__main__":
    print("Testing spell combiner...")
    combined_spell = spell_combiner(teleport, invisibility)
    fireball_result, heal_result = combined_spell("Dragon", 25)
    print(f"Combined spell result: {fireball_result}, {heal_result}")

    print("\nTesting power amplifier...")
    mega_teleport = power_amplifier(teleport, 3)
    print(f"Original: {teleport('Dragon', 10)}")
    print(f"Amplified: {mega_teleport('Dragon', 10)}")

    print("\nTesting conditional caster...")
    guarded_vortex = conditional_caster(
        lambda target, power: power >= 50, vortex
    )
    print(guarded_vortex("Dragon", 70))
    print(guarded_vortex("Dragon", 10))

    print("\nTesting spell sequence...")
    full_combo = spell_sequence([teleport, invisibility, vortex, control])
    for result in full_combo("Dragon", 25):
        print(result)

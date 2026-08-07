from collections.abc import Callable
from functools import wraps
import inspect
import time


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: object, **kwargs: object) -> object:
        print(f"Casting {func.__name__}...")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result

    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: object, **kwargs: object) -> object:
            bound = inspect.signature(func).bind(*args, **kwargs)
            bound.apply_defaults()
            power = bound.arguments.get("power")
            if power is None or power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: object, **kwargs: object) -> object:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            f"Spell failed, retrying... "
                            f"(attempt {attempt}/{max_attempts})"
                        )
            return f"Spell casting failed after {max_attempts} attempts"

        return wrapper

    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(
            char.isalpha() or char == " " for char in name
        )

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


@spell_timer
def fireball(target: str) -> str:
    time.sleep(0.1)
    return "Fireball cast!"


@retry_spell(max_attempts=3)
def unstable_spell(target: str) -> str:
    raise RuntimeError("Spell fizzled")


@retry_spell(max_attempts=3)
def guaranteed_spell(target: str) -> str:
    return "Waaaaaaagh spelled !"


if __name__ == "__main__":
    print("Testing spell timer...")
    spell_result = fireball("Dragon")
    print(f"Result: {spell_result}")

    print("\nTesting retrying spell...")
    print(unstable_spell("Ork"))
    print(guaranteed_spell("Ork"))

    print("\nTesting MageGuild...")
    guild = MageGuild()
    print(MageGuild.validate_mage_name("Gandalf"))
    print(MageGuild.validate_mage_name("Al"))
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Spark", 5))

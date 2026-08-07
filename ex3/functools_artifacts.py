from collections.abc import Callable
from functools import lru_cache, partial, reduce, singledispatch
from typing import Any
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    operations: dict[str, Callable[[int, int], int]] = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min,
    }

    if operation not in operations:
        raise ValueError(f"Unknown spell operation: {operation}")

    return reduce(operations[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    elements = ["fire", "ice", "lightning"]
    return {
        element: partial(base_enchantment, power=50, element=element)
        for element in elements
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def cast(spell: Any) -> str:
        return "Unknown spell type"

    @cast.register
    def _(spell: int) -> str:
        return f"{spell} damage"

    @cast.register
    def _(spell: str) -> str:
        return spell

    @cast.register
    def _(spell: list) -> str:
        return f"{len(spell)} spells"

    return cast


def apply_enchantment(power: int, element: str, target: str) -> str:
    return f"{target} enchanted with {element} ({power} power)"


if __name__ == "__main__":
    print("Testing spell reducer...")
    spells: list[int] = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")
    try:
        spell_reducer(spells, "divide")
    except ValueError as error:
        print(f"Error: {error}")

    print("\nTesting partial enchanter...")
    enchantments = partial_enchanter(apply_enchantment)
    print(enchantments["fire"](target="Sword"))
    print(enchantments["ice"](target="Shield"))

    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    print(f"Cache info: {memoized_fibonacci.cache_info()}")

    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(f"Damage spell: {dispatcher(42)}")
    print(f"Enchantment: {dispatcher('fireball')}")
    print(f"Multi-cast: {dispatcher(['fireball', 'heal', 'shield'])}")
    print(dispatcher(3.14))

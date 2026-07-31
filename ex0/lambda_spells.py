def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda a: a["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda m: m["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    return {
        "max_power": max(mages, key=lambda m: m["power"])["power"],
        "min_power": min(mages, key=lambda m: m["power"])["power"],
        "avg_power": round(
            sum(map(lambda m: m["power"], mages)) / len(mages), 2
        ),
    }


if __name__ == "__main__":
    artifacts: list[dict] = [
        {"name": "Sword of Flames", "power": 75, "type": "weapon"},
        {"name": "Amulet of Wisdom", "power": 40, "type": "accessory"},
        {"name": "Staff of Storms", "power": 90, "type": "weapon"},
        {"name": "Ring of Shadows", "power": 60, "type": "accessory"},
    ]

    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    first, second = sorted_artifacts[0], sorted_artifacts[1]
    print(
        f"{first['name']} ({first['power']} power) comes before "
        f"{second['name']} ({second['power']} power)"
    )

    mages: list[dict] = [
        {"name": "Alex", "power": 85, "element": "fire"},
        {"name": "Jordan", "power": 60, "element": "water"},
        {"name": "Riley", "power": 92, "element": "air"},
    ]

    print("\nTesting power filter...")
    strong_mages = power_filter(mages, 80)
    print(f"Mages with power >= 80: {[m['name'] for m in strong_mages]}")

    spells: list[str] = ["fireball", "heal", "shield"]
    print("\nTesting spell transformer...")
    print(" ".join(spell_transformer(spells)))

    print("\nTesting mage stats...")
    print(mage_stats(mages))

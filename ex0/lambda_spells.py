def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda a: a["power"], reverse=True)

def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x["power"] >= min_power, mages))

def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda m: f"* {m} *", spells))

artifacts: list[dict] = [
    {"name": "Sword of Flames", "power": 75, "type": "weapon"},
    {"name": "Amulet of Wisdom", "power": 40, "type": "accessory"},
    {"name": "Staff of Storms", "power": 90, "type": "weapon"},
    {"name": "Ring of Shadows", "power": 60, "type": "accessory"},
]

# print(artifact_sorter(artifacts))
# print(power_filter(artifacts, 80))
# print(spell_transformer(("sdsds", "gdhged", "rt ywttw", "h")))
def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda a: a["power"], reverse=True)

artifacts: list[dict] = [
    {"name": "Sword of Flames", "power": 75, "type": "weapon"},
    {"name": "Amulet of Wisdom", "power": 40, "type": "accessory"},
    {"name": "Staff of Storms", "power": 90, "type": "weapon"},
    {"name": "Ring of Shadows", "power": 60, "type": "accessory"},
]

print(artifact_sorter(artifacts))
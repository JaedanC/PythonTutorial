def save_level(filename, level_state):
    with open(filename, "w") as f:
        level = level_state["level"]
        enemies = level_state["enemies"]
        pickups = ",".join(level_state["pickups"])
        f.write(f"Level:{level}\n")
        f.write(f"Enemies:{enemies}\n")
        f.write(f"Pickups:{pickups}")


level = {
    "level": 1,
    "enemies": 15,
    "pickups": [ "potions", "gear", "weapons" ]
}

save_level("level_1_save.txt", level)
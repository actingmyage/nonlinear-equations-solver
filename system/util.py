

def choose_system(systems: list) -> list:
    print("<Choose system to solve!> \n")

    for i in range(len(systems)):
        print(f"SYSTEM {i + 1} = {{")

        system = systems[i]
        for j in range(len(system)):
            print(f"[{j + 1}] {system[j]}")
        print("}\n")

    choice = int(input("System: "))
    print("\n <Choose system to solve!> [END] \n")
    return systems[choice-1]

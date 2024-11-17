def calculate_love_score(name1, name2):
    combined_names = (name1 + name2).lower()

    true_count = (combined_names.count('t') + combined_names.count('r') + combined_names.count('u') + combined_names.count('e'))

    print(f"T occurs {combined_names.count('t')}")
    print(f"R occurs {combined_names.count('r')}")
    print(f"U occurs {combined_names.count('u')}")
    print(f"E occurs {combined_names.count('e')}")

    print(f"The Total of TRUE: {true_count}\n")

    love_count = (combined_names.count('l') + combined_names.count('o') + combined_names.count('v') + combined_names.count('e'))

    print(f"L occurs {combined_names.count('l')}")
    print(f"O occurs {combined_names.count('o')}")
    print(f"V occurs {combined_names.count('v')}")
    print(f"E occurs {combined_names.count('e')}")

    print(f"The Total of LOVE: {love_count}\n")


    print(f"True love score: {true_count}{love_count}")


calculate_love_score("Angela Yu", "Jack Bauer")

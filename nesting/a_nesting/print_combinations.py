def print_combinations(colors, clothes):
        for color in colors:
            for cloth in clothes:
                 print(color,cloth)

colors = ["gray","cream", "cyan"]
clothes = ["shirt", "flannel"]
print_combinations(colors,clothes)

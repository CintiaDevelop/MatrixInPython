matrix = [
    ["BR", "BK", "BB", "BK", "BQ", "BB", "BK", "BR"],
    ["BP", "BP", "BP", "BP", "BP", "BP", "BP", "BP"],
    ["0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0"],
    ["WP", "WP", "WP", "WP", "WP", "WP", "WP", "WP"],
    ["WR", "WK", "WB", "WQ", "WK", "WB", "WK", "WR"]
]

for fila in matrix:
    for elemento in fila:
        print(elemento, end=" ")
    print()
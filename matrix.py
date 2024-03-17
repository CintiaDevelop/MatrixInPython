matrix = [
    ["BRook", "BKnight", "BBishop", "BKing ", "BQueen", "BBishop", "BKnight", "BRook"],
    ["BPawn", " BPawn ", " BPawn ", "BPawn ", "BPawn ", " BPawn ", " BPawn ", "BPawn"],
    ["     ", "       ", "       ", "      ", "      ", "       ", "       ", "     "],
    ["     ", "       ", "       ", "      ", "      ", "       ", "       ", "     "],
    ["     ", "       ", "       ", "      ", "      ", "       ", "       ", "     "],
    ["     ", "       ", "       ", "      ", "      ", "       ", "       ", "     "],
    ["WPawn", " WPawn ", " WPawn ", "WPawn ", "WPawn ", " WPawn ", " WPawn ", "WPawn"],
    ["WRook", "WKnight", "WBishop", "WQueen", "WKing ", "WBishop", "WKnight", "WRook"]
]

for fila in matrix:
    for elemento in fila:
        print(elemento, end=" ")
    print()

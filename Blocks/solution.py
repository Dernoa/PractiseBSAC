def can_spell(word, blocks):
    word = word.lower()
    used_blocks = {}

    for letter in word:
        if letter in used_blocks and used_blocks[letter] == 2:
            return False

        if letter in used_blocks:
            used_blocks[letter] += 1
        else:
            block_found = False
            for block in blocks:
                if block[0].lower() == letter and block not in used_blocks.values():
                    used_blocks[letter] = 1
                    block_found = True
                    break
                elif block[1].lower() == letter and block not in used_blocks.values():
                    used_blocks[letter] = 1
                    block_found = True
                    break

            if not block_found:
                return False

    return True

blocks = [
    ("B", "O"),
    ("X", "K"),
    ("D", "Q"),
    ("C", "P"),
    ("N", "A"),
    ("G", "T"),
    ("R", "E"),
    ("T", "G"),
    ("Q", "D"),
    ("F", "S"),
    ("J", "W"),
    ("H", "U"),
    ("V", "I"),
    ("A", "N"),
    ("O", "B"),
    ("E", "R"),
    ("F", "S"),
    ("L", "Y"),
    ("P", "C"),
    ("Z", "M")
]

word = input(str())
print(can_spell(word, blocks))  # True


def canConstruct(ransomNote, magazine):
    # Create dictionaries to count characters in ransomNote and magazine
    ransom_count = {}
    magazine_count = {}

    # Count characters in ransomNote
    for char in ransomNote:
        ransom_count[char] = ransom_count.get(char, 0) + 1
        print("ransome_count", ransom_count)

    # Count characters in magazine
    for char in magazine:
        magazine_count[char] = magazine_count.get(char, 0) + 1
        print("magazine_count", magazine_count)

    # Check if characters in ransomNote can be formed from magazine
    for char, count in ransom_count.items():
        if char not in magazine_count or magazine_count[char] < count:
            return False

    return True


print(canConstruct("aa", "ab"))

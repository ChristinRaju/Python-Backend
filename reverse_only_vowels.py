def reverse_vowels(word):
    vowels = "aeiouAEIOU"
    vowels_only = []

    # Step 1: Collect vowels from the word
    for letter in word:
        if letter in vowels:
            vowels_only.append(letter)

    # Step 2: Create a new word with reversed vowels
    result = ""
    for letter in word:
        if letter in vowels:
            result = result + vowels_only.pop()  # Take last vowel
        else:
            result = result + letter

    return result

# Example
print(reverse_vowels("hello"))  # Output: "holle"

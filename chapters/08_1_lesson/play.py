def only_vowels(phrase):
    # Takes a phrase, and returns a string of all the vowels
    # Initalize an empty string to hold all of the vowels
    vowel_string = ''
    for letter in phrase:
        # check if each letter is a vowel
        if is_a_vowel(letter):
            # If it's a vowel, we append the letter to the vowel string
            vowel_string = vowel_string + letter
        # if not a vowel, we don't care about it- so do nothing!

    return vowel_string
    # Code after a "return" doesn't print
    print("A line of code after the return!")

def run_only_vowels(phrase):
    print(phrase, only_vowels(phrase))

# Testing the functions
run_only_vowels("tim the beAver")
run_only_vowels("HeLlO wOrLd!!")
run_only_vowels("klxn")
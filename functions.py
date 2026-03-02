def add(a, b):
    return a + b


def is_even(n):
    return n % 2 == 0


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def count_vowels(text):
    vowels = "aeiou"
    count = 0
    for ch in text.lower():
        if ch in vowels:
            count += 1
    return count


def first_word(sentence):
    return sentence.split()[0]
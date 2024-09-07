from celery.contrib.testing.manager import Manager

from arjanCodes.avoid_bad_practice.string_utils import (
    reverse_and_uppercase,
    remove_vowels,
    count_words,
)


def main() -> None:
    s = "Hellow, World!"
    print(reverse_and_uppercase(s))
    print(remove_vowels(s))
    print(count_words(s))


if __name__ == "__main__":
    main()

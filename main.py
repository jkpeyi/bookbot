def main():
    with open("books/frankenstein.txt") as f:
        contents = f.read()
        print(contents)

        total_word= word_count(contents)
        lt_count=count_letter(contents)
        
        print(lt_count)
        stdout(lt_count,total_word)


def word_count(text):
    return len(text.split())


def count_letter(text):

    letters = {}
    for alp in "abcdefghijklmopqrstuwxyz":
        letters[alp]=0

    for letter in text.lower():
        if letter in letters:
            letters[letter]+=1
    return letters

def stdout(letters, total_word):

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{total_word} words found in the document\n")

    for letter in letters:
        print(f"The {letter} character was found {letters[letter]} times")
    print("--- End report ---")

main()
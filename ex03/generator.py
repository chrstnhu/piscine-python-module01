import sys
import random 

def manual_shuffle(lst):
    """
    Shuffle the list and yield the elements one by one.
    """
    # Copy the list
    shuffled_lst = lst[:]
    
    # Shuffle the list
    n = len(shuffled_lst)
    for i in range(n):
        # Pick a random index
        j = random.randint(i, n - 1)
        # Swap the elements
        shuffled_lst[i], shuffled_lst[j] = shuffled_lst[j], shuffled_lst[i]
    
    for word in shuffled_lst:
        yield word


def manual_unique(text):
    """
    Removes duplicates from the list.
    """
    # Save the words in a set
    seen = set()

    for word in text:
        # Check if the word is unique
        if word not in seen:
            seen.add(word)
            yield word


def manual_ordered(text):
    """
    Orders the list in ascending order.
    """
    # Sort the list
    sorted_words = sorted(text)
    for word in sorted_words:
        yield word


def generator(text, sep=" ", option=None):
    """
    Splits the text according to sep value and yields the substrings.
    """
    # Check if is valid
    if option not in ["shuffle", "unique", "ordered", None]:
        raise ValueError("Option should be either 'shuffle', 'unique', 'ordered' or None")
  
    if not isinstance(text, str):
        raise ValueError("ERROR: Text should be a string")
    if not text.isprintable():
        raise ValueError("ERROR: Text should be printable")
    
    # Split the text into words
    words = text.split(sep)
    
    if option == "shuffle":
        yield from manual_shuffle(words)
    elif option == "unique":
        yield from manual_unique(words)
    elif option == "ordered":
        yield from manual_ordered(words)
    else:
        for word in words:
            yield word


# Main
if __name__ == "__main__":
    try:
        text1 = "Le Lorem Ipsum est simplement du faux texte."
        
        print("-> Test generator with no option :\n" + text1)
        for word in generator(text1, sep=" "):
            print(word)
        
        print("\n-> Test generator with option shuffle:\n" + text1)
        for word in generator(text1, sep=" ", option="shuffle"):
            print(word)

        print("\n-> Test generator with option ordered:\n" + text1)
        for word in generator(text1, sep=" ", option="ordered"):
            print(word)

        text2 = "Lorem Ipsum Lorem Ipsum"
        
        print("\n-> Test generator with option unique:\n" + text2)
        for word in generator(text2, sep=" ", option="unique"):
            print(word)

        text3 = 1.0
        print("\n-> Test generator with no option :\n" + str(text3))
        for word in generator(text3, sep="."):
            print(word)

    except Exception as e:
        print(e)

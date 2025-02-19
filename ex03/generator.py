import sys
import random 

def manual_shuffle(lst):
    """
    Shuffle the list.
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
    
    return shuffled_lst

def manual_unique(text):
    """
    Removes duplicates from the list.
    """
    words = text.split()

    # Create a empty list
    unique_words = []
    for word in words:
        # Check if the word is unique and append
        if word not in unique_words:
            unique_words.append(word)
    
    return unique_words

def manual_ordered(text):
    """
    Orders the list in ascending order.
    """
    words = text.split()

    # Sort the list
    sorted_words = sorted(words)

    return sorted_words


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
        shuffled_text = manual_shuffle(words)        
        for word in shuffled_text:
            yield word
    elif option == "unique":
        unique_text = manual_unique(text) 
        for word in unique_text:
            yield word
    elif option == "ordered":
        ordered_text = manual_ordered(text)
        for word in ordered_text:
            yield word
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

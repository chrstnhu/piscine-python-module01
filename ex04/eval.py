import sys

class Evaluator :
    @staticmethod
    def zip_evaluate(coefs, words):
        """
        Zip two lists and multiply the elements.
        (the first item in each passed iterator is paired together)
        """

        if len(coefs) != len(words):
            return -1
        
        res = 0
        for coef, word in zip(coefs, words):
            res += len(word) * coef
            # print(tuple(zip(coefs, words)))
        return res

    @staticmethod
    def enumerate_evaluate(coefs, words):
        """
        Enumerate the lists and multiply the elements.
        (adds a counter to each item in iterator or list)
        """
        if len(coefs) != len(words):
            return -1
        
        res = 0
        for index, word in enumerate(words, start = 0):
            res += len(word) * coefs[index]
            # print(list(enumerate(words, start = 0)))
        return res


# Main
if __name__ == "__main__" :
    # Zip evaluate
    word1 = ["Le", "Lorem", "Ipsum", "est", "simple"]
    coef1 = [1.0, 2.0, 1.0, 4.0, 0.5]

    print("=== Zip evaluate ===")
    print(Evaluator.zip_evaluate(coef1, word1))

    # Enumerate evaluate
    word2 = ["Le", "Lorem", "Ipsum", "n’", "est", "pas", "simple"]
    coef2 = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42, 0.0]
    
    print("\n=== Enumerate evaluate ===")
    print(Evaluator.enumerate_evaluate(coef2, word2))


    # Error handling
    word3 = ["Le", "Lorem", "Ipsum", "est", "simple"]
    coef3 = [1.0, 2.0, 1.0, 4.0, 0.5, 1.5]

    print("\n=== Zip evaluate ===")
    print(Evaluator.zip_evaluate(coef3, word3))

    word4 = ["Le", "Lorem", "Ipsum", "n’", "est", "pas", "simple"]
    coef4 = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
    
    print("\n=== Error enumerate evaluate ===")
    print(Evaluator.enumerate_evaluate(coef4, word4))
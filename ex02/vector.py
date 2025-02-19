class Vector:
    def __init__(self, data):
        self.data = data

        if len(data) > 0 and len(data[0]) == 1:
            self.values = data #column vector
            self.shape = (len(data), 1)
        elif len(data) == 1 and isinstance(data[0], list):
            self.values = data #row vector
            self.shape = (1, len(data[0]))
        else:
            raise ValueError("Invalid vector shape")

    # ADDITION
    def __add__(self, other):
        """
        Handles the addition of a scalar or another vector.
        Only vectors of the same shape.
        """
    
        if isinstance(other, Vector):
            if self.shape != other.shape:
                raise ValueError("Cannot add vectors of different lengths")
            result_data = [
                [self.data[i][j] + other.data[i][j] for j in range(len(self.data[i]))]
                for i in range(len(self.data))
            ]
            return Vector(result_data)
        elif isinstance(other, (int, float)):
            result_data = [
                [self.data[i][j] + other for j in range(len(self.data[i]))]
                for i in range(len(self.data))
            ]
            return Vector(result_data)
        else:
            raise TypeError("Unsupported addition type.")

    def __radd__(self, other):
        """
            Handles the addition of a scalar or another vector.
            Only vectors of the same shape.
        """
        return self.__add__(other)


    # SUBSTRACTION
    def __sub__(self, other):
        """
        Handles the substraction of a scalar or another vector.
        Only vectors of the same shape.
        """
        if isinstance(other, Vector):
            if self.shape != other.shape:
                raise ValueError("Cannot add vectors of different lengths")
            result_data = [
                [self.data[i][j] - other.data[i][j] for j in range(len(self.data[i]))]
                for i in range(len(self.data))
            ]
            return Vector(result_data)
        elif isinstance(other, (int, float)):
            result_data = [
                [self.data[i][j] - other for j in range(len(self.data[i]))]
                for i in range(len(self.data))
            ]
            return Vector(result_data)
        else:
            raise TypeError("Unsupported substraction type.")

    def __rsub__(self, other):
        """
        Handles the substraction of a scalar or another vector.
        Only vectors of the same shape.
        """
        return self.__sub__(other)
    

    # DIVISION
    def __truediv__(self, other):
        """
        Handles the division of a scalar or another vector.
        Only with scalars (to perform division of a Vector by a scalar).
        """            

        if isinstance(other, Vector):
            if self.shape != other.shape:
                raise ValueError("Cannot multiply vectors of different lengths")
            result_data = [
                [self.data[i][j] / other.data[i][j] for j in range(len(self.data[i]))]
                for i in range(len(self.data))
            ]
            return Vector(result_data)
        elif isinstance(other, (int, float)):
            if other == 0 or other == 0.0:
                raise ZeroDivisionError("ZeroDivisionError: division by zero.")
            result_data = [
                [self.data[i][j] / other for j in range(len(self.data[i]))]
                for i in range(len(self.data))
            ]
            return Vector(result_data)
        else:
            raise TypeError("Unsupported substraction type.")


    def __rtruediv__(self, other):
        """
        Handles the division of a scalar or another vector.
        Only with scalars (to perform division of a Vector by a scalar).
        """
        raise NotImplementedError("NotImplementedError: Division of a scalar by a Vector is not defined here.")



    # MULTIPLICATION
    def __mul__(self, other):
        """
        Handles the multiplication of a scalar or another vector.
        Only scalars (to perform multiplication of a Vector by a scalar).
        """
    
        if isinstance(other, Vector):
            if self.shape != other.shape:
                raise ValueError("Cannot multiply vectors of different lengths")
            result_data = [
                [self.data[i][j] * other.data[i][j] for j in range(len(self.data[i]))]
                for i in range(len(self.data))
            ]
            return Vector(result_data)
        elif isinstance(other, (int, float)):
            result_data = [
                [self.data[i][j] * other for j in range(len(self.data[i]))]
                for i in range(len(self.data))
            ]
            return Vector(result_data)
        else:
            raise TypeError("Unsupported multiplication type.")

    def __rmul__(self, other):
        """
        Handles the reverse multiplication (scalar * vector).
        """
        return self.__mul__(other)


    # STRING REPRESENTATION
    def __str__(self):
        """
        Returns a string representation of a vector for printing.
        """
        # Flattening the 2D list to a 1D list
        flattened = [item[0] for item in self.data]
        return f"[[{', '.join(map(str, flattened))}]]"

    #  USEFUL FOR INTERACTIVE SESSION (python3 shell)
    def __repr__(self):
        """
        Returns a string representation of a vector for interactive session.
        """
        return self.__str__()

    
    def dot(self, other):
        """
        Computes the dot product of two vectors.
        """
        if self.shape != other.shape:
            raise ValueError("Cannot compute dot product of vectors of different lengths")
        result = 0
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                result += self.data[i][j] * other.data[i][j]
        return result

    def T(self):
        """
        Transposes the vector.
        If it's a column vector, it becomes a row vector and vice versa.
        """
        # Row to column
        if len(self.data) == 1:
            return Vector([[self.data[0][i]] for i in range(len(self.data[0]))])
        # Column to row
        else:
            return Vector([self.data[i] for i in range(len(self.data))])


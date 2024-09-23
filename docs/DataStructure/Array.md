# [Day 1: Arrays and Strings](https://docs.google.com/spreadsheets/d/1pViJo3jAgve8OB_qHbircFv4lW214_9edoSmc5Yq6RA/edit?gid=0#gid=0)
* Concepts to Learn: Arrays, dynamic arrays, string manipulations.
### Topics:
* Basics of arrays (1D and 2D arrays).
* Common operations (insert, delete, update).
* String manipulation (substrings, searching, concatenation).
### Practice Problems:
* Find the second-largest element in an array.
* Reverse a string in place.
* Check if a string is a palindrome.
### Resources:
* [Arrays in C# (Official Documentation)](https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/arrays/)
* [Strings in C# (Official Documentation)](https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/strings/)
* [LeetCode Problem Set: Arrays](https://leetcode.com/problem-list/array/)


## Basic Array
* An array is a group of like-typed variables that are referred to by a common name. And each data item is called an element of the array.

* The number of dimensions are set when an array variable is declared. The length of each dimension is established when the array instance is created. These values can't be changed during the lifetime of the instance.

* Each element in the array is accessed by its index, starting from zero.
* An array is a collection of elements stored in contiguous memory locations, where each element is of the same type (e.g., int, string, char). Arrays are one of the most basic and fundamental data structures used for storing multiple values.

## Types of Array
There are 3 types of array in C#. They are 

1. Single-dimensional array
2. Multidimensional array
3. Jagged array

### 1. Single-dimensional array
A 1D array is a simple list of elements of the same type. It's indexed by a single integer.

#### Declaration:
```
int[] arr = new int[5];  // Creates an array of 5 integers
```

#### Initialization:
```
int[] arr = {1, 2, 3, 4, 5};  // Initializes an array with 5 elements
```

#### Accessing Elements:
```
Console.WriteLine(arr[2]);  // Output: 3
arr[2] = 10;                // Update the element at index 2
```
#### Example
```
int[] numbers = {10, 20, 30, 40, 50};
for (int i = 0; i < numbers.Length; i++)
{
    Console.WriteLine(numbers[i]);
}

```

### 2. 2D Arrays (Two-Dimensional Arrays)
A 2D array is an array of arrays, which can be visualized as a table with rows and columns.

#### Declaration:
```
int[,] matrix = new int[3, 3];  // Creates a 3x3 matrix (2D array)

```

#### Initialization:
```
int[,] matrix = {
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9}
};

```

#### Accessing Elements:
```
Console.WriteLine(matrix[1, 2]);  // Output: 6 (element at row 1, column 2)
matrix[1, 2] = 10;                // Update the element at row 1, column 2

```
#### Example
```
int[,] matrix = {
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9}
};

for (int i = 0; i < 3; i++)
{
    for (int j = 0; j < 3; j++)
    {
        Console.Write(matrix[i, j] + " ");
    }
    Console.WriteLine();
}


```



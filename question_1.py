
 Lab 4 - Question 1

 Task:
 Write a Python program to find the smallest number in the following list
 using a for loop.
 my_list = [3, 1, 0, 9, 5, 2, 6, 4, 9, 8, 7]
 Print the smallest number as the output.


def main():
    print("=" * 45)
    print("       FIND SMALLEST NUMBER IN LIST          ")
    print("=" * 45)

    # Given list
    my_list = [3, 1, 0, 9, 5, 2, 6, 4, 9, 8, 7]
    print(f"Given List: {my_list}\n")

    # Assume the first number is the smallest initially
    smallest = my_list[0]

    # Iterate through each number in the list using a for loop
    for num in my_list:
        if num < smallest:
            smallest = num

    # Display the result
    print("-" * 45)
    print(f"The smallest number in the list is: {smallest}")
    print("-" * 45)

    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()

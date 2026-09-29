
 Lab 4 - Question 2

 Task:
 Write a Python program to find the average of all the numbers in the following list:
 my_list = [3, 1, 0, 9, 5, 2, 6, 4, 9, 8, 7]
 Use a for loop to calculate the sum of the numbers and then find and print their average.


def main():
    print("=" * 45)
    print("      CALCULATE SUM & AVERAGE OF LIST        ")
    print("=" * 45)

    # Given list
    my_list = [3, 1, 0, 9, 5, 2, 6, 4, 9, 8, 7]
    print(f"Given List: {my_list}\n")

    # Initialize total sum to 0
    total_sum = 0

    # Calculate sum using a for loop
    for num in my_list:
        total_sum += num

    # Count of elements
    count = len(my_list)

    # Calculate average
    average = total_sum / count

    # Display results
    print("-" * 45)
    print(f"Total Count of Numbers : {count}")
    print(f"Sum of Numbers         : {total_sum}")
    print(f"Average of Numbers     : {average:.2f} (Exact: {average})")
    print("-" * 45)

    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()


 Lab 4 - Question 4
 
 Task:
 Create an empty list:
 shopping = []
 Ask the user to enter 5 shopping items.
 Then display the complete shopping list.
 

def main():
    print("=" * 45)
    print("            SHOPPING LIST MANAGER            ")
    print("=" * 45)

    # 1. Create an empty list
    shopping = []

    # 2. Ask user to enter 5 shopping items using a loop
    total_items = 5
    print(f"Please enter {total_items} items for your shopping list:\n")

    for i in range(1, total_items + 1):
        while True:
            item = input(f"Enter item {i}: ").strip()
            if item:
                shopping.append(item)
                break
            print("Item cannot be empty. Please enter an item name.")

    # 3. Display the complete shopping list
    print("\n" + "=" * 45)
    print("           COMPLETE SHOPPING LIST            ")
    print("=" * 45)
    print(f"List representation : {shopping}\n")

    print("Itemized List:")
    for idx, item in enumerate(shopping, start=1):
        print(f"  {idx}. {item}")
    print("=" * 45)

    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()

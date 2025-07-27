import random

while True:
    choice = input("roll the dice ? (y/n) ").lower()

    if choice == "y":
        # Ask user how many dice they want to roll
        while True:
            try:
                num_dice = int(input("How many dice do you want to roll? (1-10): "))
                if 1 <= num_dice <= 10:
                    break
                else:
                    print("Please enter a number between 1 and 10!")
            except ValueError:
                print("Please enter a valid number!")           
        
        # Roll the specified number of dice
        dice_results = []
        for i in range(num_dice):
            dice_results.append(random.randint(1, 6))
        
        # Display the results
        if num_dice == 1:
            print(f"You rolled: {dice_results[0]}")
        else:
            print(f"You rolled: {dice_results}")
            print(f"Total: {sum(dice_results)}")

    elif choice == "n":
        print("Thanks for playing!")
        break

    else:
        print("Invalid choice!")

 





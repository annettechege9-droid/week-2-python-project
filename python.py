import random

# Function to save scores
def save_score(username, attempts_used):
    with open("highscores.txt", "a") as file:
        file.write(f"{username} - {attempts_used} attempts\n")

# Function to display leaderboard
def show_leaderboard():
    try:
        print("\n===== LEADERBOARD =====")
        with open("highscores.txt", "r") as file:
            scores = file.readlines()
            if scores:
                for score in scores:
                    print(score.strip())
            else:
                print("No scores yet.")
    except FileNotFoundError:
        print("No leaderboard found.")

# Welcome message
print("===== GUESS THE NUMBER GAME =====")

username = input("Enter your name: ")

# Difficulty levels
print("\nChoose Difficulty:")
print("1. Easy (10 tries)")
print("2. Medium (7 tries)")
print("3. Hard (5 tries)")

choice = input("Enter choice (1/2/3): ")

if choice == "1":
    attempts = 10
elif choice == "2":
    attempts = 7
elif choice == "3":
    attempts = 5
else:
    print("Invalid choice. Defaulting to Easy.")
    attempts = 10

# Generate random number
secret_number = random.randint(1, 100)

remaining_attempts = attempts
wrong_guesses = 0

print("\nI have chosen a number between 1 and 100.")
print(f"You have {attempts} attempts to guess it!")

while remaining_attempts > 0:
    try:
        guess = int(input("\nEnter your guess: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if guess == secret_number:
        attempts_used = attempts - remaining_attempts + 1
        print(f"\n🎉 Congratulations {username}!")
        print(f"You guessed the number {secret_number} in {attempts_used} attempts.")
        save_score(username, attempts_used)
        break

    elif guess < secret_number:
        print("Too Low!")
    else:
        print("Too High!")

    remaining_attempts -= 1
    wrong_guesses += 1

    # Hint after 3 wrong tries
    if wrong_guesses == 3:
        print("\n--- HINT ---")
        if secret_number <= 50:
            print("Hint: The number is between 1 and 50.")
        else:
           print("Hint: The number is between 51 and 100.")
    
    if remaining_attempts > 0:
        print(f"Remaining guesses: {remaining_attempts}")

else:
    print(f"\n❌ Game Over! The number was {secret_number}.")

# Show leaderboard
show_leaderboard()
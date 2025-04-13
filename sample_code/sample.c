#include <stdio.h>
#include <stdlib.h> // For rand() and srand()
#include <time.h>   // For time() - used for seeding the random number generator

// Function prototypes (declaration before use)
int generateRandomNumber(int min, int max);
int getUserGuess();
void compareGuess(int randomNumber, int userGuess);
void printGameRules();

int main() {
    // Seed the random number generator based on the current time.
    // This ensures you get a different random number each time you run the program.
    srand(time(NULL));

    int randomNumber;
    int userGuess;
    char playAgain;

    printGameRules();  // Display game rules at the start

    do {
        // Generate a random number between 1 and 100 (inclusive).
        randomNumber = generateRandomNumber(1, 100);

        // Get the user's guess.
        userGuess = getUserGuess();

        // Compare the user's guess to the random number and provide feedback.
        compareGuess(randomNumber, userGuess);

        printf("Do you want to play again? (y/n): ");
        scanf(" %c", &playAgain);  // Note the space before %c to consume leftover newline characters
    } while (playAgain == 'y' || playAgain == 'Y');

    printf("Thanks for playing!\n");

    return 0;
}


// Function to generate a random number within a specified range.
int generateRandomNumber(int min, int max) {
    return (rand() % (max - min + 1)) + min;
}


// Function to get the user's guess.
int getUserGuess() {
    int guess;
    printf("Enter your guess (between 1 and 100): ");
    scanf("%d", &guess);

    // Input validation:  Check if the guess is within the valid range.
    while (guess < 1 || guess > 100) {
        printf("Invalid guess. Please enter a number between 1 and 100: ");
        scanf("%d", &guess);
    }

    return guess;
}

// Function to compare the user's guess to the random number.
void compareGuess(int randomNumber, int userGuess) {
    if (userGuess == randomNumber) {
        printf("Congratulations! You guessed the number!\n");
    } else if (userGuess < randomNumber) {
        printf("Too low. Try again.\n");
    } else {
        printf("Too high. Try again.\n");
    }
    printf("The number was: %d\n", randomNumber); // Reveal the number at the end
}

// Function to print the game rules and instructions.
void printGameRules() {
    printf("Welcome to the Number Guessing Game!\n");
    printf("I will generate a random number between 1 and 100.\n");
    printf("Your goal is to guess the number.\n");
    printf("I will provide feedback on whether your guess is too high or too low.\n");
    printf("Good luck!\n\n");
}
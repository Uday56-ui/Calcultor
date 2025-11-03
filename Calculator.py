#include <stdio.h>

int main() {
    int choice;
    float num1, num2, result;

    printf("------ Simple Calculator ------\n");
    printf("1. Addition (+)\n");
    printf("2. Subtraction (-)\n");
    printf("3. Multiplication (*)\n");
    printf("4. Division (/)\n");
    printf("5. Modulus (%%)\n");
    printf("-------------------------------\n");

    printf("Enter your choice (1-5): ");
    scanf("%d", &choice);

    if (choice == 5) {
        int a, b;
        printf("Enter two integers: ");
        scanf("%d %d", &a, &b);
        if (b == 0) {
            printf("Error! Division by zero is not allowed.\n");
        } else {
            printf("Result: %d %% %d = %d\n", a, b, a % b);
        }
    } else {
        printf("Enter two numbers: ");
        scanf("%f %f", &num1, &num2);

        switch (choice) {
            case 1:
                result = num1 + num2;
                printf("Result: %.2f + %.2f = %.2f\n", num1, num2, result);
                break;
            case 2:
                result = num1 - num2;
                printf("Result: %.2f - %.2f = %.2f\n", num1, num2, result);
                break;
            case 3:
                result = num1 * num2;
                printf("Result: %.2f * %.2f = %.2f\n", num1, num2, result);
                break;
            case 4:
                if (num2 == 0)
                    printf("Error! Division by zero is not allowed.\n");
                else {
                    result = num1 / num2;
                    printf("Result: %.2f / %.2f = %.2f\n", num1, num2, result);
                }
                break;
            default:
                printf("Invalid choice! Please select a valid option (1-5).\n");
        }
    }

    return 0;
}

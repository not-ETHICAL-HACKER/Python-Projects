#include <stdio.h>

// Function to find maximum of 3 values
int max_3(int a, int b, int c)
{
    int m = a;
    if (b > m)
        m = b;
    if (c > m)
        m = c;
    return m;
}

int main()
{
    float red, green, blue, cyan, yellow, magenta;
    float white;

    printf("Enter values for red, green, blue: ");

    for (;;)
    {
        scanf("%f %f %f", &red, &green, &blue);

        if (red > 255 || red < 0 ||
            green > 255 || green < 0 ||
            blue > 255 || blue < 0)
        {
            printf("\nInvalid RGB values. Try again: ");
        }
        else
        {
            printf("\nThank you for giving valid values.\n");
            break;
        }
    }

    white = max_3(red, green, blue) / 255.0;

    printf("White = %f\n", white);
    cyan = white - (red / 255.0);
    yellow = white - (green / 255.0);
    magenta = white - (blue / 255.0);
    printf("Cyan: %f\nYellow: %f\nMagenta: %f\n", cyan, yellow, magenta);
    return 0;
}

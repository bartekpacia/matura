/**
 * Użytkownik podaje znak. Program wyświetla czy jest to samogłoska. Jeśli znak
 * nie jest samogłoską, wyświetla tekst "To inny znak".
 */

#include <ctype.h>
#include <stdio.h>

int main() {
    char znak;

    printf("Podaj znak: \n");
    scanf("%c", &znak);

    znak = tolower(znak);

    switch (znak) {
        case 'a':
        case 'e':
        case 'i':
        case 'o':
        case 'u':
        case 'y':
            printf("To samogłoska\n");
            break;
        default:
            printf("To inny znak\n");
    }

    getchar();
    return 0;
}
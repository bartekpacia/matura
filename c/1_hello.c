/**
 * Najprostszy program w C. Wyświetla tekst i czeka na naciśnięcie
 * dowolnego klawisza.
 */

// Importujemy bibliotekę standardowego wejścia-wyjścia (standard input-output).
// Dzięki temu mamy dostęp do funkcji printf i getchar.
#include <stdio.h>

// Wykonywanie każdego programu zaczyna się od funkcji nazwanej main.
int main() {
    printf("Hello World!\n");  // wyświetlenie tekstu w terminalu
    getchar();  // czekanie na wciśnięcie dowolnego klawisza (get character)
    return 0;   // zwrócenie wartości z funkcji main. 0 oznacza pomyślne
                // wykonanie programu.
}
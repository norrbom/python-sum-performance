#include <stdio.h>
#include <stdlib.h>

int main() {
    long ln = 100000000, sum = 0;
    int *array = (int *)malloc(ln  * sizeof(int));

    if (array == NULL) {
        printf("Memory allocation failed.\n");
        return 1;
    }

    // initialize the array
    for (int i = 0; i < ln; i++) {
        array[i] = i + 1;
    }

    // sum the array
    for (int i = 0; i < ln; i++) {
        sum += array[i];
    }

    printf("Sum of the array is %ld\n", sum);

    // Use the array here

    free(array); // Don't forget to free the allocated memory

    return 0;
}

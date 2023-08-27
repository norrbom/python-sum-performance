#include <stdio.h>
#include <stdlib.h>

int main() {
    long ln = 100000000, sum = 0;
    int *array = (int *)malloc(ln  * sizeof(int));

    if (array == NULL) {
        printf("Could not allocate enough memory.\n");
        return 1;
    }

    // initialize the array and sum
    for (int i = 0; i < ln; i++) {
        array[i] = i + 1;
        sum += array[i];
    }

    printf("Sum of the array is %ld\n", sum);
    free(array);

    return 0;
}

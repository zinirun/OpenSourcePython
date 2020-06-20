#include "multiplication.h"

void multiplication(int **a, int **b) {
    int **c = malloc(sizeof(int *) * rowA);
    for (int i = 0; i < rowA; i++)
        c[i] = malloc(sizeof(int) * colB);
    int sum;
    for (int i = 0; i < rowA; i++) {
        for (int j = 0; j < colB; j++) {
            sum = 0;
            for (int k = 0; k < colA; k++)
                sum += a[i][k] * b[k][j];
            c[i][j] = sum;
        }
    }
    
    printf("result\n");
    for (int i = 0; i < rowA; i++) {
        for (int j = 0; j < colB; j++)
            printf("%d\t", c[i][j]);
        printf("\n");
    }
    for (int i = 0; i < rowA; i++)
        free(c[i]);
    free(c);
}


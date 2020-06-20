#include "division.h"
void division(int **a, int **b) {
    int idx = 0;
    int **c = malloc(sizeof(int *) * rowA);
    for (int i = 0; i < rowA; i++) {
        c[i] = malloc(sizeof(int) * colA);
        for (int j = 0; j < colA; j++)
            c[i][j] = 0;
    }
    for (int i = 0; i < rowA; i++) {
        for (int j = 0; j < colA; j++) {
            if (b[i][j] == 0) {
                printf("Error : Can't divide by zero");
                idx = 1;
                break;
            }
            else
                c[i][j] = a[i][j] / b[i][j];
        }
    }
    if (idx == 0) {
        printf("result\n");
        for (int i = 0; i < rowA; i++) {
            for (int j = 0; j < colA; j++)
                printf("%d\t", c[i][j]); printf("\n");
        }
        for (int i = 0; i < rowA; i++)
            free(c[i]);
        free(c);
    }
    else {
        for (int i = 0; i < rowA; i++)
            free(c[i]);
        free(c);
    }
}



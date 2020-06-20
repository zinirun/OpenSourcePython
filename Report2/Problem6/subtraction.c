#include "subtraction.h"

void subtraction(int **a, int **b) {
    int **c = malloc(sizeof(int *) * rowA);
    
    for (int i = 0; i < rowA; i++)
        c[i] = malloc(sizeof(int *) * colA);
    
    for (int i = 0; i < rowA; i++) {
        for (int j = 0; j < colA; j++){
            c[i][j] = a[i][j] - b[i][j];
        }
        
    }
    printf("result\n");
    for (int i = 0; i < rowA; i++) {
        for (int j = 0; j < colA; j++) { printf("%d\t", c[i][j]);
        }
        printf("\n");
    }
    for (int i = 0; i < rowA; i++)
        free(c[i]);
    free(c);
}



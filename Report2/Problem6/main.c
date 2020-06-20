#include <stdio.h>
#include <stdlib.h>
#include "subtraction.h"
#include "multiplication.h"
#include "division.h"

int rowA, colA, rowB, colB;

int main() {
    int num;
    
    printf("A 행렬의 행(row) : ");
    scanf("%d", &rowA);
    printf("A 행렬의 열(column) : ");
    scanf("%d", &colA);
    int **a = malloc(sizeof(int *) * rowA);
    
    for (int i = 0; i < rowA; i++)
        a[i] = malloc(sizeof(int) * colA);
    printf(">> A 행렬 입력\n");
    for (int i = 0; i < rowA; i++) {
        printf(">> ");
        for (int j = 0; j < colA; j++) {
            scanf("%d", &num);
            a[i][j] = num;
        }
        
    }
    printf("\n");
    
    printf("B 행렬의 행(row) : "); scanf("%d", &rowB);
    printf("B 행렬의 열(column) : "); scanf("%d", &colB);
    int **b = malloc(sizeof(int *) * rowB);
    for (int i = 0; i < rowB; i++)
        b[i] = malloc(sizeof(int) * colB);
    printf(">> B 행렬 입력\n");
    for (int i = 0; i < rowB; i++) {
        printf(">> ");
        for (int j = 0; j < colB; j++) {
            scanf("%d", &num);
            b[i][j] = num;
        }
        
    }
    printf("\n");
    while(1) {
        printf("1. Subtraction / 2. Multiplication / 3.Element-wise Division / 0. Quit\n>> ");
        scanf("%d", &num);
        if (num == 1) {
            subtraction(a, b);
        } else if (num == 2) {
            if (colA == rowB)
                multiplication(a, b);
            else
                printf("Check two matrices row and column");
        } else if (num == 3) {
            if (rowA == rowB && colA == colB)
                division(a, b);
            else
                printf("Check two matrices row and column");
        }
        else {
            for(int i = 0; i < rowA; i++)
                free(a[i]);
            free(a);
            for(int i = 0; i < rowB; i++)
                free(b[i]);
            free(b);
            break;
        }
    }
    return 0;
}

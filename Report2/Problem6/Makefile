CC = gcc
CFLAG = -l.

MatrixCalc: subtraction.o multiplication.o division.o main.o
	$(CC) -o MatrixCalc subtraction.o multiplication.o division.o main.o

subtraction.o: subtraction.c subtraction.h 
	$(CC) -c subtraction.c $(CFLAG)
multiplication.o: multiplication.c multiplication.h 
	$(CC) -c multiplication.c $(CFLAG)
division.o: division.c division.h
	$(CC) -c division.c $(CFLAG)
main.o: main.c subtraction.h multiplication.h division.h 
	$(CC) -c main.c $(CFLAG)
clean:
	rm -f *.o MatrixCalc

#include <stdio.h>

void sumInput() {

   printf("Enter a number: ");
   int num1, num2;
   scanf("%d", &num1);
   printf("Enter a second number: ");
   scanf("%d", &num2);

   
   printf( "The sum is: %d + %d = %d\n", num1, num2, num1 + num2 );
}




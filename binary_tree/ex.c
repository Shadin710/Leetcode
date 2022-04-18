#include<stdio.h>

int main()
{
    float sum=0.0,j=1.0,i=2.0;
    int counter=0;
    while (i/j>0.001)
    {
        j=j+j;
        sum=sum+i/j;
        counter++;
    }
    printf("%d",counter);
}
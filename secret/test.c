#include <stdio.h>
#include <math.h>

int main(){
    int a,b,c,d,e;
    a=67;
    b=69;
    c=a+b;
    printf("%d %d %d",a,b,c);
    printf("\nEnter a Number for Calculations:");
    scanf("%d",&d);
    if (d>=10){
        printf("Helo orlf");
        e=10?5:7;
        printf("Testing Ternary Operator%d",e);
    }
    else{
            a=(int)pow(((b+1)*10),2);
            printf("%d",a);
    }
    return 0;
}
#include <stdio.h>

int main()
{
    double a = 5.0;
    int c = 5;
    int d;
    double b;

    printf("Enter b:");
    scanf("%lf", &b);

    printf("Enter d:");
    scanf("%d", &d);

    a = a + b - 2;
    printf("a = a+b-2 -> %lf\n", a);

    c = c + 1;
    d = c - a + d;
    printf("c = c+1 -> %d\n", c);
    printf("d = c-a+d -> %d\n", d);

    a = a * c;
    c = c - 1;
    printf("a = a*c -> %lf\n", a);
    printf("c = c-1 -> %d\n", c);

    a /= 10;
    c /= 2;
    b -= 1;
    d *= (c + b + a);

    printf("a = a/10 -> %lf\n", a);
    printf("c = c/2 -> %d\n", c);
    printf("b = b-1 -> %lf\n", b);
    printf("d = d*(a+b+c) -> %d\n", d);

    return 0;
}
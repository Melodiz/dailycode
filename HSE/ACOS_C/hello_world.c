#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct point
{
    int x;
    int y;
} point;


int dist(point p1, point p2)
{
    return (p2.x - p1.x) * (p2.x - p1.x) + (p2.y - p1.y) * (p2.y - p1.y);
}

int main()
{
    int n;
    point *mass;
    scanf("%d", &n);
    mass = (point *)malloc(n * sizeof(point));
    for (int i = 0; i < n; i++)
    {
        scanf("%d %d", &mass[i].x, &mass[i].y);
    }
    // enter a new point 
    point new_point;
    printf("Enter the coordinates of the new point: ");  // example: 10 20  (x, y) 
    scanf("%d %d", &new_point.x, &new_point.y);

    // find the closest point to the new point
    int min_dist = dist(mass[0], new_point);
    int min_index = 0;
    for (int i = 1; i < n; i++)
    {
        int dist_i = dist(mass[i], new_point);
        if (dist_i < min_dist)
        {
            min_dist = dist_i;
            min_index = i;
        }
    }
    printf("The closest point to the new point is (%d, %d)\n", mass[min_index].x, mass[min_index].y);
    free(mass);
}
#include <stdio.h>
#include <stdlib.h>

// Define a structure to represent items with weight and value
struct Item
{
    double weight;
    double value;
};

// Function to compare two items based on their value-to-weight ratio
int compare(const void *a, const void *b)
{
    struct Item *itemA = (struct Item *)a;
    struct Item *itemB = (struct Item *)b;
    double ratioA = itemA->value / itemA->weight;
    double ratioB = itemB->value / itemB->weight;
    if (ratioA < ratioB)
        return 1;
    else if (ratioA > ratioB)
        return -1;
    else
        return 0;
}

// Function to perform the greedy knapsack algorithm
double knapsackGreedy(struct Item *items, int n, double maxWeight)
{
    double totalValue = 0;
    double totalWeight = 0;

    // Sort items based on their value-to-weight ratio in non-increasing order
    qsort(items, n, sizeof(struct Item), compare);

    // Iterate through sorted items and add them to the knapsack
    for (int i = 0; i < n; i++)
    {
        if (totalWeight + items[i].weight <= maxWeight)
        {
            totalValue += items[i].value;
            totalWeight += items[i].weight;
        }
        else
        {
            totalValue += (maxWeight - totalWeight) * (items[i].value / items[i].weight);
            break;
        }
    }
    return totalValue;
}

int main()
{
    // Define items and their properties
    struct Item items1[] = {
        {2, 10}, {1, 5}, {3, 15}, {4, 20}};
    int n1 = sizeof(items1) / sizeof(items1[0]);
    double maxWeight1 = 5;
    printf("%.2f\n", knapsackGreedy(items1, n1, maxWeight1));

    struct Item items2[] = {
        {5, 30}, {10, 40}, {15, 45}, {22, 77}, {25, 90}};
    int n2 = sizeof(items2) / sizeof(items2[0]);
    double maxWeight2 = 60;
    printf("%.2f\n", knapsackGreedy(items2, n2, maxWeight2));

    struct Item items3[] = {
        {40, 280}, {10, 100}, {20, 120}, {24, 120}};
    double maxWeight3 = 60;
    int n3 = sizeof(items3) / sizeof(items3[0]);
    printf("%.2f\n", knapsackGreedy(items3, n3, maxWeight3));

    return 0;
}

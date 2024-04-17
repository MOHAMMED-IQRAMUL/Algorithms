#include <bits/stdc++.h>
using namespace std;

double KnapSack_Greedy(vector<array<double, 2>> WP, double MaxWeight) {

    double TotalValue = 0;
    double TotalWeight = 0;
    sort(WP.begin(), WP.end(), [](const auto& a, const auto& b) {
        double ratioA = a[1] / a[0];
        double ratioB = b[1] / b[0];
        return ratioB < ratioA;
    });

    for (int i = 0; i < WP.size(); i++) {
        if (TotalWeight + WP[i][0] <= MaxWeight) {
            TotalValue += WP[i][1];
            TotalWeight += WP[i][0];
        } else {
            TotalValue += (MaxWeight - TotalWeight) * (WP[i][1] / WP[i][0]);
            TotalWeight = MaxWeight;
            break;
        }
    }
    return TotalValue;
}

int main() {
    vector<array<double, 2>> Arr1 = {
        {2, 10}, {1, 5}, {3, 15}, {4, 20}
    };
    double MaxWeight = 5;
    cout << KnapSack_Greedy(Arr1, MaxWeight) << endl;

    vector<array<double, 2>> Arr2 = {
        {5, 30}, {10, 40}, {15, 45}, {22, 77}, {25, 90}
    };
    MaxWeight = 60;
    cout << KnapSack_Greedy(Arr2, MaxWeight) << endl;

    vector<array<double, 2>> Arr3 = {
        {40, 280}, {10, 100}, {20, 120}, {24, 120}
    };
    MaxWeight = 60;
    cout << KnapSack_Greedy(Arr3, MaxWeight) << endl;

    return 0;
}
#include<iostream>
using namespace std;
template<typename T>
void bubbleSort(T arr[], int n) {
    for (int i = 0; i < n - 1; ++i) {
        bool swapped = false;
        for (int j = 0; j < n - 1 - i; ++j) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
                swapped = true;
            }
        }
        if (!swapped)
            break;
    }
    for (int i = 0; i < n; ++i) {
        cout << arr[i] << " ";
    }
    cout << endl;
}
int main() {
    int a[] = { 8, 1, 4, 7, 2, 5, 9, 3, 6 };
    int n = sizeof(a) / sizeof(int);
    cout << "after sort:" << endl;
    bubbleSort<int>(a, n);
    char b[] = { 'l','v','c', 'a', 'r', 'y', 't'};
    int m = sizeof(b) / sizeof(char);
    cout << "after sort:" << endl;
    bubbleSort<char>(b, m);
}
#include <iostream>
 
using namespace std;
 
 
 
int main(void) {
 
    int n,i,pos1,pos2,front=0, rear=0;
 
    int arr[11] = { 0, };
 
    cin >> n;
 
    cin >> pos1;
 
    front = pos1; rear = pos1;
 
    arr[front] = 1;
 
    for (i = 2; i <= n; i++) {
 
        cin >> pos2;
 
        if (pos1 != pos2)
 
            arr[--front] = i;
 
        else
 
            arr[++rear] = i;
 
        pos1 = pos2;
 
    }
 
    for (i = 0; i < n; i++)
 
        cout << arr[i] << " ";
 
    return 0;
 
}
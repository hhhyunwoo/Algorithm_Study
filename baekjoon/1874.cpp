#include <iostream>
#include <math.h>

void push(int*, int);
int pop(int, int*);
void print(int);
void print22();

int top = -1;
char printChar[1000000];
int index = 0;

int j = 0;

using namespace std;

int main() {
	int inputNum,i=0;
	cin >> inputNum;

	if (inputNum > 100000 || inputNum < 1)
		return 0;


	int* inputArr = new int[inputNum];
	for (i = 0; i < inputNum; i++)
		cin >> inputArr[i];


	int* stack = new int[inputNum];
	
	int n = 1;
	i = 0;
	while (1) {
		if (inputArr[j] < n) {
			if(pop(inputArr[j], stack)==0)
				return 0;
	
			j++;
			if (j==inputNum){//top == -1) {
				print22();
				return 0;
			}
			continue;
		}
		else if (inputArr[j] >= n) {
			push(stack, n);
		}
		stack[i] = n;
		i++;
		n++;
	}
	
	return 0;
}
void print(int a) {
	if (a == 1) {
		printChar[index] = '-';
		//cout << "-\n";
	}
	else {
		printChar[index] = '+';
		//cout << "+\n";
	}
	index++;
}
void print22() {
	int i = 0;
	for(i=0;i<index;i++)
		cout << printChar[i] << "\n";
}

int pop(int ans, int* arr) {
	if (arr[top] < ans) {
		cout << "NO";
		return 0;
	}

	print(1);
	return arr[top--];
}

void push(int* arr, int num) {
	print(0);

	arr[++top] = num;
}
#include <iostream>
using namespace std;
int tab[10][10];
int main()
{
	for (int i = 0; i < 10; i++) {
		for (int i2 = 0; i2 < 10; i2++) {
			if (i = i2) {
				tab[i][i2] = 1;
			}
			else {
				tab[i][i2] = 0;
			}
		}
	}
	for (int i = 0; i < 10; i++) {
		for (int i2 = 0; i2 < 10; i2++) {
			cout << tab[i][i2];
		}
		cout << endl;
	}
}

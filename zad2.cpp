#include <iostream>
using namespace std;
int tab[2][2];
int main()
{
	for (int i = 0; i < 2; i++) {
		for (int i2 = 0; i2 < 2; i2++) {
			cout << endl << "kolumna " << i + 1 << " wiersz " << i2 + 1 << ":" << endl;
			cin >> tab[i][i2];
		}
	}
	cout << (tab[0][0] * tab[1][1]) - (tab[0][1] * tab[1][0]);
}

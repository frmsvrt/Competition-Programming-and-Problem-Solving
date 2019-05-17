#include <iostream>
using namespace std;

int minCoins(int arr[], int S, int len) {
	if (S == 0) return 0;
	int res = INT_MAX;
	
	for (int i=0; i<len; i++)
		if (arr[i] <= S) {
			int sub_res = minCoins(arr, S-arr[i], len);
			if (sub_res != INT_MAX && sub_res + 1 < res)
				res = sub_res + 1;
		}

	return res;
}

int main() {
	int N, S;
	cin >> N >> S;

	int coins[N];

	for (int i=0; i<N; i++)
		cin >> coins[i];

	int len =  sizeof(coins)/sizeof(coins[0]);
	cout << "Min number of coins: " << minCoins(coins, S, len) << endl;
	return 0;
}

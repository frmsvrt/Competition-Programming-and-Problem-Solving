#include <iostream>
using namespace std;

int solver() {
	int ret;

	return ret;
}

int main() {
	int T, test_cases, N, i, ret;
	cin >> T;

	for (test_cases = 0; test_cases < T; test_cases++) {
		cin >> N;
		int locs[N];
		ret = 0;
		for (i = 0; i < N; i++)
				cin >> locs[i];

		for (auto& x : locs)
			ret += x;

		cout << "Sum of arr: " << ret << endl;
	}
	return 0;
}

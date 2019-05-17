// template.cpp
// template file for problim solving
// consist of main function that read size of array
// and then fill this array from cmd
// and solve method, empty ofcourse

#include <iostream>
#include <algorithm>
#include <limits.h>
#include <stdio.h>

int solve(int arr[], int size) {
	return 0;
}

int main() {
	int n, ret;
	std::cin >> n;

	// paste elements into seq
	int seq[n];
	for (int i = 0; i < n; i++) {
		std::cin >> seq[i];
	}

	// just for debug
	for (auto& x : seq) std::cout << x;
	std::cout << "\n";

	return 0;
}

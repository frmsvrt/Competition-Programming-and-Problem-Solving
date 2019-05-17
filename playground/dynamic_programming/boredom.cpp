// boredom.cpp
// Given a seq `a` of `n` integers
// Choose one element of `a` to delete,
// then all `a_k+1` and `a_k-1` will be deleted too
// that will brind a_k points;
// the goal is maximize points

#include <iostream>
#include <algorithm>
#include <limits.h>
#include <stdio.h>
#include <map>

int solve(int arr[], int size) {
	return 0;
}

int main() {
	int n, ret;
	std::cin >> n;
	std::map<int, int> freq;

	// paste elements into seq
	// count it freq
	int seq[n];
	for (int i = 0; i < n; i++) {
		std::cin >> seq[i];
		freq[seq[i]]++;
	}

	// max el of array
	auto max = *std::max_element(seq, seq + n);

	// go through the freq
	/***
	for (std::map<int, int>:: iterator it = freq.begin(); it != freq.end(); it++) {
		
	}
	***/
	for (auto it = begin(freq); it != end(freq); ++it) {
		std::cout << it->first << " " << it->second << std::endl;
	}

	return 0;
}

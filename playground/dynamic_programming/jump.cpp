// Minimum numbers of jumps to reach end
// First solution is kinda recursive approach
// Second one -- dynamic programming
#include <iostream>
#include <stdio.h>
#include <limits.h>
#include <algorithm>

int minJumps(int arr[], int start, int end) {
  if (end == start) return 0;

  if (arr[start] == 0) return INT_MAX;

  int min = INT_MAX;
  for (int i = start + 1; i <= end && i <= start + arr[start]; i++) {
    int jumps = minJumps(arr, i, end);
    if (jumps != INT_MAX && jumps + 1 < min)
      min = jumps + 1;
  }

  return min;
}


// function to solve this in O(n) time complexity
int minJumps2(int arr[], int n) {
  if (n <= 1) return 0;
  if (arr[0] == 0) return -1;

  int maxR = arr[0];
  int step = arr[0];
  int jump = 1;

  for (int i = 1; i < n; i++) {
    if (i == n - 1) return jump;
    maxR = std::max(maxR, i + arr[i]);
    step--;

    if (step == 0) {
      jump++;
      if (i >= maxR) return -1;
      step = maxR - i;
    }
  }
  return 0;
}

int minJumps3(int arr[], int n) {
  if (arr[0] == 0) return INT_MAX;
  if (n == 0) return INT_MAX;

  int jumps[n];
  jumps[0] = 0;

  for (int i = 1; i < n; i++) {
    jumps[i] = INT_MAX;
    for (int j = 0; j < i; j++) {
      if (i <= j + arr[j] && jumps[j] != INT_MAX) {
        jumps[i] = std::min(jumps[i], jumps[j] + 1);
        break;
      }
    }
  }

  return jumps[n - 1];
}

int main() {
  // int arr[] = {2, 5, 0, 0};
  int arr[] = {1, 3, 6, 3, 2, 3, 6, 8, 9, 5};
  int n = sizeof(arr) / sizeof(arr[0]);
  printf("Min number of jumps %d\n", minJumps(arr, 0, n - 1));
  printf("Min number of jumps %d\n", minJumps2(arr, n));
  printf("Min number of jumps %d\n", minJumps3(arr, n));
  return 0;
}

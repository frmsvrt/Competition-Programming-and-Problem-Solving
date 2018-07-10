// Minimum numbers of jumps to reach end
// First solution is kinda recursive approach
// Second one -- dynamic programming
#include <iostream>
#include <stdio.h>
#include <limits.h>

int minJumps(int arr[], int start, int end) {
  if (end == start) return 0;

  if (arr[start] == 0) return INT_MAX;

  int min = INT_MAX;
  for (int i = start+1; i <= end && i <= start + arr[start]; i++) {
    int jumps = minJumps(arr, i, end);
    if (jumps != INT_MAX && jumps + 1 < min)
      min = jumps + 1;
  }

  return min;
}

int main() {
  // int arr[] = {2, 5, 0, 0};
  int arr[] = {1, 3, 6, 3, 2, 3, 6, 8, 9, 5};
  int n = sizeof(arr)/sizeof(arr[0]);
  printf("Min number of jumps %d\n", minJumps(arr, 0, n - 1));
  return 0;
}

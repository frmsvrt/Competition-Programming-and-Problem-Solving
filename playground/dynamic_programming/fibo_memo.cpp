#include<stdio.h>
#include<iostream>
#define NIL -1
#define MAX 100

int lookup[100];

void _initialize() {
  for (int i = 0; i < MAX; i++) {
    lookup[i] = NIL;
  }
}

int fib(int n) {
  if (lookup[n] == NIL) {
    if (n <= 1)
      lookup[n] = n;
    else
      lookup[n] = fib(n-1) + fib(n-2);
  }
  return lookup[n];
}

int main() {
  int n;
  std::cin >> n;
  _initialize();
  printf("Fib number is %d \n", fib(n));
  return 0;
}

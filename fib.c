#include <stdio.h>
double fib(int n){
	double a=0.0, b=1.0, tmp;
	int i;
	for (i=0; i<n; ++i){
		tmp = a ;
		a = a+b;
		b = tmp;
	}
	return a;
}

int main(){
	int n = 1000;
	double res;
	res = fib(n);
	printf("\nfib of %d is %f\n",n,res);
	return 0;
}

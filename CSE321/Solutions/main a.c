#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>

int n, s;
long long *arr;
long long *result;
int *search;
void *searchFunc(void *arg);
void *fibonacci_generator(void *arg);

int main(){
	pthread_t thread1, thread2;

	printf("Enter the term of fibonacci sequence:\n");
	scanf("%d", &n);
	if (n<0 || n>40){
		printf("n must be between 0 and 40\n");
		return 1;
	}

	//thread1
	pthread_create(&thread1, NULL, fibonacci_generator, &n);
	pthread_join(thread1, (void **)&arr);

	for (int i=0; i<=n; i++){
		printf("a[%d] = %lld\n", i, arr[i]);
	}

	printf("How many numbers you are willing to search?:\n");
	scanf("%d", &s);

	if (s <= 0){
		printf("Number of searches must be greater than 0\n");
		free(arr);
		return 1;
	}

	search = malloc(sizeof(int)*s);

	for (int i=0; i<s; i++){
		printf("Enter search %d:\n", i+1);
		scanf("%d", &search[i]);
	}

	//thread2
	pthread_create(&thread2, NULL, searchFunc, NULL);
	pthread_join(thread2, (void **)&result);

	for (int i=0; i<s; i++){
		printf("result of search #%d = %lld\n", i+1, result[i]);
	}

	free(result);
    free(arr);
    free(search);
	return 0;
}

void *fibonacci_generator(void *arg){
	int n = *(int *)arg;
	long long *arr = malloc(sizeof(long long)*(n+1));
	
	arr[0]=0;
	if(n>=1) arr[1]=1;

	for (int i=2; i<=n; i++){
		arr[i] = arr[i-1] + arr[i-2];
	}
	return arr;
}

void *searchFunc(void *arg){
	long long *result = malloc(sizeof(long long)*s);

	for (int i=0; i<s; i++){
		if (search[i] < 0 || search[i] > n)
            result[i]=-1;
		else
			result[i] = arr[search[i]];
	}
	return result;
}

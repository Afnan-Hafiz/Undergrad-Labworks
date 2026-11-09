#include <stdio.h>
#include <unistd.h>
#include <semaphore.h>
#include <time.h>
#include <stdlib.h>
#include <pthread.h>

int N;
sem_t bc,cl,bl;
sem_t empty;

pthread_mutex_t lock;
void *maker(void *arg);
void *supplier(void *arg);

int main(){
	printf("Enter the number of times the supplier places ingredients:\n");
	scanf("%d", &N);
	srand(time(NULL));

	pthread_mutex_init(&lock, NULL);

	sem_init(&bc, 0, 0);
	sem_init(&cl, 0, 0);
	sem_init(&bl, 0, 0);
	sem_init(&empty, 0, 1);

	char nameA = 'A', nameB = 'B', nameC = 'C';
	pthread_t s, a, b, c;

	pthread_create(&s, NULL, supplier, NULL);
	pthread_create(&a, NULL, maker, &nameA);
	pthread_create(&b, NULL, maker, &nameB);
	pthread_create(&c, NULL, maker, &nameC);

	pthread_join(s,NULL);

	pthread_cancel(a);
	pthread_cancel(b);
	pthread_cancel(c);
	pthread_join(a, NULL);
	pthread_join(b, NULL);
	pthread_join(c, NULL);

	pthread_mutex_destroy(&lock);
	sem_destroy(&bc);
	sem_destroy(&cl);
	sem_destroy(&bl);
	sem_destroy(&empty);

	return 0;
}

void *supplier(void *arg){
	for (int i=0; i<N; i++){

		sem_wait(&empty);
		pthread_mutex_lock(&lock);
		int choice = rand() % 3;

		if (choice == 0)
			printf("Supplier places: Bread and Cheese\n");
		else if (choice == 1)
			printf("Supplier places: Cheese and Lettuce\n");
		else
			printf("Supplier places: Bread and Lettuce\n");

		pthread_mutex_unlock(&lock);

		if (choice==0) sem_post(&bc);
		else if (choice==1) sem_post(&cl);
		else sem_post(&bl);
	}

	sem_wait(&empty);
	return NULL;
}

void *maker(void *arg){
	char name = *(char *)arg;
	sem_t *mySem;
	char *ingredients;

	if (name == 'A'){
		mySem = &cl;
		ingredients = "Cheese and Lettuce";
	}
	else if (name == 'B'){
		mySem = &bl;
		ingredients = "Bread and Lettuce";
	}
	else {
		mySem = &bc;
		ingredients = "Bread and Cheese";
	}

	while(1){
		sem_wait(mySem);
		pthread_mutex_lock(&lock);
		
		printf("Maker %c picks up %s\n", name, ingredients);
		pthread_mutex_unlock(&lock);

		printf("Maker %c is making the sandwich...\n", name);
		printf("Maker %c finished making the sandwich and eats it\n", name);
		printf("Maker %c signals Supplier\n", name);

		sem_post(&empty);
	}
	return NULL;
}
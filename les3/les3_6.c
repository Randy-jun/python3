/*
 *
 * 这段代码是用C写一个简单的汉诺塔解决问题，并且记录时间
 *
 * */
#include<stdio.h>
#include<time.h>

void move(int n, char a, char b, char c)
{
	if(n == 1){
		printf("move %c ----> %c\n", a, c);
		return;
	}
	move(n - 1, a, c, b);
	printf("move %c ----> %c\n", a, c);
	move(n - 1, b, a, c);
}

int main()
{
	time_t t_start, t_end;
	int n = 50;
	char a, b, c;
	t_start = clock();
	move(n, 'A', 'B', 'C');
	t_end = clock();
	printf("Time: %.0f s\n", difftime(t_end, t_start));
	return 0;
}

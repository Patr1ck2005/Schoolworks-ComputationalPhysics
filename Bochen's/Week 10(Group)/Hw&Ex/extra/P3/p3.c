#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

#define pi 3.14159265358979

int n,N;
double sum,step;
time_t start,end;

double factorial(double m)   //计算真实值公式见document
{
	int i1;
	long double y1=1;
	for(i1=m;i1>=1;i1--)
	{
        	y1=y1*i1; 
	}
	return y1;
}

double double_factorial(double m)   
{
	int i2;
	double y2=1;
	for(i2=m;i2>=1;i2-=2)
	{
    		y2=y2*i2; 
	}
	return y2;
}

double n_dimensional(int n1)    //计算真实值，根据维数的奇偶分别计算
{
	double y;
	if(n1%2)
	{
       	y=pow(pi,(n1-1)/2)*pow(2,(n1+1)/2)/double_factorial(n1);
	}
	else
	{
		y=pow(pi,n1/2)/factorial(n1/2);
	}
	return y;
}

double fx(double *x)
{
	int i;
	double r=0;
	for(i=0;i<N;i++)
	{
		r+=x[i]*x[i];
	}
	if(r>1) return 0;
	else if(r<1) return 1;
	return 0.5;
}

void Circulation(int k,double *X,double *A,double a)   //递归法计算积分值    
{
	int i;
	if(k>=0)
	{
		for(X[k]=0,i=0;i<n;i++)
		{
			Circulation(k-1,X,A,a*A[i]);
			X[k]+=step;
		}
	}
	else
	{
		sum+=a*fx(X);
	}
}

void findn()     //根据维数选取不同的点数，即分段不同
{
	if(N<5) n=25;
	else if(N<=10) n=9+2*(9-N);
	else  n=5;
}

int main()
{
	int i,j;
	double result,real_V,error,X[20],A[25];
	FILE *fp1,*fp2;
	fp1=fopen("Volume.dat","w");
	fp2=fopen("error.dat","w");
	for(N=1;N<=14;N++)
	{
		start=time(NULL);
		real_V=n_dimensional(N);
		printf("%d_dimensional\nreal_V=%.15lf\n",N,real_V);     //输出真实值
		findn();
		
		A[0]=1;
		A[n-1]=1;
		for(j=1;j<(n-1);j+=2)A[j]=4;     //分配不同的权重
		for(j=2;j<(n-1);j+=2)A[j]=2;
	
		sum=0;
		step=1.0/(n-1);
		Circulation(N-1,X,A,1);
	
		for(j=0;j<N;j++) sum*=2*step/3;
		result=sum;
		end=time(NULL);
		error=fabs(real_V-result)/real_V;
		printf("result=%.15lf\trelative error=%.15lf%%\n",result,100*error);
		printf("time spend:%ld\n\n",(end-start));
		
		fprintf(fp1,"%d\t",N);               //输出数据到文件中
		fprintf(fp1,"%.15lf\t",real_V);
		fprintf(fp1,"%.15lf\n",result);
		fprintf(fp2,"%d\t",N);
		fprintf(fp2,"%.15lf\n",error);
		
	}
	fclose(fp1);
	fclose(fp2);
	return 0;
}











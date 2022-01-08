# include <stdio.h>
#include <stdlib.h>

//Trigonometric convertions


int main()
{
	//create variables
	int function,angle,divisor=360 ;
	char loop='Y';
	
	while(loop=='Y')
	{
		printf("Chose the function type you want to convert :\n ");
	printf(">>>>print 1 for sin() \n >>>>print 2 for cos() \n >>>>print 3 for tan() \n >>>>print 4 for cot() \n >>>>print 5 for sec() \n >>>>print 6 for csc() :");
	scanf("%d",&function);
	
	printf("Enter the vector angle :");
	scanf("%d",&angle);
	
	if(angle>=0)
	{
		angle=angle%divisor;
		printf("Simplified angle is %d \n",angle);
	}
	else if(angle<0)
	{
		angle=(angle%divisor)+360;
		printf("Simplified angle is %d \n",angle);
	}
	
	if(0<=angle and angle<=90)
	{
		if(function==1)
		{
			//sin function
			printf("sin%d is equal to cos%d",angle,90-angle);
		}
		
		else if(function==2)
		{
			//cos function
			printf("cos%d is equal to sin%d",angle,90-angle);
			
		}
		
		else if(function==3)
		{
			//tan function
			printf("tan%d is equal to cot%d",angle,90-angle);
			
		}
		
		else if(function==4)
		{
			//cot function
			printf("cot%d is equal to tan%",angle,90-angle);
		}
		
		else if(function==5)
		{
			//sec function
			printf("sec%d is equal to csc%d",angle,90-angle);
		}
		
		else if(function==6)
		{
			//csc function
			printf("csc%d is equal to sec%d",angle,90-angle);
		}
	}
	
	else if(90<=angle and angle<=180)
	{
		//angle is between 90 and 180
		
		if(function==1)
		{
			//sin function
			printf("sin%d is equal to sin%d\n",angle,180-angle);
			printf("sin%d is equal to cos%d",angle,angle-90);
		}
		
		else if(function==2)
		{
			//cos function
			printf("cos%d is equal to -cos%d\n",angle,180-angle);
			printf("cos%d is equal to -sin%d",angle,angle-90);
			
		}
		
		else if(function==3)
		{
			//tan function
			printf("tan%d is equal to -tan%d\n",angle,180-angle);
			
			printf("tan%d is equal to -cot%d",angle,angle-90);
			
		}
		
		else if(function==4)
		{
			//cot function
			printf("cot%d is equal to -cot%d\n",angle,180-angle);
			printf("cot%d is equal to -tan%d",angle,angle-90);
		}
		
		else if(function==5)
		{
			//sec function
			printf("sec%d is equal to -sec%d\n",angle,180-angle);
			printf("sec%d is equal to -csc%d",angle,angle-90);
		}
		
		else if(function==6)
		{
			//csc function
			printf("csc%d is equal to -csc%d\n",angle,180-angle);
			printf("csc%d is equal to -sec%d",angle,angle-90);
		}
		
	}
	
	else if(180<=angle and angle<=270)
	{
		//angle is between 180 and 270
		
		if(function==1)
		{
			//sin function
			printf("sin%d is equal to -sin%d\n",angle,angle-180);
			printf("sin%d is equal to -cos%d",angle,270-angle);
		}
		
		else if(function==2)
		{
			//cos function
			printf("cos%d is equal to -cos%d\n",angle,angle-180);
			printf("cos%d is equal to -sin%d",angle,270-angle);
			
		}
		
		else if(function==3)
		{
			//tan function
			printf("tan%d is equal to tan%d\n",angle,angle-180);
			
			printf("tan%d is equal to cot%d",angle,270-angle);
			
		}
		
		else if(function==4)
		{
			//cot function
			printf("cot%d is equal to cot%d\n",angle,angle-180);
			printf("cot%d is equal to tan%d",angle,270-angle);
		}
		
		else if(function==5)
		{
			//sec function
			printf("sec%d is equal to -sec%d\n",angle,angle-180);
			printf("sec%d is equal to -csc%d",angle,270-angle);
		}
		
		else if(function==6)
		{
			//csc function
			printf("csc%d is equal to -csc%d\n",angle,angle-180);
			printf("csc%d is equal to -sec%d",angle,270-angle);
		}
	}
	
	else if(270<=angle and angle<=360)
	{
		//angle is between 270 and 360
		if(function==1)
		{
			//sin function
			printf("sin%d is equal to -cos%d\n",angle,angle-270);
			printf("sin%d is equal to -sin%d",angle,360-angle);
		}
		
		else if(function==2)
		{
			//cos function
			printf("cos%d is equal to sin%d\n",angle,angle-270);
			printf("cos%d is equal to cos%d",angle,360-angle);
			
		}
		
		else if(function==3)
		{
			//tan function
			printf("tan%d is equal to -cot%d\n",angle,angle-270);
			
			printf("tan%d is equal to -tan%d",angle,360-angle);
			
		}
		
		else if(function==4)
		{
			//cot function
			printf("cot%d is equal to -tan%d\n",angle,angle-270);
			printf("cot%d is equal to -cot%d",angle,360-angle);
		}
		
		else if(function==5)
		{
			//sec function
			printf("sec%d is equal to -csc%d\n",angle,angle-270);
			printf("sec%d is equal to -sec%d",angle,360-angle);
		}
		
		else if(function==6)
		{
			//csc function
			printf("csc%d is equal to -sec%d\n",angle,angle-270);
			printf("csc%d is equal to -csc%d",angle,360-angle);
		}
	}
	
		printf("\nWould you like to continue ?(Y/N):");
		scanf(" %c",&loop);
		
	}
	
	printf("Program is being closed...");
	
	return 0;
}

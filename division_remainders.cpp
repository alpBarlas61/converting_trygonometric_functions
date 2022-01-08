#include <stdio.h>
#include <stdlib.h>

//Finding basic angle in trigonometry

int main()
{
	int angle,divisor=360,smplfd_angle;
	
	printf("Enter the angle value :");
	scanf("%d",&angle);//Take the user input for angle
	
	if(angle>=0)
	{
		smplfd_angle=angle%divisor;// % operator gives the remainder of calculations, divisor is 360 beacuse of circle
		printf("The simplified angle is %d",smplfd_angle);//In this case remainder is being callled as simplified angle
	}
	
	else if(angle<0)
	{
		smplfd_angle=angle%divisor;
		printf("The simplified angle is %d",smplfd_angle+360);
	}
	
	return 0;
}

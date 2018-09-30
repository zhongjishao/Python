numbers=[17,5,34,6,3,9,28,13,16,28];
print numbers
count=len(numbers);
i=1;
for i in range(1,count):
  j=0;
  for j in range(0,i):
      if(numbers[i]<numbers[j]):
          temp=numbers[i];
          numbers[i]=numbers[j];
          numbers[j]=temp;
j=j+1
print numbers;

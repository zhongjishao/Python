#!
class Number:
   num=0
   def init(self):
     self.num+=1
	
m1=Number();
m2=Number();

#m2.num=5;
m1.init();
m2.init();
print m2.num
m1.init();
print m1.num

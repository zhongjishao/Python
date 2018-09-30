class Filter:
  def init(self):
    self.blocked=[]
  def filter(self,sequence):
    for x in sequence:
      if x not in self.blocked:
        return x
class SPAMFilter(Filter):
  def init(self):
    self.blocked=['hi']
	
f=SPAMFilter()
f.init()
seq=['hi','hello','hi','nice','good']
seq=f.filter(seq)
print seq

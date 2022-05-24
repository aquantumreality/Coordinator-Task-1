class pair:
    def __init__(self,input,target):
        self.input = input
        self.target = target
        
    def findpair(self):
        dict = {}
        c = 1
        for i in range(len(self.input)):
           for j in range(len(self.input)):
               if(self.input[i]+self.input[j] == self.target and i!=j):
                   dict[c] = [i,j]
                   c = c+1
        return dict


input = [10,20,10,40,50,60,70]
target = 50
list = pair(input,target)
print(list.findpair())
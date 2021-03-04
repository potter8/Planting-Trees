#get input
x=input()
#store input in list 
tree=list(map(int,input().split()))
#sort days in decreasing order #ex: 4 -> 1

tree=sorted(tree, reverse=True)
# index +1
# for loop in range days

for i in range (len(tree)):
  tree[i] = tree[i] + i + 1
  
m = max(tree) + 1

print(m)




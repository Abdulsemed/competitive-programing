ans.append("p")
queue.append(TreeNode(0))
if curr.right:
ans.append(str(abs(curr.right.val)))
ans.append("p" if curr.right.val >= 0 else "n")
queue.append(curr.right)
sets.add(curr.right.val)
else:
ans.append("l")
ans.append("p")
queue.append(TreeNode(0))
if not sets:
break
ans = "".join(ans)
return ans
def deserialize(self, data):
"""Decodes your encoded data to tree.
:type data: str
:rtype: TreeNode
"""
index = 0
holder = []
while index < len(data):
val = 0
if data[index] == "l":
holder.append(1001)
index += 1
else:
while data[index] != "p" and data[index] != "n":
val = val * 10 + int(data[index])
index += 1
if data[index] == "n":
holder.append(-val)
else:
holder.append(val)
index += 1
data = holder
if data:
root = TreeNode(int(data[0]))
dicts = {0:root}
size = len(data)
for index in range(size):
if data[index] != 1001:
val = (2*index)+1
if data[val] != 1001:
left = TreeNode(data[val])
dicts[val] = left
dicts[index].left = left
val += 1
if data[val] != 1001:
right = TreeNode(data[val])
dicts[val] = right
dicts[index].right = right
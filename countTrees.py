def countTrees(nodes, aux):
  if(nodes==0 or nodes==1):
    return 1;
  else:
    sum = 0
    for index in range(0,nodes):
      left = aux[index] if len(index+1)>=nodes else countTrees(index)
      right = aux[nodes-index] if len(aux)>=nodes else countTrees(nodes-index)
      aux[nodes]+= left+right
    return aux[nodes]

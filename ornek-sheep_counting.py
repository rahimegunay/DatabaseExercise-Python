def count_sheep(n):
  sheep=""
  for i in range(n):
    sheep += f"{i+1} sheep...."
  print(sheep) 

count_sheep(5)

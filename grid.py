row = True #if it is a row
rows = 5
for i in range(2*rows+1): #create the rows, and a container at one end
  string = ""
  if row:
    for j in range(2*rows+1): #if it is a row, we need two per column, and 1 for the final crossing
      string += "-"
    row = False
  else:
    for j in range(rows+1): #if it is a column, we need 1 column and space, and 1 bar for the end
      string += "| "
    row = True
  print(string) #print each row/column

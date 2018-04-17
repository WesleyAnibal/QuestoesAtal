

string1 = input()
string2 = input()

def lcs(string1, string2):
  maior = 0
  matrix = [[0 for i in range(len(string2)+1)] for j in range(len(string1)+1)]
  for i in range(1, len(string1)+1):
    for j in range(1, len(string2)+1):
      if(string1[i-1] == string2[j-1]):
        matrix[i][j] = matrix[i-1][j-1]+1
        if(matrix[i][j]> maior):
          maior = matrix[i][j]
  return maior

print(lcs(string1, string2))
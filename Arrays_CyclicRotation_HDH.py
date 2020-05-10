def solution(A, K):

  cond_1 = 0
  cond_2 = 0
  l=len(A)

  for i in range (0, l) :
    if A[i] > 1000 or A[i] < -1000 :
      cond_1 = 1
      break

  if K > 100 or l > 100 : 
    cond_2 = 1

  if cond_1 == 1 and cond_2 == 0 :
    print("------------------Result------------------")
    print("Error => (N<-1000) or (N>1000)")

  elif cond_2 == 1 and cond_1 == 0 :
    print("------------------Result------------------")
    print("Error => (K>100) or (Length of A>100)")
  
  elif cond_1 == 1 and cond_2 == 1 :
    print("------------------Result------------------")
    print("Error => ((N<-1000) or (N>1000)) and ((K>100) or (Length of A>100))")

  else :

    if l < K :
      s = K % l

    else :
      s = K

    A_left = A[l-s:l]
    A_right = A[0:l-s]

    for i in range (0,l-s):
      A_left.append(A_right[i])

    print("------------------Result------------------")
    print("Shifted Array :", A_left)


A = list(map(int, input("insert array A : ").split()))
K = int(input("insert K : "))

solution(A, K)
 

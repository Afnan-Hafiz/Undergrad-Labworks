d = {"1":[".",",","?","!",":"],"2":["A","B","C"],"3":["D","E","F"],"4":["G","H","I"],"5":["J","K","L"],"6":["M","N","O"],"7":["P","Q","R","S"],"8":["T","U","V"],"9":["W","X","Y","Z"],"0":[" "]}
inp = input()
inp = inp.upper()
for i in inp:
    for k,v in d.items():
      if i in v:
        for j in range(len(v)):
          if v[j] == i:
            for i in range(j+1):
              print(k,end="")
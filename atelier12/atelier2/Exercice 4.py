s1 = {23,42,65,57,78,83,29}
s2 = {57,83,29,67,73,43,48}

inters = s1&s2 # l'intersection de deux Sets s1 et s2 = {57,83,29}

print(inters)

s1 = s1 - inters # suprrimer le set (inters = {57,83,29}) dans s1 => s1 ={65,42,78,23}

print(s1)




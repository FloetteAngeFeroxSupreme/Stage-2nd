suite = [0, 1]
for i in range(2, int(input("combien de termes voulez-vous afficher?"))):
    suite.append(suite[i-1] + suite[i-2])
print(suite)
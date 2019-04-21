from sklearn.metrics import explained_variance_score

g = avarage = explained_variance_score(
    [2], [2.1],  multioutput='uniform_average')

print(g)

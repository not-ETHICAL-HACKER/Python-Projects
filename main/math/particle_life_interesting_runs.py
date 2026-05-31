import pickle

with open("matrices.pkl", "rb") as f,open("fav_matrices.pkl", "ab") as f2:
    data = pickle.load(f)
    print(data)
    pickle.dump(data, f2)
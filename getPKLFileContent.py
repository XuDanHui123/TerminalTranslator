import pickle

f = open("./config.pkl", "rb")
x = pickle.load(f)
print("config.pkl:", x)
f.close()

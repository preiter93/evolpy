import numpy as np
import matplotlib.pyplot as plt

files = ["cr002.txt","cr01.txt", "cr02.txt", "cr05.txt", "cr1.txt"]
titles = ["c-rate = 0.02", "c-rate = 0.1", "c-rate = 0.2", "c-rate = 0.5", "c-rate = 1"]
for file, title in zip(files, titles):
    data = np.loadtxt(file)
    i = [str(i) for i in range(len(data))]
    plt.scatter(i, data/124, label=title, s=10)
plt.legend()
plt.xticks([0, 1000])
plt.xlabel("Generation")
plt.ylabel("Fitness")
plt.savefig("c_rate.png")
plt.show()

files = ["pr002.txt","pr01.txt", "pr02.txt", "pr05.txt", "pr08.txt"]
titles = ["p-rate = 0.02", "p-rate = 0.1", "p-rate = 0.2", "p-rate = 0.5", "p-rate = 0.8"]
for file, title in zip(files, titles):
    data = np.loadtxt(file)
    i = [str(i) for i in range(len(data))]
    plt.scatter(i, data/124, label=title, s=10)
plt.legend()
plt.xticks([0, 1000])
plt.xlabel("Generation")
plt.ylabel("Fitness")
plt.savefig("p_rate.png")
plt.show()

files = ["mr002.txt","mr01.txt", "mr02.txt", "mr05.txt", "mr08.txt"]
titles = ["m-rate = 0.02", "m-rate = 0.1", "m-rate = 0.2", "m-rate = 0.5", "m-rate = 0.8"]
for file, title in zip(files, titles):
    data = np.loadtxt(file)
    i = [str(i) for i in range(len(data))]
    plt.scatter(i, data/124, label=title, s=10)
plt.legend()
plt.xticks([0, 1000])
plt.xlabel("Generation")
plt.ylabel("Fitness")
plt.savefig("m_rate.png")
plt.show()

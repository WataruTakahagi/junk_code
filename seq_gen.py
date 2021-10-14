
import numpy as np
file, seq, dna_length = open("sequence.txt","w"), str(), int(input("DNA Length : "))
for i in range(dna_length): seq += np.random.choice(["A","T","G","C"])
file.write(seq)
file.close()

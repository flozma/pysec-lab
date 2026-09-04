from datasketch import MinHash


data1 = ["minhash", "python", "tutorial", "similarity", "big", "data"]
data2 = ["minhash", "python", "code", "similarity", "large", "scale"]

# Create MinHash objects with a fixed number of permutation functions / hash functions (num_perm)
# It is the random seed used to generate the fixed number of permutation functions / hash functions.
min_h1 = MinHash(num_perm=64, seed=42)
min_h2 = MinHash(num_perm=64, seed=42)

# Update the MinHash structures with data strings encoded into bytes
for token in data1:
  min_h1.update(token.encode())  # default parameter of encode is 'utf-8'

for token in data2:
  min_h2.update(token.encode())  # default parameter of encode is 'utf-8'

# Jaccard Index from the compressed signature
jaccard_index = min_h1.jaccard(min_h2)

print(min_h1.digest())
print(min_h2.digest())

set1 = set(data1)
set2 = set(data2)
true_jaccard = len(set1.intersection(set2)) / len(set1.union(set2))

print(f"Estimated Jaccard Similarity: {jaccard_index:.4f}")
print(f"True jaccard index:           {true_jaccard:.4f}")

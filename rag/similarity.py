from math import sqrt

def cosine_similarity(vector1, vector2):
    dot = sum(a * b for a, b in zip(vector1, vector2))
    norm1 = sqrt(sum(x * x for x in vector1))
    norm2 = sqrt(sum(x * x for x in vector2))
    if norm1 == 0 or norm2 == 0:
        return 0
    else:
        return dot / (norm1 * norm2)


import numpy as np
def embedding_via_one_hot(token_ids,W):
    vocab_size=W.shape[0]
    H=np.zeros((len(token_ids),vocab_size))
    for i,token in enumerate(token_ids):
        H[i,token]=1
    return H@W
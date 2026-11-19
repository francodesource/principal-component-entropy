import numpy as np

def pc_entropy(x: np.ndarray):
    """ 
    Compute the PC-entropy for a matrix.  
    
    Args:
        x (np.ndarray): a matrix (..., N , M ) where N is the number of samples and M is the number of channels

    Return:
        The PC-entropy value. For matrices with more than two dimensions the PC-entropy will be iterated along the other dimensions.

    """
    channels_index = -1  
    samples_index = -2
    samples_n = x.shape[samples_index] # N
    channels_n = x.shape[channels_index] # M

    # computing covariance matrixes
    c = x - x.mean(axis=samples_index, keepdims=True)
    c_t = np.swapaxes(c, samples_index, channels_index)
    cov =  c_t @ c / (samples_n - 1)

    assert cov.shape[-2:] == (channels_n, channels_n)

    # compute the eigenvalues
    lam = np.linalg.eigvalsh(cov)
    lam = np.clip(lam, 0, None) # Clipping minimum value to avoid numerical errors

    # normalize the eigenvalues
    p = lam / lam.sum(axis=-1, keepdims=True)

    plogp = np.where(p > 0, p * np.log2(np.where(p > 0, p, 1)), 0.0)

    return  -plogp.sum(axis=-1) / np.log2(channels_n)
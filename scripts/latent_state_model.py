import numpy as np
from hmmlearn import hmm

class LatentStateModel:
    """
    Hidden Markov Model for modeling latent health states over time.
    """

    def __init__(self, n_states=3, n_iter=100):
        """
        Initialize the HMM model.
        
        Parameters:
        - n_states: number of hidden states (e.g., low/moderate/high risk)
        - n_iter: max iterations for training
        """
        self.n_states = n_states
        self.model = hmm.GaussianHMM(n_components=n_states, covariance_type='diag', n_iter=n_iter, verbose=True)

    def fit(self, X):
        """
        Train the HMM on data X.
        
        X: np.ndarray of shape (n_samples, n_features)
        """
        self.model.fit(X)

    def predict_states(self, X):
        """
        Predict latent states for observations X.
        
        Returns:
        - states: np.ndarray of shape (n_samples,)
        """
        return self.model.predict(X)

    def get_model_params(self):
        """
        Return model parameters like transition matrix, means, covariances.
        """
        return {
            'transmat': self.model.transmat_,
            'startprob': self.model.startprob_,
            'means': self.model.means_,
            'covars': self.model.covars_
        }
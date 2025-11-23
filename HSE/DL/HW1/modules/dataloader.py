import numpy as np

class DataLoader(object):
    """
    Tool for shuffling data and forming mini-batches
    """
    def __init__(self, X, y, batch_size=1, shuffle=False):
        """
        :param X: dataset features
        :param y: dataset targets
        :param batch_size: size of mini-batch to form
        :param shuffle: whether to shuffle dataset
        """
        assert X.shape[0] == y.shape[0]
        self.X = X
        self.y = y
        self.batch_size = batch_size
        self.shuffle = shuffle
        self.batch_id = 0  # use in __next__, reset in __iter__
        self.indices = None

    def __len__(self) -> int:
        """
        :return: number of batches per epoch
        """
        # Number of batches = ceil(num_samples / batch_size)
        return (self.X.shape[0] + self.batch_size - 1) // self.batch_size

    def num_samples(self) -> int:
        """
        :return: number of data samples
        """
        return self.X.shape[0]

    def __iter__(self):
        """
        Shuffle data samples if required
        :return: self
        """
        # Reset batch index
        self.batch_id = 0
        
        # Create or shuffle indices
        self.indices = np.arange(self.X.shape[0])
        if self.shuffle:
            np.random.shuffle(self.indices)
        
        return self

    def __next__(self):
        """
        Form and return next data batch
        :return: (x_batch, y_batch)
        """
        if self.batch_id >= len(self):
            raise StopIteration
        
        # Get batch indices
        start_idx = self.batch_id * self.batch_size
        end_idx = min(start_idx + self.batch_size, self.X.shape[0])
        batch_indices = self.indices[start_idx:end_idx]
        
        # Get batch data
        X_batch = self.X[batch_indices]
        y_batch = self.y[batch_indices]
        
        # Increment batch counter
        self.batch_id += 1
        
        return X_batch, y_batch

import numpy as np
from .base import Criterion
from .activations import LogSoftmax


class MSELoss(Criterion):
    """
    Mean squared error criterion
    """
    def compute_output(self, input: np.ndarray, target: np.ndarray) -> float:
        """
        :param input: array of size (batch_size, *)
        :param target:  array of size (batch_size, *)
        :return: loss value
        """
        assert input.shape == target.shape, 'input and target shapes not matching'
        # Mean squared error: (1/BN) * sum((input - target)^2)
        diff = input - target
        return np.mean(diff * diff)

    def compute_grad_input(self, input: np.ndarray, target: np.ndarray) -> np.ndarray:
        """
        :param input: array of size (batch_size, *)
        :param target:  array of size (batch_size, *)
        :return: array of size (batch_size, *)
        """
        assert input.shape == target.shape, 'input and target shapes not matching'
        # Gradient of MSE: (2/BN) * (input - target)
        return 2.0 * (input - target) / input.size


class CrossEntropyLoss(Criterion):
    """
    Cross-entropy criterion over distribution logits
    """
    def __init__(self, label_smoothing: float = 0.0):
        super().__init__()
        self.log_softmax = LogSoftmax()
        self.label_smoothing = label_smoothing

    def compute_output(self, input: np.ndarray, target: np.ndarray) -> float:
        """
        :param input: logits array of size (batch_size, num_classes)
        :param target: labels array of size (batch_size, )
        :return: loss value
        """
        # Use log-softmax for numerical stability
        log_probs = self.log_softmax.forward(input)
        batch_size = input.shape[0]
        
        # Select log probabilities for the correct class
        # Create one-hot encoding  
        if self.label_smoothing > 0:
            num_classes = input.shape[1]
            smooth_labels = np.zeros_like(log_probs)
            smooth_labels[np.arange(batch_size), target] = 1 - self.label_smoothing
            smooth_labels += self.label_smoothing / num_classes
            loss = -np.sum(smooth_labels * log_probs) / batch_size
        else:
            loss = -log_probs[np.arange(batch_size), target].mean()
        
        return loss

    def compute_grad_input(self, input: np.ndarray, target: np.ndarray) -> np.ndarray:
        """
        :param input: logits array of size (batch_size, num_classes)
        :param target: labels array of size (batch_size, )
        :return: array of size (batch_size, num_classes)
        """
        batch_size = input.shape[0]
        
        # Compute softmax probabilities  
        probs = np.exp(self.log_softmax.output)
        
        # Create gradient tensor
        grad = probs.copy()
        
        if self.label_smoothing > 0:
            num_classes = input.shape[1]
            smooth_labels = np.zeros_like(grad)
            smooth_labels[np.arange(batch_size), target] = 1 - self.label_smoothing
            smooth_labels += self.label_smoothing / num_classes
            grad = (probs - smooth_labels) / batch_size
        else:
            # Subtract 1 from the probability of the correct class
            grad[np.arange(batch_size), target] -= 1
            # Average over batch
            grad /= batch_size
        
        return grad

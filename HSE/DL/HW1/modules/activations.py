import numpy as np
from scipy import special
from .base import Module


class ReLU(Module):
    """
    Applies element-wise ReLU function
    """
    def compute_output(self, input: np.ndarray) -> np.ndarray:
        """
        :param input: array of an arbitrary size
        :return: array of the same size
        """
        return np.maximum(input, 0)

    def compute_grad_input(self, input: np.ndarray, grad_output: np.ndarray) -> np.ndarray:
        """
        :param input: array of an arbitrary size
        :param grad_output: array of the same size
        :return: array of the same size
        """
        return grad_output * (input > 0)


class Sigmoid(Module):
    """
    Applies element-wise sigmoid function
    """
    def compute_output(self, input: np.ndarray) -> np.ndarray:
        """
        :param input: array of an arbitrary size
        :return: array of the same size
        """
        return 1.0 / (1.0 + np.exp(-input))

    def compute_grad_input(self, input: np.ndarray, grad_output: np.ndarray) -> np.ndarray:
        """
        :param input: array of an arbitrary size
        :param grad_output: array of the same size
        :return: array of the same size
        """
        sigmoid = self.output  # reuse forward output
        return grad_output * sigmoid * (1 - sigmoid)


class GELU(Module):
    """
    Applies element-wise GELU function
    """
    def compute_output(self, input: np.ndarray) -> np.ndarray:
        """
        :param input: array of an arbitrary size
        :return: array of the same size
        """
        # GELU(x) = x * Phi(x) where Phi is the CDF of standard normal
        return input * special.ndtr(input)

    def compute_grad_input(self, input: np.ndarray, grad_output: np.ndarray) -> np.ndarray:
        """
        :param input: array of an arbitrary size
        :param grad_output: array of the same size
        :return: array of the same size
        """
        # d/dx(x * Phi(x)) = Phi(x) + x * phi(x)
        # where phi(x) is the PDF of standard normal
        phi_x = special.ndtr(input)
        pdf_x = np.exp(-0.5 * input**2) / np.sqrt(2 * np.pi)
        return grad_output * (phi_x + input * pdf_x)


class Softmax(Module):
    """
    Applies Softmax operator over the last dimension
    """
    def compute_output(self, input: np.ndarray) -> np.ndarray:
        """
        :param input: array of size (batch_size, num_classes)
        :return: array of the same size
        """
        # Numerically stable softmax
        exp_input = np.exp(input - input.max(axis=-1, keepdims=True))
        return exp_input / exp_input.sum(axis=-1, keepdims=True)

    def compute_grad_input(self, input: np.ndarray, grad_output: np.ndarray) -> np.ndarray:
        """
        :param input: array of size (batch_size, num_classes)
        :param grad_output: array of the same size
        :return: array of the same size
        """
        # Jacobian of softmax is softmax_i * (delta_ij - softmax_j)
        softmax = self.output  # reuse forward output
        grad_sum = (grad_output * softmax).sum(axis=-1, keepdims=True)
        return softmax * (grad_output - grad_sum)


class LogSoftmax(Module):
    """
    Applies LogSoftmax operator over the last dimension
    """
    def compute_output(self, input: np.ndarray) -> np.ndarray:
        """
        :param input: array of size (batch_size, num_classes)
        :return: array of the same size
        """
        # Numerically stable log-softmax
        shifted = input - input.max(axis=-1, keepdims=True)
        return shifted - np.log(np.exp(shifted).sum(axis=-1, keepdims=True))

    def compute_grad_input(self, input: np.ndarray, grad_output: np.ndarray) -> np.ndarray:
        """
        :param input: array of size (batch_size, num_classes)
        :param grad_output: array of the same size
        :return: array of the same size
        """
        # Gradient of log-softmax
        softmax = np.exp(self.output)  # exp(log_softmax) = softmax
        grad_sum = grad_output.sum(axis=-1, keepdims=True)
        return grad_output - softmax * grad_sum

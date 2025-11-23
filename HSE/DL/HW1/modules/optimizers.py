import numpy as np
from typing import Tuple
from .base import Module, Optimizer


class SGD(Optimizer):
    """
    Optimizer implementing stochastic gradient descent with momentum
    """
    def __init__(self, module: Module, lr: float = 1e-2, momentum: float = 0.0,
                 weight_decay: float = 0.0, nesterov: bool = False):
        """
        :param module: neural network containing parameters to optimize
        :param lr: learning rate
        :param momentum: momentum coefficient (alpha)
        :param weight_decay: weight decay (L2 penalty)
        """
        super().__init__(module)
        self.lr = lr
        self.momentum = momentum
        self.weight_decay = weight_decay
        self.nesterov = nesterov

    def step(self):
        parameters = self.module.parameters()
        gradients = self.module.parameters_grad()
        if 'm' not in self.state:
            self.state['m'] = [np.zeros_like(param) for param in parameters]

        for param, grad, m in zip(parameters, gradients, self.state['m']):
            # Apply weight decay
            if self.weight_decay != 0:
                grad = grad + self.weight_decay * param
            
            # Update momentum
            np.multiply(self.momentum, m, out=m)
            np.add(m, grad, out=m)
            
            # Update parameters
            if self.nesterov:
                # Nesterov momentum: param = param - lr * (grad + momentum * m)
                np.subtract(param, self.lr * (grad + self.momentum * m), out=param)
            else:
                # Standard momentum: param = param - lr * m
                np.subtract(param, self.lr * m, out=param)


class Adam(Optimizer):
    """
    Optimizer implementing Adam
    """
    def __init__(self, module: Module, lr: float = 1e-3,
                 betas: Tuple[float, float] = (0.9, 0.999),
                 eps: float = 1e-8, weight_decay: float = 0.0):
        """
        :param module: neural network containing parameters to optimize
        :param lr: learning rate
        :param betas: Adam beta1 and beta2
        :param eps: Adam eps
        :param weight_decay: weight decay (L2 penalty)
        """
        super().__init__(module)
        self.lr = lr
        self.beta1 = betas[0]
        self.beta2 = betas[1]
        self.eps = eps
        self.weight_decay = weight_decay

    def step(self):
        parameters = self.module.parameters()
        gradients = self.module.parameters_grad()
        if 'm' not in self.state:
            self.state['m'] = [np.zeros_like(param) for param in parameters]
            self.state['v'] = [np.zeros_like(param) for param in parameters]
            self.state['t'] = 0

        self.state['t'] += 1
        t = self.state['t']
        for param, grad, m, v in zip(parameters, gradients, self.state['m'], self.state['v']):
            # Apply weight decay
            if self.weight_decay != 0:
                grad = grad + self.weight_decay * param
            
            # Update biased first moment estimate
            np.multiply(self.beta1, m, out=m)
            np.add(m, (1 - self.beta1) * grad, out=m)
            
            # Update biased second moment estimate
            np.multiply(self.beta2, v, out=v)
            np.add(v, (1 - self.beta2) * (grad * grad), out=v)
            
            # Compute bias-corrected first moment estimate
            m_corrected = m / (1 - self.beta1 ** t)
            
            # Compute bias-corrected second moment estimate
            v_corrected = v / (1 - self.beta2 ** t)
            
            # Update parameters
            np.subtract(param, self.lr * m_corrected / (np.sqrt(v_corrected) + self.eps), out=param)

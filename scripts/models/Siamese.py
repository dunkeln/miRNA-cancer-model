import torch
import torch.nn as nn
import torch.functional as F
from typing import Tuple


class ConvNet(nn.Module):
    def __init__(self, input_dim: Tuple):
        super(ConvNet, self).__init__()
        self.cnn_stack()

class Siamese(nn.Module):
    def __init__(self):
        super(Siamese, self).__init__()
        
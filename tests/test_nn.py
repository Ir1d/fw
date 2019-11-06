import torch
import torch.nn as nn
from torch.autograd import gradcheck
from fw.nn import PixelUnShuffle, Swish
import math

def test_PixelUnshuffle():
    """Test nn.PixelUnshuffle()
    """
    pass

def test_Swish():
    """Test nn.Swish()
    """

    def sigmoid(x):
        return 1 / (1 + math.exp(-x))

    swish = Swish()
    input = (torch.randn(20, 20, dtype=torch.double, requires_grad=True))
    test = gradcheck(swish, input, eps=1e-6, atol=1e-4)
    assert(test == True)

    input = torch.zeros((1))
    res = swish(input)
    assert(res == 0)
    input = torch.tensor([1.0])
    res = swish(input)
    assert(res == sigmoid(1))


    

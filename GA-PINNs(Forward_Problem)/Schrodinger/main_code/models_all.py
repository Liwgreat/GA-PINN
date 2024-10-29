import numpy as np
import torch
from torch import nn, optim, autograd
from torch.nn import functional as F

def weights_init(m):
    if isinstance(m, nn.Linear):
        nn.init.xavier_normal_(m.weight)
        nn.init.constant_(m.bias, 0)
    elif isinstance(m, nn.Conv2d):
        #nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
        nn.init.xavier_normal_(m.weight)
        nn.init.constant_(m.bias, 0)
    elif isinstance(m, nn.BatchNorm2d):
        nn.init.constant_(m.weight, 1)
        nn.init.constant_(m.bias, 0)

class hidden_layers(nn.Module):
    def __init__(self,input_number,output_number):
        super(hidden_layers, self).__init__()
        self.layer = nn.Linear(input_number,output_number)
    def forward(self, x):
        x = self.layer(x)
        x = torch.tanh(x)
        return x

class NN_H2 (nn.Module):
    def __init__(self,in_N, width, depth, out_N):
        #depth = layers-2
        super(NN_H2, self).__init__()
        self.in_N = in_N
        self.width = width
        self.depth = depth
        self.out_N = out_N

        self.stack = nn.ModuleList()

        self.stack.append(hidden_layers(in_N, width))

        for i in range(depth):
            self.stack.append(hidden_layers(width, width))

        self.stack.append(nn.Linear(width, out_N))
        
        
    def forward(self, x):
        for m in self.stack:
            x = m(x)
        return x

class get_discriminator(nn.Module):
    def __init__(self,in_N, width, depth, out_N):
 
        super(get_discriminator, self).__init__()
        self.in_N = in_N
        self.width = width
        self.depth = depth
        self.out_N = out_N

        self.stack = nn.ModuleList()

        self.stack.append(hidden_layers(in_N, width))

        for i in range(depth):
            self.stack.append(hidden_layers(width, width))

        self.stack.append(nn.Linear(width, out_N))
        
        
    def forward(self, x):
        for m in self.stack:
            x = m(x)
            x = torch.sigmoid(x)
        return x 

def relative_l2(u_pred,u_real):
    l2 = np.linalg.norm(u_real-u_pred,2)/np.linalg.norm(u_real,2)
    return l2



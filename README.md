# GA-PINN


### Initial Work:
[Revisiting PINNs: Generative Adversarial Physics-Informed Neural Networks and Point-Weighting Method](https://arxiv.org/abs/2205.08754)

### Current Version:
[Generative adversarial physics-informed neural networks for solving forward and inverse problem with small labeled samples](https://www.sciencedirect.com/science/article/abs/pii/S089812212500032X)


### Please note:
The observation data is important for PINNs to solve inverse problems. We take the three well-known PDE (Burgers, Allen-Cahn and reaction-diffusion) inverse problems as the examples. The structure of the discriminator should be similar to that of the generator. Especially, the discriminator has half the number of layers as the generator due to the size of labeled samples is small.


### Requirements
[Details in requirements.md](requirements.md)  

![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)
![PyDOE Version](https://img.shields.io/badge/PyDOE-0.3.8-blue.svg)
![PyTorch Version](https://img.shields.io/badge/pytorch-1.10.0-brightgreen.svg)


## Folder tree
```plaintext
Different Method/
├── experimental_data # Data from Experimental Results
├── figures # Images Created from Data Derived from Experimental Results
├── main_code
│   ├── example.ipynb
│   └── models_all.py # Network Architecture Code
├── plot_code 
└── saved_model # Saving the Experimental Result Model
```

## GA-PINN in Solving Forward problems
### Code
- GA-PINN [Forward problems]
    - [Burgers](/GA-PINNs(Forward_Problem)/Burgers)
    - [Heat](/GA-PINNs(Forward_Problem)/Heat)
    - [Helmholtz](/GA-PINNs(Forward_Problem)/Helmholtz)
    - [HD-Poisson](/GA-PINNs(Forward_Problem)/Poisson-HD)
    - [Poisson](/GA-PINNs(Forward_Problem)/Poisson)
    - [Schrödinger](/GA-PINNs(Forward_Problem)/Schrodinger)

## GA-PINN in Solving Inverse problems
### Code
- GA-PINN [Inverse problems]
    - [Allen-Cahn](/GA-PINNs(Inverse_Problem)/Allen-Cahn)
    - [Burgers](/GA-PINNs(Inverse_Problem)/Burgers)
    - [Diffusion Equation](/GA-PINNs(Inverse_Problem)/Diffusion)
    - [Lorenz System](/GA-PINNs(Inverse_Problem)/Lorenz_System)


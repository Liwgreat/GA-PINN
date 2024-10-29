# GA-PINN


### Initial Work Reference:
[Revisiting PINNs: Generative Adversarial Physics-Informed Neural Networks and Point-Weighting Method](https://arxiv.org/abs/2205.08754)

### Please note:
- The forward problems in this repository utilize PyTorch version **1.10.0**.
- The inverse problems are implemented using PyTorch version **1.9.0** to meet basic requirements.

"GA-PINNs: Generative Adversarial Physics-informed Neural Networks for Solving Forward and Inverse PDE Problem with Small Labeled Samples
Introduction"

Physics-informed neural networks (PINNs) provide a deep learning framework for numerically solving partial differential equations (PDEs), but there still remain some challenges in the application of PINNs, for example, how to exhaustively utilize a small size of (usually very few) labeled samples, which are the exact solutions to the PDEs or their high-accuracy approximations, to improve the accuracy and the training efficiency. In this paper, we propose the generative adversarial physics-informed neural networks (GA-PINNs), which integrate the generative adversarial (GA) mechanism with original PINNs, to improve the performance of PINNs by exploiting a small size of labeled samples. The numerical experiments show that, compared with the original PINNs equipped with an additive loss computed on these labeled samples, GA-PINNs can more effectively utilize the small labeled samples when solving forward and inverse problems. As a generalization of GA-PINNs, we also combine the GA mechanism with the deep Ritz method (DRM) and the deep Galerkin method (DGM) to form GA-DRM and GA-DGM, respectively. The experimental results validate their superiority as well.


## Usage for Academic Purposes

This code is provided for academic purposes related to the submission of our paper titled "GA-PINNs: Generative Adversarial Physics-informed Neural Networks for Solving Forward and Inverse PDE Problem with Small Labeled Samples
Introduction". The use of this code is restricted to academic review and study in the context of this paper.

> Please note that all the code will be displayed after the paper is formally accepted. Currently, the paper is under review, and we will only showcase experiments related to the Schrödinger equation  in the forward problem and experiments related to the Burgers' equation in the inverse problem.

### Requirement
    
![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)
![PyDOE Version](https://img.shields.io/badge/PyDOE-0.3.8-blue.svg)
![PyTorch Version](https://img.shields.io/badge/pytorch-1.10.0-brightgreen.svg)
![PyTorch Version](https://img.shields.io/badge/pytorch-1.9.0-brightgreen.svg)


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
    - [Schrodinger](/GA-PINNs(Forward_Problem)/Schrodinger)

## GA-PINN in Solving Inverse problems
### Code
- GA-PINN [Inverse problems]
    - [Allen-Cahn](/GA-PINNs(Inverse_Problem)/Allen-Cahn)
    - [Burgers](/GA-PINNs(Inverse_Problem)/Burgers)
    - [Diffusion Equation](/GA-PINNs(Inverse_Problem)/Diffusion)
    - [Lorenz System](/GA-PINNs(Inverse_Problem)/Lorenz_System)


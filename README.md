# GA-PINN
![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)
![PyTorch Version](https://img.shields.io/badge/pytorch-1.10.0-brightgreen.svg)



The paper is "GA-PINNs: Generative Adversarial Physics-informed Neural Networks for Solving Forward and Inverse PDE Problem with Small Labeled Samples
Introduction"

Physics-informed neural networks (PINNs) provide a deep learning framework for numerically solving partial differential equations (PDEs), but there still remain some challenges in the application of PINNs, for example, how to exhaustively utilize a small size of (usually very few) labeled samples, which are the exact solutions to the PDEs or their high-accuracy approximations, to improve the accuracy and the training efficiency. In this paper, we propose the generative adversarial physics-informed neural networks (GA-PINNs), which integrate the generative adversarial (GA) mechanism with original PINNs, to improve the performance of PINNs by exploiting a small size of labeled samples. The numerical experiments show that, compared with the original PINNs equipped with an additive loss computed on these labeled samples, GA-PINNs can more effectively utilize the small labeled samples when solving forward and inverse problems. As a generalization of GA-PINNs, we also combine the GA mechanism with the deep Ritz method (DRM) and the deep Galerkin method (DGM) to form GA-DRM and GA-DGM, respectively. The experimental results validate their superiority as well.

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
    - [Burgers](src/function.py)
    - [Heat](src/function.py)
    - [Helmholtz](src/function.py)
    - [HD-Poisson](src/function.py)
    - [KdV](src/function.py)
    - [Poisson](src/function.py)
    - [Schrodinger](src/function.py)

## GA-PINN in Solving Inverse problems
### Code
- GA-PINN [Inverse problems]
    - [Allen-Cahn](src/function.py)
    - [Burgers](src/function.py)
    - [Diffusion Equation](src/function.py)
    - [Lorenz System](src/function.py)
## GA-DGM
### Code
- GA-DGM
    - [Poisson](src/function.py)
    - [HD-Poisson](src/function.py)
## GA-DRM
### Code
- GA-DRM
    - [Poisson](src/function.py)
    - [HD-Poisson](src/function.py)


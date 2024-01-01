# GA-PINN
The paper is "GA-PINNs: Generative Adversarial Physics-informed Neural Networks for Solving Forward and Inverse PDE Problem with Small Labeled Samples
Introduction"

Physics-informed neural networks (PINNs) provide a deep learning framework for numerically solving partial differential equations (PDEs), but there
still remain some challenges in the application of PINNs, for example, how to
exhaustively utilize a small size of (usually very few) labeled samples, which
are the exact solutions to the PDEs or their high-accuracy approximations, to
improve the accuracy and the training efficiency. In this paper, we propose the
generative adversarial physics-informed neural networks (GA-PINNs), which
integrate the generative adversarial (GA) mechanism with original PINNs,
to improve the performance of PINNs by exploiting a small size of labeled
samples. The numerical experiments show that, compared with the original
PINNs equipped with an additive loss computed on these labeled samples,
GA-PINNs can more effectively utilize the small labeled samples when solving
forward and inverse problems. As a generalization of GA-PINNs, we also
combine the GA mechanism with the deep Ritz method (DRM) and the deep
Galerkin method (DGM) to form GA-DRM and GA-DGM, respectively. The
experimental results validate their superiority as well.

## Folder tree



## Installation


## GA-PINN (Forward Problems)


## GA-PINN (Inverse Problems)

## GA-DGM

## GA-DRM

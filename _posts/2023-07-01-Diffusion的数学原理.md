---
layout: mypost
title: Diffusion的数学原理
categories: [文章]
published: true
date: 2023-07-01
tags: [文章]
---

# Variational Autoencoders

## Concepts
- Distirbution: $p$ for real distribution, and $q$ usually represents an approximation of the real distribution.
- Observable: a variable $X$ whose quantity can be observed and measured.
- Latent (variable): a variable $Z$ related to some observables, but cannot be directly measured.
- Entropy:
    - Gibbs entropy formula: $S = - k_B \sum_{i} (p_i \ln{p_i})$ in which $k_B$ is the Boltzmann's constant representing the proportionality related to the average relative thermal energy. 
    - Shannon's entropy (information entropy): $H(X) = - \sum_{x \in X}{\left(p(x) \log{p(x)} \right)}$, $H \in [0,\infty)$. In this context, $H$ represents *Heat*.
- Cross entropy: $H(p,q) = - \sum_{x \in X}{p(x)\log{q(x)}}$, $H$ achieves minimum when distribution $p=q$, thus $\min{H} = H(p)$ which is the *Heat* or entropy of $p$.
    - $H(p,q) = - \sum_{x \in X}{p(x)\left( \log{p(x)} + (\log{q(x)} - \log{p(x)}) \right)}$
    - $H(p,q) = - \sum_{x \in X}{p(x)\log{p(x)}} - \sum_{x \in X}{p(x)(\log{q(x)} - \log{p(x)})}$
- Kullback–Leibler (KL) divergence (relative entropy), is the latter part of cross-entropy:
    - $KL(p,q) = - \sum_{x \in X}{p(x)(\log{q(x)} - \log{p(x)})}$
    - $KL(p,q) = \sum_{x \in X}{p(x)(\log{p(x)} - \log{q(x)})}$
    - $KL(p,q) = \sum_{x \in X}{p(x)\log{\frac{p(x)}{q(x)}} }$
    - $KL \in [0,+\infty)$
- Prior: $p(x)$ a total probability of a variable. The measured variable is ususally a latent factor influencing our desired observables. Also, prior is a kind of marginal probability on a specific margin.
- Posterior: $p(Z=z|x)$ conditional probability given a specific prerequisite. e.g. $p(Class=cat|image)$.
- Likelihood function: $\mathcal{L}(\theta,x) = p(\theta|x)$ aims to measure the possibility of model parameters to fit the observed data $x$
- Baye's theorem:$P(A|B)=\frac{P(B|A)P(A)}{P(B)}$
    - $P(A,B)=P(A,B)$
    - $P(A|B)P(B)=P(B|A)P(A)$
    - $P(A|B)=\frac{P(B|A)P(A)}{P(B)}$
- Jensen's inequality: $f(\mathbb{E}(X)) \geq \mathbb{E}f(X)$
- Varational lower-bound:$\mathbb{E}[\log p(X,Z)] + H(Z)$
    
    in which, $x$ can be the image data, $z$ can be the latent feature extracted from $x$, or can be the classification distribution (prob-vector) of $x$. 
    $$
    \begin{align}
    \log{p(X)} &= \log{ \int_Z{p(X,Z)} } \\\\
              &= \log{ \int_Z{p(X,Z)\frac{q(Z)}{q(Z)}} } \\\\
              &= \log{\mathbb{E}_q \left[ \frac{p(X,Z)}{q(Z)} \right] } \\\\
              &\geq \mathbb{E}_q \left[ \log{\frac{p(X,Z)}{q(Z)}}  \right] \\\\
              &= L = \mathbb{E}_q[\log p(X,Z)] + H(Z)
    \end{align}
    $$
    maximization of $\log{p(X)}$ can now become ELBO target $L$.

    another aspect is to define $p(X)$ as a image generation process. Further introducing latent class variable $C$ creates classification model $p(C|X)$. Also, introducing latent feature variable $Z$ creates feature encoding distribution $p(Z|X)$. Here we will use feature variable $Z$ as an example.

    To create a trained approximator $q(Z)$ to fit the underlying real $p(Z|X)$, KL divergence metric can be used:

    $$
    \begin{align}
    KL(q,p)
    \end{align}
    $$



# Reference
1. [Mathjax CDN](https://cdnjs.com/libraries/mathjax/2.7.9)
1. [Mathjax 3.2 Docs](https://www.osgeo.cn/mathjax/index.html)


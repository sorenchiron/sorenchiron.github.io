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
- Observable: is a random variable in contrast to latent variable.
- Latent (variable): a variable $Z$ related to some observables, but cannot be directly measured.
- Random variable: a random variable $X$ is a set, and is a function: [Outcome](https://en.wikipedia.org/wiki/Outcome_(probability))->Mesurement, aka. $X:\Omega \rightarrow E$. Measurement values $x\in E$ is a numerical representation of a outcome or outcomes aka. sample-space. A single sample $x$ can be drawn from the **range** of random variable $x\in X$ or $x \in E$.
- Distirbution: $p$ is a function standing for the real distribution, and $q$ can represent an approximation function of the real distribution. $p(X=x)$ or $p(X)$ is a scalar while $p(X),X=\\{x_1,x_2,...,x_n\\}$ is a set describing the probablistic distribution of the entire sample space.
- Entropy:
    - Gibbs entropy formula: $S = - k_B \sum_{i} (p_i \ln{p_i})$ in which $k_B$ is the Boltzmann's constant representing the proportionality related to the average relative thermal energy. 
    - Shannon's entropy (information entropy): $H(X) = - \sum_{x \in X}{\left(p(x) \log{p(x)} \right)}$, $H \in [0,\infty)$. In this context, $H$ represents *Heat*.
- Cross entropy: $H(p,q) = - \sum_{x \in X}{p(x)\log{q(x)}}$, $H$ achieves minimum when distribution $p=q$, thus $\min{H(p,q)} = H(p)$ which is the *Heat* or entropy of $p$.
    $$
    \begin{align}
    H(p,q) &= - \sum_{x \in X}{p(x)\left( \log{p(x)} + (\log{q(x)} - \log{p(x)}) \right)} \\\\
    &= - \sum_{x \in X}{p(x)\log{p(x)}} - \sum_{x \in X}{p(x)(\log{q(x)} - \log{p(x)})} \\\\
    &= H(p) + D_{KL}(p,q)
    \end{align}
    $$
- Kullback–Leibler (KL) divergence (relative entropy), is the latter part of cross-entropy:
    $$
    \begin{align}
    KL(p,q) &= - \sum_{x \in X}{p(x)(\log{q(x)} - \log{p(x)})} \\\\
    KL(p,q) &= \sum_{x \in X}{p(x)(\log{p(x)} - \log{q(x)})} \\\\
    KL(p,q) &= \sum_{x \in X}{p(x)\log{\frac{p(x)}{q(x)}} } \\\\
    KL &\in [0,+\infty)
    \end{align}
    $$
- Prior: $p(x)$ a total probability of a variable. The measured variable is ususally a latent factor influencing our desired observables. Also, prior is a kind of marginal probability on a specific margin.
- Posterior: $p(Z=z\|x)$ conditional probability given a specific prerequisite. e.g. $p(Class=cat\|image)$.
- Likelihood function: $\mathcal{L}(\theta,x) = p(\theta\|x)$ aims to measure the possibility of model parameters to fit the observed data $x$
- Baye's theorem:$P(A\|B)=\frac{P(B\|A)P(A)}{P(B)}$
    $$\begin{align}
    P(A,B) &= P(A,B) \\\\
    P(A\|B)P(B) &= P(B\|A)P(A) \\\\
    P(A\|B) &= \frac{P(B\|A)P(A)}{P(B)}
    \end{align}$$
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

    another aspect is to define $p(X)$ as a image generation process. Further introducing latent class variable $C$ creates classification model $p(C\|X)$. Also, introducing latent feature variable $Z$ creates feature encoding distribution $p(Z\|X)$. Here we will use feature variable $Z$ as an example.

- Dirac Delta function
    $$
    \begin{align}
    \delta(x) &= 0, \text{if } x\neq 0\\\\
            \int^{+\infty}_{-\infty} \delta(x)  &= 1 
    \end{align}
    $$

- Functional(泛函) An important sub-concept to VAE.

    $\mathcal{F}:(\mathbb{R}\rightarrow \mathbb{R}) \rightarrow \mathbb{R}$

- Fermat's theorem 费马引理 An important sub-concept to VAE.

    函数在点 $\xi$ 邻域有定义，$\xi$ 处可导，且 $f(\xi)$ 是邻域极值，则$f'(\xi)=0$

- Lagrangian 拉格朗日函数 An important sub-concept to VAE.

    `Lagrangian` is a function describing energy : $\mathcal{L} = T - V$ in which T is kinetic energy and V is potential energy.

    `Lagrangian` is generalized to better describe complex physical system. Given position $q$, velocity $q'$ and time $t$, the status of the system can be represented using Lagrangian function $\mathcal{L}(q,q',t)$

    Lagrange and Euler together developed Euler-Lagrange equation to solve motion determination problems. 

- Variational principle: The principle that enables a problem to be solved using calculus of variations, which concerns finding functions that optimize the values of quantities that depend on those functions. 最速降曲线问题，找到最佳曲线（最优函数），以使得速降时间最短（物理量极值）
    - `Variational` means the domain of the functional is no longer in a fixed scalar or vector form. Instead, the domain is the whole set of functions or at least a subset of functions. Such a large domain relative to that of those traditional scalar mapping functions is deemed as a `Highly variational search space` because functions can take large variations than real numbers. From this point, functional is a dynamically undetermined form, and thus is a form of variation nautrally.
    - calculus of variations : method to optimize for a best function. Commonly used method is Euler-Lagrange equation.

- Variational Auto-Encoder:

    It is a variational problem to find optimal functions `Encoder()` and `Decoder()` from a set of possible functions. Even though in deep learning scenario the NN structure of encoder and decoder is fixed and it is the scalar parameters which are optimized for, researchers tends to use generalized scope to describe their research which have brought two benifits:

    1. variational methods can be tried to help solving for encoders and decoders.
    1. an upstream math concept can make their research more theoretical and classy. 

## From ELBO to Autoencoders
#### Generative tasks from probabilistic view
Given an image generation process function $g(\cdot)$, the generation process is:
$$\begin{align}
x = g(z)
\end{align}$$
high dimensional image $x$ is generated by latent variable $z$ in a low dimensional manifold space e.g. classification space or deep feature space.

To approximate the underlying real generation process $g(\cdot)$, $f_\theta(\cdot)$ is created parameterized by $\theta \in \mathbb{Q}^M$, meaning $\theta$ can be a set of $M$ parameters. $f$ is trained on a set of observations $X' \subseteq X$, which is a subset of the numerical representation $X$ of the entire sample space $\Omega$.

The approximation process is:
$$\begin{align}
x = g(z)
\end{align}$$

The objective is:
$$\begin{align}
\theta^* = \arg \max_{\theta} \mathbb{P_\theta}(X')
\end{align}$$

meaning to maximize the possibility that $g$ parameterized by $\theta$ generates training set examples $X'$. The sampled training set $X'$ is a representative subset of the underlying full-set $X$.

In this context, $X'$ can be simply replaced by $X$ because sampling technique for $X'$ is not the key concern. Subset $X'$ is treated as the full set $X$.

#### Difficulties in optimizing objective

It is easy to compute $\mathbb{P}(X)$ empirically just for the training sample set. But it is difficult to measure $P(X) = P(g(Z)) = P(X\|Z)P(Z)$ which means the possibility that $g$ generates each sample $x \in X$.

The difficulty lies in:

1. The existence and actual distribution of latent variable $Z$ is purely hypothetic. The real distribution of $Z$ is unknown and can only be assumed inaccuratly.
1. Any assumed $Z$ may have different distribution from $p(Z)$. The assumed distribution can only be $q:q(Z) \sim p(Z)$
1. $p(X\|Z)q(Z)$ is difficult to compute precisely or in closed-form, when the generation process $g$ is complex and highly non-linear.

#### Change the form of objective using Jensen's inequality

If we maximize for log likelihood, we get:

$$\begin{align}
\arg\max p(X) &= \arg\max \log{p(X)} \\\\
\log{p(x)} &= \log \int{p(x,z)dz} \\\\
           &= \log \int{\frac{p(x,z)q_{\Phi}(z\|x)}{q_{\Phi(z\|x)}}dz} \\\\
           &= \log E_{q_\Phi(z\|x)} \left[ \frac{p(x,z)}{q_\Phi(z\|x)} \right] \\\\
           &\geq E_{q_\Phi(z\|x)} \left[ \log \frac{p(x,z)}{q_{\Phi(z\|x)}} \right] \label{eq:elbo}
\end{align}$$
This latter form is ELBO.

Here the parameter of encoding process $q(z\|x)$ is denoted as $\Phi$ in reference paper[^5].
 
#### Closed-form of Evidence Lowerbound

To deduce in a closed form[^5]:

$$
\begin{align}
\log{p(x)} &= \log{p(x)} \int{q_\Phi(z\|x)dz} \\\\
&= \int{q_\Phi(z\|x)\log{p(x)}dz} \\\\
&= E_{q_\Phi(z\|x)}\log p(x) \\\\
&= E_{q_\Phi(z\|x)}\left[ \log \frac{p(x,z)}{p(z\|x)} \right]\\\\
&= E_{q_\Phi(z\|x)}\left[ \log \frac{p(x,z)q_\Phi(z\|x)}{p(z\|x)q_\Phi(z\|x)} \right]\\\\
&= E_{q_\Phi(z\|x)}\left[ \log \frac{p(x,z)}{q_\Phi(z\|x)} \right] + E_{q_\Phi(z\|x)}\left[ \log \frac{q_\Phi(z\|x)}{p(z\|x)} \right]\\\\
&= E_{q_\Phi(z\|x)}\left[ \log \frac{p(x,z)}{q_\Phi(z\|x)} \right] + D_{KL}(q_\Phi(z\|x) \|\| p(z\|x)) \\\\
&= ELBO + D_{KL}
\end{align}
$$

When optimizing for an encoder $q_\Phi(z\|x)$, the evidence term $p(x)$ from the very begining is a constant to a given $x$. Hence by maximizing ELBO, the latter KL-divergence is minimized respectively.

When optimizing for a decoder $q_\Theta(x\|z)$, one can get:
$$
\begin{equation}
\log{p(x)} \neq \log{p(x)} \int{q_\Theta(x\|z)dz}
\end{equation}
$$
This means ELBO cannot be deduced using a decoder $q$.

#### Why ELBO can be optimized while $D_{KL}$ cannot?
$D_{KL}(q_\Phi(z\|x) \|\| p(z\|x))$ term involves comparison with the true $p(z\|x)$ which is unknown.

For the ELBO term, 
$$
\begin{align}
E_{q_\Phi(z\|x)}\left[ \log \frac{p(x,z)}{q_\Phi(z\|x)} \right] &= E_{q_\Phi(z\|x)}\left[ \log \frac{p(x\|z)p(z)}{q_\Phi(z\|x)} \right] \\\\
&= E_{q_\Phi(z\|x)}\left[ \log p(x\|z) \right] + E_{q_\Phi(z\|x)}\left[ \log \frac{p(z)}{q_\Phi(z\|x)} \right] \\\\
&= E_{q_\Phi(z\|x)}\left[ \log p(x\|z) \right] - E_{q_\Phi(z\|x)}\left[ \log \frac{q_\Phi(z\|x)}{p(z)} \right] \\\\
&= - CE(q_\Phi(z\|x) \|\| p(x\|z)) - D_{KL}(q_\Phi(z\|x) \|\| p(z))
\end{align}
$$
To maximize ELBO, CE and $D_{KL}$ are to be minimized.

The first term $CE$ is reconstruction term, meaning the maximization of reconstruction likelihood $p(z)=\int p(z\|x)p(x\|z)dz$. The last term is prior matching term, encouraging the latent feature space to be smooth rather than being a Dirac delta pluse function 

As for why $p(x,z)$ is transformed specifically to $p(x\|z)p(z)$ instead of $p(z\|x)p(x)$. This is because such transform will bring the equation back to $\log p(x) = ELBO + D_{KL}$ gaining no new knowledge, as described in appendix.

<img width="50%" src="https://bkimg.cdn.bcebos.com/pic/5fdf8db1cb134954301abf06534e9258d1094a4f?x-bce-process=image/format,f_auto/watermark,image_d2F0ZXIvYmFpa2UyNzI,g_7,xp_5,yp_5,P_20/resize,m_lfit,limit_1,h_1080"/> A simple demo of dirac function


#### How to train a Varational AutoEncoder
Training using Monte Carlo estimate, subset $X',Z'$ are sampled from the underlying full data spaces $X,Z$. The training process is:
$$\begin{equation}
\arg_{\Phi,\Theta}\max -CE-D_{KL} \approx \arg_{\Phi,\Theta}\max \sum^L_{l=1} \log p_\theta(x\|z^{(l)}) - D_{KL}(q_\Phi(z\|x) \|\| p(z))
\end{equation}$$

prior of latent $z$ can be $\mathcal{N}(0,1)$.

posterior $p(z\|x)$ can be $\mathcal{N}\sim (\mu_\Phi(x),\sigma^2_\Phi(x)\mathrm{I})$, in which the untrackable distribution of $z$ is reparameterized by $\mu_\Phi,\sigma_\Phi$ and $x$. Now $z$ can be sampled as :

$$\begin{equation}
z = \mu_\Phi(x) + \sigma_\Phi(x)\odot \epsilon, \epsilon \in \mathrm{N}(0,1)
\end{equation}$$
where $\odot$ is element-wise product. Now input $x$ can determine distribution parameters of latent $z$, and thus $z$ can be indirectly optimized for each $x$.

Generation process:

$$\begin{align}
z_{gen} &\sim p(z), \\\\
x_{gen} &\sim p_{\Theta}(z_{gen})
\end{align}
$$

#### Hierarchical Variational Autoencoders

Given a hierarchical generation involving $T$ times processing and therefore $T$ latents:

$$\begin{equation}
x \leftrightarrow z_1 \leftrightarrow z_2 \leftrightarrow ... \leftrightarrow z_T
\end{equation}$$

For the general HVAE, the encoding process can depend on all previous samples. 

$$\begin{equation}
z_t \sim \mathcal{N}(\mu_{\Phi}(z_{t-1},z_{t-2},...,x),\sigma_{\Phi}(z_{t-1},z_{t-2},...,x))
\end{equation}$$

Vice versa, deocoding process can depend on all previous latents.

#### Markovian HVAE
Under Markovian assumption, current status only depend on the very previous status. Hence encoding process only depend on previous sample $z_{t-1}$. And decoding only depend on previous latent $z_{t+1}$.

The ELBO is:

$$\begin{align}
E_{q_\Phi(z\|x)}\left[ \log \frac{p(x,z)}{q_\Phi(z\|x)} \right] &= E_{q_\Phi(z_{1..T}\|x)}\left[ \log \frac{p(x,z_{1..T})}{q_\Phi(z_{1..T}\|x)} \right] =  E_{q_\Phi(z_{1..T}\|x)}\left[ \log \frac{p(x \| z_{1}) p(z_{1..T})}{q_\Phi(z_{1..T}\|x)} \right] \\\\
&= E_{q_\Phi(z_{1..T}\|x)}\left[ \log \frac{p(z_T)  p(x\|z_1) \prod_{i=2}^T p(z_{i-1}\|z_{i})}{q_\Phi(z_1\|x) \prod_{i=2}^T q_\Phi(z_{i}\|z_{i-1})} \right]
\end{align}$$

## Variational Diffusion Models

VDM is a MHVAE with restrictions:

1. size of latents are the same as sample $x$.
1. encoder is Gaussian noising scaled around previous sample ($\mu,\sigma$ linearly scaled). $x_{i} = \gamma_i x_{i-1} + \mathcal{N}(0,\sigma_i)$
1. the final latent $z_T$ is a standard Gaussian $\mathcal{N}(0,1)$ 

#### ELBO objective function

$$\begin{align}
ELBO=&E_{q(x_{1:T}\|x_0)}\left[ \log \frac{p(x_{0:T})}{q(x_{1:T}\|x_0)} \right] \\\\
=&E_{q(x_1\|x_0)}[\log p_\theta(x_0\|x_1)] - E_{q(x_{T-1}\|x_0)}[D_{KL}(q(x_T\|x_{T-1}) \\| p(x_T) )] \\\\
&-\sum_{t=1}^{T-1} E_{q(x_{t-1},x_{t+1}\|x_0)}[D_{KL}(q(x_t\|x_{t-1}) \\| p_\theta(x_t\|x_{t+1}))] \label{eq:term3}
\end{align}$$

1. $E_{q(x_1\|x_0)}[\log p_\theta(x_0\|x_1)]$ reconstruction term, also a consistentcy term asking the first noising step to be reversable.
1. $-E_{q(x_{T-1}\|x_0)}[D_{KL}(q(x_T\|x_{T-1}) \\| p(x_T) )]$ prior matching term, it asks the last noising step to be random enough such that the generated $x_T$ is $\mathcal{N}(0,1)$ which is $p(x_T)$.
1. $-\sum_{t=1}^{T-1} E_{q(x_{t-1},x_{t+1}\|x_0)}[D_{KL}(q(x_t\|x_{t-1}) \\| p_\theta(x_t\|x_{t+1}))]$ consistency term, asking the forward and backward generation of any $x_t$ be consistent.

In term 3, expectation is computed over two variables $x_{t-1},x_{t+1}$. It is suggested in [^7] that using one variable at a time is better in reducing ELBO variance and thus is easier to optimize. But euqation-53 has a mistake. And we do not agree with his deduction.



#### Analyze the objective of VDM

In VDM, noising process is defined as a Gaussian linear model[^8], which is a linear combination of multiple gaussian noises and original input image as a residual $\epsilon$. In VDM described by [^7], noising process is specifically defined as:
$$\begin{align}
q(x_t\| x_{t-1}) &= \mathcal{N}(x_t; \sqrt{\alpha_t}x_{t-1},(1-\alpha_t)\mathrm{I}) \label{eq:markov_xt_dist} \\\\
x_t &= \sqrt{\alpha_t} x_{t-1} + \sqrt{1-\alpha_t} \epsilon \label{eq:markov_xt_linear}
\end{align}$$

$x_t$ can be expanded and source back to $x_0$. By merging variances of independent noises $\epsilon^\ast$ into a single $\epsilon_t$, we can get:

$$
\begin{align}
x_t &= \sqrt{\alpha_t} x_{t-1} + \sqrt{1-\alpha_t} \epsilon_{t-1}^{\ast} \\\\
&= \sqrt{\alpha_t} \left( \sqrt{a_{t-1}} x_{t-2}  + \sqrt{1-\alpha_{t-1}} \epsilon_{t-2}^{\ast} \right) + \sqrt{1 - \alpha_t}  \epsilon_{t-1}^{\ast} \\\\
&= \sqrt{\alpha_t \alpha_{t-1}} x_{t-2} + \sqrt{1- \alpha_t \alpha_{t-1}} \epsilon_{2}\\\\
&= ... \\\\
&= \sqrt{\prod_{i=1}^{t}\alpha_i }x_0 + \sqrt{1- \prod_{i=1}^{t}\alpha_i }\epsilon_t \\\\
&=\sqrt{\bar{\alpha}_t} x_0 + \sqrt{1-\bar{\alpha}_t} \epsilon_t \label{eq:noise_process}\\\\
&\sim \mathcal{N}(x_t; \sqrt{\bar{\alpha}_t} x_0,(1-\bar{\alpha}_t)\mathrm{I} ) \label{eq:xt_on_x0_dist}
\end{align} 
$$

in which $\epsilon_t$ is the summation of $t$ independent gaussians $\epsilon^\ast$. This form directly link $x_t$ to $x_0$ and thus is useful to analyze consistency term in ELBO objective.

According to paper[^7] Eq. 58, encode-decode consistency term(Eq. \ref{eq:term3} term-3) can become:
$$
\begin{equation}
-E_{q(x_t\|x_0)} [D_{KL}(q(x_{t-1}\|x_t,x_0) \\| p_\theta(x_{t-1}\|x_t))]
\end{equation}
$$

This form is derived in paper[^7] using a proabably problematic cancellation(Eq. 53). However this result is reasonable, since the true distribution of encoding and decoding are the same $p(x_t\|x_{t-1}) \sim p(x_t\|x_{t+1})$. Approximator $p_\theta(x_t\|x_{t+1})$ can fit
 either one of them.

To analyze the decoding posterior $q(x_{t-1}\|x_t)$ , a dummy $x_0$ condition can be added: $q(x_{t-1}\|x_t,x_0)$. Although VDM is Markov HVAE, adding the original image $x_0$ can gain insight of the connection with $x_0$ . 

$$\begin{align}
q(x_{t-1}\|x_t,x_0) &= \frac{q(x_t\|x_{t-1},x_0)q(x_{t-1}\|x_0)}{q(x_t\|x_0)} \\\\
&\propto \mathcal{N}(x_{t-1};\frac{\sqrt{\alpha_t}(1-\bar{\alpha}\_{t-1})x_t + \sqrt{\bar{\alpha}\_{t-1}}(1-\alpha_t)x_0 }{1-\bar{\alpha}\_t},\frac{(1-\alpha_t)(1-\bar{\alpha}\_{t-1})}{1-\bar{\alpha}\_t}\mathrm{I}) \label{eq:posterior_param}
\end{align}
$$

To maximize ELBO, $D_{KL}(q\\|p_{\theta})$ is to be minimzed.

$$\begin{align}
&\arg_{\theta} \min D_{KL}(q(x_{t-1}\|x_{t},x_0) \\| p_{\theta}(x_{t-1}\|x_t) ) \\\\
=& \arg_{\theta} \min \frac{1}{2\sigma^2(t)} \\| \mu_\theta - \mu_q \\|^2_2
\end{align}
$$

According to Eq. \ref{eq:posterior_param}, the most likely $x_{t-1}$ is a linear combination of noisy $x_t$ and image $x_0$. By creating a network $\hat{x}\_\theta(x_t,t) \sim x_0$ to estimate $x_0$, one can interpolate and obtain $x_{t-1}$

$$\begin{align}
&\arg_{\theta} \min D_{KL}(q(x_{t-1}\|x_{t},x_0) \\| p_{\theta}(x_{t-1}\|x_t) ) \\\\
=& \arg_{\theta} \min \frac{1}{2\sigma_{q}^2(t)} \frac{\bar{\alpha}\_{t-1}(1-\alpha_t)^2}{(1-\bar{\alpha}\_t)^2} \\| \hat{x}\_\theta(x_t,t) - x_0 \\|^2_2 \label{eq:objective_l2}
\end{align}
$$

The problem is now to train a $\hat{x}$ to approxmate $x_0$. Optimizing a VDM boils down to learning a neural network to predict the original ground truth image from an arbitrarily noisified version of it.



#### Learning diffusion noise parameters

From Eq. \ref{eq:posterior_param} the variance $\sigma_q^2$ for decoding process $p(x_{t-1}\|x_t,x_0)$ is $\frac{(1-\alpha_t)(1-\bar{\alpha}\_{t-1})}{1-\bar{\alpha}}\_t$. Using this variance to replace $\sigma_q^2$ in MSE objective defined by Eq. \ref{eq:objective_l2}, the objective is updated as:

$$\begin{align}
&\arg_{\theta} \min D_{KL}(q(x_{t-1}\|x_{t},x_0) \\| p_{\theta}(x_{t-1}\|x_t) ) \\\\
=& \arg_{\theta} \min \frac{1}{2\sigma_{q}^2(t)} \frac{\bar{\alpha}\_{t-1}(1-\alpha_t)^2}{(1-\bar{\alpha}\_t)^2} \\| \hat{x}\_\theta(x_t,t) - x_0 \\|^2_2 \label{eq:objective_l2_raw}\\\\
=& \arg_{\theta} \min \frac{1}{2 \frac{(1-\alpha_t)(1-\bar{\alpha}\_{t-1})}{1-\bar{\alpha}\_t}} \frac{\bar{\alpha}\_{t-1}(1-\alpha_t)^2}{(1-\bar{\alpha}\_t)^2} \\| \hat{x}\_\theta(x_t,t) - x_0 \\|^2_2 \label{eq:objective_l2_var}
\end{align}
$$

It is possible to use `SNR` concept to replace those $\alpha$, since $SNR(\mathcal{N})=\frac{\mu^2}{\sigma^2}$ 

Recall the incremental noising process (Eq. \ref{eq:markov_xt_dist},\ref{eq:markov_xt_linear}) and chained noising formular (Eq. \ref{eq:xt_on_x0_dist}):
$$
\begin{align}
x_t &= \sqrt{\alpha_t} x_{t-1} + \sqrt{1-\alpha_t} \epsilon \\\\
q(x_t\|x_{t-1}) &= \mathcal{N}(x_t;\sqrt{\alpha_t} x_{t-1};(1-\alpha_t)\mathrm{I})\\\\
q(x_t\|x_0) &= \mathcal{N}(x_t;\sqrt{\bar{\alpha}\_{t}}x_0,(1-\bar{\alpha}\_t)\mathrm{I})
\end{align}
$$

Knowing that , SNR of $x_t$ is:

$$
\begin{equation}
SNR(t)=\frac{\bar{\alpha}\_t}{1-\bar{\alpha}\_t}
\end{equation}
$$

The variance-based MSE objective in Eq. \ref{eq:objective_l2_var} become:
$$\begin{align}
&\arg_{\theta} \min D_{KL}(q(x_{t-1}\|x_{t},x_0) \\| p_{\theta}(x_{t-1}\|x_t) ) \\\\
=& \arg_{\theta} \min  \frac{1}{2}\left(  \frac{\bar{\alpha}\_{t-1}}{1-\bar{\alpha}\_{t-1}} - \frac{\bar{\alpha}\_t}{1-\bar{\alpha}\_t} \right) \\| \hat{x}\_\theta(x_t,t) - x_0 \\|^2_2 \\\\
=& \frac{1}{2}(SNR(t-1) - SNR(t))  \\| \hat{x}\_\theta(x_t,t) - x_0 \\|^2_2 \label{eq:objective_l2_snr}
\end{align}$$

SNR concept introduced here helps us obtain $\alpha$ so as to generate $x_t$ directly from $\sqrt{\bar{\alpha}\_{t}} x_0 + \epsilon_t$ and optmize RMSE loss $...\\|\hat{x}\_\theta(x_t,t) -x_0 \\|^2\_2$. One can choose a series of SNRs and obtain corresponding $\bar{\alpha}\_t$. A convenient way to define a descending SNR sequence is using a monotonically increasing neural network $\omega_\eta$:

$$\begin{equation}
SNR(t) = \exp(-\omega_\eta(t))
\end{equation}$$

$\exp$ is useful to get a $\bar{\alpha}$ as sigmoid activated logits of network $\omega_\eta$
$$\begin{align}
SNR &=\frac{\bar{\alpha}\_t}{1-\bar{\alpha}\_t} = \exp(-\omega_\eta(t)) \\\\
\therefore \bar{\alpha}\_t & = \mathrm{sigmoid}(-\omega_\eta(t)) \\\\
\therefore 1-\bar{\alpha}\_t & = \mathrm{sigmoid}(\omega_\eta(t))
\end{align}$$

#### Learning noise instead of $x_0$

According to Eq. \ref{eq:noise_process}, $x_0$ can be estimated using a predicted noise $\hat{\epsilon}\_{t}$ written as:

$$\begin{equation}
x_0 = \frac{x_t - \sqrt{1-\bar{\alpha}\_t} \hat{\epsilon}\_{t}}{\sqrt{\bar{\alpha}\_t}}
\end{equation}$$ 

The RMSE loss in Eq. \ref{eq:objective_l2_raw} can be:

$$\begin{align}
&\arg_{\theta} \min D_{KL}(q(x_{t-1}\|x_{t},x_0) \\| p_{\theta}(x_{t-1}\|x_t) ) \\\\
=& \arg_{\theta} \min \frac{1}{2\sigma_{q}^2(t)} \frac{\bar{\alpha}\_{t-1}(1-\alpha_t)^2}{(1-\bar{\alpha}\_t)^2} \\| \frac{x_t - \sqrt{1-\bar{\alpha}\_t} \hat{\epsilon}\_{t}}{\sqrt{\bar{\alpha}\_t}} - x_0 \\|^2_2 \\\\
=& \arg_{\theta} \min \frac{1}{2\sigma_{q}^2(t)} \frac{\bar{\alpha}\_{t-1}(1-\alpha_t)^2}{(1-\bar{\alpha}\_t)^2} \\| \sqrt{\frac{1-\bar{\alpha}\_t}{\bar{\alpha}\_t}}(\epsilon_t - \hat{\epsilon}\_{t} ) \\|^2_2 \\\\
=& \arg_{\theta} \min \frac{1}{2\sigma_{q}^2(t)} \frac{\bar{\alpha}\_{t-1}(1-\alpha_t)^2}{(1-\bar{\alpha}\_t)^2} \frac{1-\bar{\alpha}\_t}{\bar{\alpha}\_t} \\| \epsilon_t - \hat{\epsilon}\_{t}(x_t,t) \\|^2_2 \\\\
=& \arg_{\theta} \min \frac{1}{2\sigma_{q}^2(t)} \frac{(1-\alpha_t)^2}{(1-\bar{\alpha}\_t)\alpha_t} \\| \epsilon_t - \hat{\epsilon}\_{t}(x_t,t) \\|^2_2 \label{eq:objective_l2_noise}\\\\
\end{align}
$$

It is found that predicting noise performs better.


#### Learning gradient of $x_t$ towards $x_0$

There is a way to predict original image $x_0$ directly from noised $x_t \sim \mathcal{N}(x_t;\sqrt{\bar{\alpha}\_t}x_0,(1-\bar{\alpha}\_t)\mathrm{I})$
According to Tweedie’s Formula, a maximum likelihood estimate of mean=$\sqrt{\bar{\alpha}\_t}x_0$ is to travel from $x_t$ a distance $\Sigma_x$ at gradient direction $\nabla \log p(x_t) = \frac{\partial \log p(x_t)}{\partial x_t}$.

It can be deduced that this gradient to be learnt equals the variance-normalized noise $\nabla \log p(x_t) = - \frac{1}{\sqrt{1-\bar{\alpha}\_t}}\epsilon_t$ in the denoising direction.

#### Score-based Generative Models

Score-based Generative Models means to create a function $f(\cdot)$ to predict the score of a current solution $x$. By obtaining the derivatives $\nabla f(\cdot)$ of the score function, $x$ can therefore be updated towards optimum.

The gradient can be computed using Stochastic differential equation (SDE) solvers numerically.

In our scenario, it is possible to directly learn the gradient of log-likelihood function $\log p(x)$ and update current solution $x$ towards maximum log likelihood. From the perspective "Learning gradient of $x_t$ towards $x_0$", VDM can be treated as a Score-based Generative Model when trained to predict noise/gradient.

## Conditional VDM

in order to control the generation detail of VDM, conditions can be added to manipuate generation process.

#### Guidance based on posterior condition
condition feature can be embeded into posteriors during training.

$$\begin{equation}
p(x_{0:T}\|y) = p(x_T) \prod_{t=1}^T p_\theta(x_{t-1}\| x_t,y)
\end{equation}$$

#### Classifier Guidance
During inference, gradient of classifier(s) can be plugged into the score based VDM to modify the update direction

#### Classifier-Free Guidance

It is actually Free-controlling conditional VDM. Because one can choose to use conditions, or not. Furthermore, choosing the balance between different condition strength is also possible.

It is achieved by learning two diffusion models $p(x_t\|y),p(x_t)$ and combine them using a linear combination
$$\begin{equation}
\nabla \log \hat{p}(x_{t}\|y) = \gamma \nabla \log p(x_{t}\|y) + (1-\gamma) \nabla \log p(x_{t})
\end{equation}$$

Even if it is more flexible to learn two models and tuning them during inference, the high training cost makes training-time combination more feasible, in which all-zero-vector is fed as $y$ representing unconditioned status.


# Closing

The author(s) deemed that: 
> It is unlikely that this is how we, as humans, naturally model and generate data; we do not generate samples as random noise that we iteratively denoise.

I personally think that generating image from noise with conditions is a biologically sound procedure. Human picture imaginations based on noisy thoughts, with conditions or latent motivations also rise from chaotic noise.

Human draw pictures from structures and lines may simply because a noisy generation process is pre-generated in our mind already before we pick up pens.

# Key questions to answer

##### Q: how exactly to stochastically optimize ELBO given an encoder and decoder parameterized by $\theta$? 

A: Learn the $x_0$ predictor, or $\epsilon_t$ predictor across all steps $t$ and all samples $x\in X$.

##### Q: what is the strategy for controlling the magnitude of $\sigma^2$ and $\mu$ for each step?

A: By controlling the SNR of noised samples.

##### Q: what is a scheduler?

A: The generator of a series of SNR or $\bar{\alpha}\_t$























# Appendix
#### ELBO break back into $\log p(x) = ELBO + D_{KL}$
For ELBO term, if we use bayes chain rule on $p(x,z)$:
$$
\begin{align}
E_{q_\Phi(z\|x)}\left[ \log \frac{p(x,z)}{q_\Phi(z\|x)} \right] &= E_{q_\Phi(z\|x)}\left[ \log \frac{p(z\|x)p(x)}{q_\Phi(z\|x)} \right] \\\\
&= E_{q_\Phi(z\|x)}\left[ \log p(z\|x) \right] + E_{q_\Phi(z\|x)}\left[ \log \frac{p(x)}{q_\Phi(z\|x)} \right] \\\\
&= E_{q_\Phi(z\|x)}\left[ \log p(z\|x) \right] - E_{q_\Phi(z\|x)}\left[ \log \frac{q_\Phi(z\|x)}{p(x)} \right] \\\\
\end{align}
$$
For any give $x$, $p(x)$ is a constant. Hence there is:
$$
\begin{align}
E_{q_\Phi(z\|x)}\left[ \log \frac{p(x,z)}{q_\Phi(z\|x)} \right] &= E_{q_\Phi(z\|x)}\left[ \log p(z\|x) \right] - E_{q_\Phi(z\|x)}\left[ \log \frac{q_\Phi(z\|x)}{p(x)} \right] \\\\
&= E_{q_\Phi(z\|x)}\left[ \log p(z\|x) \right] - E_{q_\Phi(z\|x)}\left[ \log q_\Phi(z\|x) \right] +  \log p(x)\\\\
&= CE(q_\Phi(z\|x) \|\| p(z\|x)) - H(q_\Phi(z\|x)) + \log p(x)
\end{align}
$$
#### MathJax Bugs
One must use subscription before superscription to get correct rendering `xxx_{xxx}^{xxx}`. A reversed sub/superscription caused the parser to fail. This is because a underscore `_` is parsed as italic or emphasis by markdown compiler, when leading by non alphabetic characters.

# Reference
[^1]: [Mathjax CDN](https://cdnjs.com/libraries/mathjax/2.7.9)
[^2]: [Mathjax 3.2 Docs](https://www.osgeo.cn/mathjax/index.html)
[^3]: [Most used code for formal notations](https://oeis.org/wiki/List_of_LaTeX_mathematical_symbols)
[^4]: [Markdown cheetsheet](https://www.markdownguide.org/cheat-sheet/#extended-syntax)
[^5]: [Understanding Diffusion Models: A Unified Perspective](https://arxiv.org/abs/2208.11970)
[^6]: [Latex math font styles](https://www.physicsread.com/latex-mathematical-font/)
[^7]: [Understanding Diffusion Models: A Unified Perspective](https://arxiv.org/abs/2208.11970)
[^8]: [Gaussian linear models](https://ocw.mit.edu/courses/18-655-mathematical-statistics-spring-2016/b36cbb44af02cddb9dc42d92b767c462_MIT18_655S16_LecNote19.pdf)
[^9]: [Mathjax config converter](https://mathjax.github.io/MathJax-demos-web/convert-configuration/convert-configuration.html)
[^10]: [Mathjax Tex and packages](https://docs.mathjax.org/en/latest/input/tex/macros/index.html)


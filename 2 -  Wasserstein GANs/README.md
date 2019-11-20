### Date : 16 November 2019

## Links

### Papers
- [Wasserstein GAN](https://arxiv.org/abs/1701.07875)
- [Improved Training of Wasserstein GANs](https://arxiv.org/abs/1704.00028)
- [Spectral Normalization for Generative Adversarial Networks](https://openreview.net/forum?id=B1QRgziT-)
- [Wasserstein Divergence for GANs](https://arxiv.org/abs/1712.01026)

### Article
- [Efficiency on Spectral Normalization](https://christiancosgrove.com/blog/2018/01/04/spectral-normalization-explained.html)

### Practice
- [Colab](https://colab.research.google.com)
- [Torch nn Library](https://pytorch.org/docs/stable/nn.html)

## Result
### Generated Images 195 epochs
| WGAN          | WGAN-GP       | WGAN-SN       | WGAN-DIV       |
| ------------- | ------------- | ------------- |-------------   |
| ![WGAN](https://github.com/DSC-UI-SRIN/GAN/raw/master/Batch1/2%20-%20Minimax%20and%20Wasserstein%20Gan%20Formulations/images/result/wgan_195.png)  | ![WGAN-gp](https://github.com/DSC-UI-SRIN/GAN/raw/master/Batch1/2%20-%20Minimax%20and%20Wasserstein%20Gan%20Formulations/images/result/wgan-gp_195.png)  | ![WGAN-sn](https://github.com/DSC-UI-SRIN/GAN/raw/master/Batch1/2%20-%20Minimax%20and%20Wasserstein%20Gan%20Formulations/images/result/wgan-sn_195.png)  | ![WGAN-div](https://github.com/DSC-UI-SRIN/GAN/raw/master/Batch1/2%20-%20Minimax%20and%20Wasserstein%20Gan%20Formulations/images/result/wgan-div_195.png)  |

### Loss
|          	| Discriminator                                                                                                                                      	| Generator                                                                                                                                          	|
|----------	|----------------------------------------------------------------------------------------------------------------------------------------------------	|----------------------------------------------------------------------------------------------------------------------------------------------------	|
| WGAN     	| ![WGAN_D](https://github.com/DSC-UI-SRIN/GAN/raw/master/Batch1/2%20-%20Minimax%20and%20Wasserstein%20Gan%20Formulations/losses/wgan_d.png)         	| ![WGAN_G](https://github.com/DSC-UI-SRIN/GAN/raw/master/Batch1/2%20-%20Minimax%20and%20Wasserstein%20Gan%20Formulations/losses/wgan_g.png)         	|
| WGAN-GP  	| ![WGAN-GP_D](https://github.com/DSC-UI-SRIN/GAN/raw/master/Batch1/2%20-%20Minimax%20and%20Wasserstein%20Gan%20Formulations/losses/wgan-gp_d.png)   	| ![WGAN-GP_G](https://github.com/DSC-UI-SRIN/GAN/raw/master/Batch1/2%20-%20Minimax%20and%20Wasserstein%20Gan%20Formulations/losses/wgan-gp_g.png)   	|
| WGAN-SN  	| ![WGAN-SN_D](https://github.com/DSC-UI-SRIN/GAN/raw/master/Batch1/2%20-%20Minimax%20and%20Wasserstein%20Gan%20Formulations/losses/wgan-sn_d.png)   	| ![WGAN-SN_G](https://github.com/DSC-UI-SRIN/GAN/raw/master/Batch1/2%20-%20Minimax%20and%20Wasserstein%20Gan%20Formulations/losses/wgan-sn_g.png)   	|
| WGAN-DIV 	| ![WGAN-DIV_D](https://github.com/DSC-UI-SRIN/GAN/raw/master/Batch1/2%20-%20Minimax%20and%20Wasserstein%20Gan%20Formulations/losses/wgan-div_d.png) 	| ![WGAN-DIV_G](https://github.com/DSC-UI-SRIN/GAN/raw/master/Batch1/2%20-%20Minimax%20and%20Wasserstein%20Gan%20Formulations/losses/wgan-div_g.png) 	|

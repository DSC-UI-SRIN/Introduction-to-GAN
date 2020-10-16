# Introduction to Generative Adversarial Networks

## Summary

Generative model is biggest milestones toward unsupervised learning capability. Started from many realistic images generation use cases, generative model are now expanded many types of data such as text, videos and time series, open new opportunities to enhance vision, speech, NLU, graph mining and reinforcement domains. Recent advances in generative model is dominated by Generative Adversarial Network (GAN) which uses gamification two of deep neural networks (DNNs), one as generator G and the other as discriminator D. Typical GAN models can be interpreted using two perspectives, (1) adversarial competition and (2) divegence minimization. Supported with progresses in theoretical re-formulation of probability and statistical divergences, various regularization and normalization techniques, massive GAN models are proposed by AI research community, hence makes GANs harder to learn. 

This course is a "deep dive introduction of GANs" with a focus on learning end-to-end standard models for basic generative use cases like images, texts, voices and videos. During this 4-week course, students will learn "how to design, implement, train and evaluate state of art GAN models" as well as gain a detailed understanding of cutting-edge research in generative models. Started from vanilla minimax (MMGAN) and Non-Saturated (NSGAN) GAN formulations, this course will explain state of the art optimal transport based GAN, called Wasserstein GAN (WGAN). This course will teach common regularization techniques of WGAN, to ensure 1-Lipschitz continuity on critic function, also how to evaluate generated samples using common metrics like Inceptin Score (IS) and Frechet Inception Distance (FID). In 4th week of this course, we will review some GAN research progresses for vision, speech and NLU domains.   

## Prerequisites
- **Proficiency in Python**. All class assignments will be in PyTorch.
- **College Calculus, Linear Algebra**. Participants should be comfortable taking derivatives and understanding matrix vector operations and notation.
- **Basic Probability and Statistics**. Participants should know basics of probabilities, gaussian distributions, mean, standard deviation, maximum likelihood etc.
- **Basic Deep Neural Network**. Participants should understand basic deep neural network architectures such as MLP (Multi-layer Perceptron), DNN (Deep Feed-forward NN), CNN (Convolutional NN) and RNN/LSTM (Recurrent NN/Long Short Term Memory). Also, participants have to understand formulation of cost/loss functions, taking derivatives and performing optimization with gradient descent using back-propagation algorithm.

## Lecturers:
- **Risman Adnan**, Director, Software R&D, Samsung R&D Indonesia (SRIN)
- **Muchlisin Adi Saputra**, Lead AI Engineer (Vision and NLU), Samsung R&D Indonesia (SRIN)
- **Muhamad Iqbal**, Master Degree, Computer Science, University of Indonesia (SRIN Intern)

## Syllabus:

- Lecture 1: [Fundamental of GANs](https://github.com/DSC-UI-SRIN/Introduction-to-GAN/tree/master/1%20-%20Fundamental%20of%20GANs) (Lecture Slides, PyTorch Codes)
- Lecture 2: [Wasserstein GANs](https://github.com/DSC-UI-SRIN/Introduction-to-GAN/tree/master/2%20-%20%20Wasserstein%20GANs) (Lecture Slides, PyTorch Codes) 
- Lecture 3: [GAN Evaluations](https://github.com/DSC-UI-SRIN/Introduction-to-GAN/tree/master/3%20-%20GAN%20Evaluations) (Lecture Slides, PyTorch Codes)
- Lecture 4: [Applications of GANs](https://github.com/DSC-UI-SRIN/Introduction-to-GAN/tree/master/4%20-%20Applications%20of%20Gans) (Lecture Slides, PyTorch Codes)


## Other Notes
### Steps how to use our codes on [Colabs](https://colab.research.google.com/)
#### 1. Open https://colab.research.google.com/ <br>
![Colabs](https://github.com/DSC-UI-SRIN/GAN/raw/master/others/images/colabs.png)
#### 2. Open Tab File>Open notebook... or Ctrl+O<br>
![Colabs](https://github.com/DSC-UI-SRIN/GAN/raw/master/others/images/select_file.png)
#### 3. Select Tab Github, and Type "DSC-UI-SRIN" <br>
![Colabs](https://github.com/DSC-UI-SRIN/GAN/raw/master/others/images/select_git.png)
#### 4. Select notebook

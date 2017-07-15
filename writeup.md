Every major player in the automotive industry today is in a race to create autonomous cars, cars which will not require human intervention. 

One key reason why many believe that self driving cars can be a reality in near future is the recent scientific and technological advancements made in machine learning, in particular the progress made in implementing neural networks for recognizing and classifying images.

Inspired by this optimism, the current project explores the idea of using neural networks **alone** to train a car to drive on its own!

The project uses a simulator provided by Udacity. The simulator can be used to drive a car and capture images taken from three camera angles - left, right and center. Along with capturing the images, the simulator also records the steering angle corresponding to each image. This image/steering-angle pair becomes the data we need to learn a model to make the car drive autonomously. Specifically, the images become the features, the input to the model which then predicts an appropriate steering angle to keep the car on track and not wander off. 

---

**Behavioral Cloning Project Goals**

The goals / steps of this project are the following:
* Use the simulator to collect data of good driving behavior
* Build, a convolution neural network in Keras that predicts steering angles from images
* Train and validate the model with a training and validation set
* Test that the model successfully drives around track one without leaving the road


Augmentation and data collection

The input images

The stats

The preprocesed images

Architecture:
Two models were tried: 
1) Vairant of LeNet
2) Variant of Nvidia model 
The architecture which worked better was the Nvdia model. The structure of the model is as follows:

The learning curve

Keras was used to code the model up.    


Video


Conclusion


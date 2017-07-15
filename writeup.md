**Introduction**

Every major player in the automotive industry today is in a race to create autonomous cars, cars which will not require human intervention. 

One key reason why many believe that self driving cars can be a reality in near future is the recent scientific and technological advancements made in machine learning, in particular the progress made in implementing neural networks for recognizing and classifying images.

Inspired by this optimism, the current project explores the idea of using neural networks **alone** to train a car to drive on its own!

The project uses a simulator provided by Udacity. The simulator can be used to drive a car and capture images taken from three camera angles - left, right and center. Along with capturing the images, the simulator also records the steering angle corresponding to each image. This image/steering-angle pair becomes the data we need to learn a model to make the car drive autonomously. Specifically, the images become the features, the input to the model which then predicts an appropriate steering angle to keep the car on track and not wander off. 

[//]: # (Image References)

[image1]: ./images_writeup/sample_images.png "Sample Images"
[image2]: ./images_writeup/features_stats.png "Features Stats"




---

**Behavioral Cloning Project Goals**

The goals / steps of this project are the following:
* Use the Udacity simulator to collect data of good driving behavior
* Build, a convolution neural network in Keras that predicts steering angles from images
* Train and validate the model with a training and validation set
* Test that the model successfully drives around track one without leaving the road


**Augmentation and data collection**

The project initially included aroud 11000 x 3 imagaes. Just training with these images was not enough to train the model. Additional images were collected by driving the car in the training mode. In order **to reduce the bias towards learning only to drive counter-clockwise, the data was collected by driving the car in clockwise direction**. Also, **data was collected with car recovering from the edge of the road**. Collecting additional data significanty improved the model performance.   


**The input images**

Some sample center images (without any processing) which form the input to our model with their corresponding steering angles:
![alt text][image1]

In order to visualize the additional features available in the data, we plot below the histogram of the brake/speed/steerirng and throttle. These statistics are for images before augmentation. Only steering is what our model needs to predict. 
![alt text][image2]
It is clear from looking at the above figure that the data is highle un-balanced, with most of the data points corresponding to steering angle being zero. This is the reason it is extremely important to collect additional data to include scenarios where the car recovers from the edge by taking sharp turns.  


**The preprocesed images**

Architecture:
Two models were tried: 
1) Vairant of LeNet
2) Variant of Nvidia model 
The architecture which worked better was the Nvdia model. The structure of the model is as follows:

The learning curve

Keras was used to code the model up.    


Video


Conclusion


**Introduction**

Every major player in the automotive industry today is in a race to create autonomous cars, cars which will not require human intervention. 

One key reason why many believe that self driving cars can be a reality in near future is the recent scientific and technological advancements made in machine learning, in particular the progress made in implementing neural networks for recognizing and classifying images.

Inspired by this optimism, the current project explores the idea of using neural networks **alone** to train a car to drive on its own!

The project uses a simulator provided by Udacity. The simulator can be used to drive a car and capture images taken from three camera angles - left, right and center. Along with capturing the images, the simulator also records the steering angle corresponding to each image. This image/steering-angle pair becomes the data we need to learn a model to make the car drive autonomously. Specifically, the images become the features, the input to the model which then predicts an appropriate steering angle to keep the car on track and not wander off. 

[//]: # (Image References)

[image1]: ./images_writeup/sample_images.png "Sample Images"
[image2]: ./images_writeup/features_stats.png "Features Stats"
[image3]: ./images_writeup/processed_images.png "Preprocessed Images"





---

**Behavioral Cloning Project Goals**

The goals / steps of this project are the following:
* Use the Udacity simulator to collect data of good driving behavior
* Build a convolution neural network in Keras that predicts steering angles from images
* Train and validate the model with a training and validation set
* Test that the model successfully drives around track one without leaving the road


**Augmentation and data collection**

The project initially included aroud 11000 x 3 images. Just training with these images was not enough to train the model. Additional images were collected by driving the car in the training mode. In order **to reduce the bias towards learning only to drive counter-clockwise, data was collected by driving the car in clockwise direction**. Also, **data was collected with car recovering from the edge of the road**. Collecting additional data significanty improved the model performance.   


**The input images**

Some sample center images (without any processing) which form the input to our model with their corresponding steering angles:
![alt text][image1]

In order to visualize the additional features available in the data, we plot below the histogram of brake/speed/steerirng and throttle. Only steering is what our model needs to predict. 
![alt text][image2]
It is clear from looking at the above figure that the data is highly un-balanced, with most of the data points corresponding to steering angle being zero. These statistics are for images after augmentation. Before augmentation, the unbalance was even more and particular emphasis was given to increas the spread of steering angle distribution by collecting additional data to include scenarios where the car recovers from the edge by taking sharp turns.  

**The preprocesed images**
In order to help the model learn relevant features and not something which possibly cannot be useful for the task at hand, certain pre-processing was done before the model was fed to the initial layer of the neural-network. There were many pre-processing steps which were experimented with but the ones which were finally used are:
 * Cropping the image
 * Converting the image to grey scale
 * Histogram Equalizing
 * Normalizing the image

The images after pre-processing looked like the following:
![alt text][image3]


**Architecture**

Two models were tried: 
 * Vairant of LeNet
 * Variant of Nvidia model 
The architecture which worked better was the Nvdia model. The structure of the model is as follows:

| Layer (type)                     |Output Shape       |Params  |Connected to           |
|----------------------------------|-------------------|-------:|-----------------------|
|convolution2d_122 (Convolution2D) |(None, 36, 158, 24)|624     |convolution2d_input_53 |
|convolution2d_123 (Convolution2D) |(None, 16, 77, 36) |21636   |convolution2d_122      |
|convolution2d_124 (Convolution2D) |(None, 6, 37, 48)  |43248   |convolution2d_123      |
|convolution2d_125 (Convolution2D) |(None, 4, 35, 64)  |27712   |convolution2d_124      |
|convolution2d_126 (Convolution2D) |(None, 2, 33, 64)  |36928   |convolution2d_125      |
|dropout_9 (Dropout)               |(None, 2, 33, 64)  |0       |convolution2d_126      |
|flatten_39 (Flatten)              |(None, 4224)       |0       |dropout_9              |
|dense_90 (Dense)                  |(None, 100)        |422500  |flatten_39             |
|dense_91 (Dense)                  |(None, 50)         |5050    |dense_90               |
|dense_92(Dense)                   |(None, 10)         |510     |dense_91               |
|dense_93 (Dense)                  |(None, 1)          |11      |dense_92               |
|                                  |**Total params**   |558219  |                       |


Keras was used to code the model. Adam optimizer was used with mean-squared-error as the loss function for regression. The Keras default learning rate of 0.001 was used for the optimizer. The model was trainied in AWS cluster which were gpu enabled. Having gpu made trail and error and iteration very efficient.     

**Conclusion**

It was a great but challenging project to work with. The project was a good apportunity for me to explore Keras and read a lot of literature on autonomous driving. 


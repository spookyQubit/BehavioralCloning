As cars drving around without manual intervention comes closer to reality with every passing day, this project is a take on trying to teach a car

Every major player in the automotive industry today is in a race to create autonomous cars, cars which will not require human intervention. At the heart of realizing this utopia is the scientific and technological advancements made in the area of machine learning. In particular, the area which promises to hold the key to making autonomous 

One key reason why many believe that self driving cars can be a reality in near future is the recent scientific and technological advancements made in machine learning, in particular the progress made in implementing neural networks for recognizing aand classifying images.

Inspired by this optimism, the current project explores the idea of using neural networks **alone** to train a car to drive on its own!

i.e an end to end neural net trained self driving car!

The project uses a simulator provided by Udacity. The simulator can be used to drive a car and capture images taken from three camera angles - left, right and center. Along with capturing the images, the simulator also records the steering angle corresponding to each image. This image/steering-angle pair becomes the data we need to learn a model to make the car drive autonomously. Specifically, the images become the features, the input to the model, which then predicts an appropriate steering angle to keep the car on track and not wander off. 

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


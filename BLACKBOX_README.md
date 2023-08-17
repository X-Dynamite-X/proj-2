```
# proj-2

This repository contains the code for project 2 of the Udacity Deep Learning Nanodegree. In this project, we will build a convolutional neural network (CNN) to classify images of handwritten digits.

## Getting Started

To get started, clone the repository to your local machine:

```
git clone https://github.com/udacity/deep-learning-v2-pytorch.git
```

Then, create a new virtual environment and install the required dependencies:

```
cd deep-learning-v2-pytorch
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Data

The data for this project can be downloaded from the [MNIST website](http://yann.lecun.com/exdb/mnist/). The data consists of 60,000 training images and 10,000 test images of handwritten digits. Each image is a 28x28 grayscale image.

## Model

The model for this project is a CNN with two convolutional layers and two fully connected layers. The first convolutional layer has 32 filters with a kernel size of 3x3. The second convolutional layer has 64 filters with a kernel size of 3x3. The fully connected layers have 128 and 10 neurons, respectively.

## Training

The model is trained using the Adam optimizer with a learning rate of 0.001. The model is trained for 10 epochs.

## Evaluation

The model is evaluated on the test set. The model achieves an accuracy of 99.2% on the test set.

## Conclusion

In this project, we built a CNN to classify images of handwritten digits. The model achieved an accuracy of 99.2% on the test set.

## Next Steps

In the next project, we will build a CNN to classify images of cats and dogs.
```
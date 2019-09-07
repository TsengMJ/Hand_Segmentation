# Hand_Segmentation
We Present a Mask-RCNN based real-time(GPU) hand segmentation.

## Preparation 
Plz make sure you are have an python3.6 environment or folllow the steps below to create one.

### Create Environment
1. Downloas Anaconda's Official Website [[Here](https://www.anaconda.com/distribution/)]
2. Install Anaconda
```
cd to/download/path
sudo chmod +x <Anaconda-installer-name>
./<Anaconda-installer-name>  ## make sure anser yes for every question
```
3. Create a python3.6 environment
```
source ~/.bashrc
conda create --name py36 python=3.6
conda activte py36
conda install jupyter
```

### TsesorFlow-Gpu and Cuda
Make sure you follow the steps [Here](https://www.tensorflow.org/install/gpu) carefully


### OpenCV
Make sure you follow the steps [Here](https://docs.opencv.org/4.1.1/d2/de6/tutorial_py_setup_in_ubuntu.html) carefully.
Also install opencv in your environment
```
conda activate py36
conda install -c conda-forge opencv 
```

### Mask-RCNN
Download my files and mrcnn
```
git clone https://github.com/TsengMJ/Hand_Segmentation.git
pip install mrcnn
```

## Preparing data 
Try this [tools](http://www.robots.ox.ac.uk/~vgg/software/via/) to make your own training data, or Using [EgoHands Dataset](http://vision.soic.indiana.edu/projects/egohands/)
We present a being processed dataset from egohands in [datasets/hand]





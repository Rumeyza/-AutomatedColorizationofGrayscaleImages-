 # Automated Colorization of Grayscale Images with Deep Neural Networks #
Team Members:

[Eren Bilaloğlu](github.com/erenbilaloglu)  
Alper Dağgez  
[Rümeyza Dinçer](github.com/rumeyza)  
[Berk Durmuş](github.com/berkdurmus)  
[Eliz Tekcan](github.com/eliztekcan)  

## Dataset:

Colorization of gray scale images is very challenging task since it requires the knowledge of many different objects in wild. Thus, for this project we want to restrict the content of the images. Instead of using irrelevant and complicated pictures together, we would like to use urban and nature pictures in our project. MIT CVCL provides hundreds of images in urban and natural scene categories. Dataset is semantically separated and we are planning to use Open Country (411 images), Forest (329 images), Highway (261 images), Mountain (375 images) and Street (292 images) categories. All images are in RGB format and 256x256 pixels. Moreover, McGill Calibrated Colour Image Database also provides colour images in different categories. We will use Landscape (115 images) category from this dataset. Images in this dataset are 786x576 pixels so we need to do preprocessing to make every image in the same size. 

## Problem:

With the provided dataset our aim is to automate the colorization of black-and-white images. This capability has wide applications including image enhancement and restoration. Having the ability to distinguish colors, shapes and patterns within an image; objects can be correlated with colors. We aim to generate colorful version of images as output, based on colorful images that the system has learned from, given a gray scale image as input. The content of the images is limited to urban and nature pictures.

## Goal:

We intend to detect at least some basic structures in generic urban and natural images (like sky, trees, rivers etc.) and coloring them as it fits to a real version as much as possible. Our model will analyse some patterns in the picture by regarding various criterias. It should be able to assign different color for each segment. In later stages, we could try to increase accuracy of our models which provides better aesthetic and natural image colorification.


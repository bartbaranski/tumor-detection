<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>Brain Tumor Detection Project</title>
    <style>
      body {
        font-family: Arial, sans-serif;
        line-height: 1.6;
        margin: 20px;
      }
      h1, h2 {
        color: #333;
      }
      code {
        background-color: #f4f4f4;
        padding: 2px 4px;
        border-radius: 4px;
      }
      ul, ol {
        margin-left: 20px;
      }
    </style>
  </head>
  <body>
    <h1>Brain Tumor Detection Project</h1>
    
    <h2>Description</h2>
    <p>
      This project implements an automated brain tumor detection system using deep learning. It employs a Convolutional Neural Network (CNN) to analyze MRI images and classify them into two categories: <strong>tumor detected</strong> (YES) and <strong>no tumor</strong> (NO). The project comprises three main scripts:
    </p>
    <ul>
      <li><code>mainTrain.py</code> – used for training the CNN model.</li>
      <li><code>mainTest.py</code> – used for testing the model on individual images.</li>
      <li><code>app.py</code> – a GUI application for interactive image classification.</li>
    </ul>
    
    <h2>Technologies</h2>
    <ul>
      <li>Python</li>
      <li>TensorFlow</li>
      <li>Keras</li>
      <li>OpenCV</li>
      <li>PIL (Python Imaging Library)</li>
      <li>NumPy</li>
      <li>Scikit-learn</li>
      <li>Tkinter</li>
    </ul>
    
    <h2>Technologies Description</h2>
    <ul>
      <li><strong>Python:</strong> The primary programming language used to develop the project.</li>
      <li><strong>TensorFlow &amp; Keras:</strong> Frameworks used to build, train, and deploy the CNN model.</li>
      <li><strong>OpenCV &amp; PIL:</strong> Libraries for image processing, including reading, converting, and resizing images.</li>
      <li><strong>NumPy:</strong> Facilitates numerical operations and array handling crucial for processing image data.</li>
      <li><strong>Scikit-learn:</strong> Provides utilities such as train-test splitting for preparing the dataset.</li>
      <li><strong>Tkinter:</strong> Used to create the graphical user interface (GUI) that allows users to load and classify images interactively.</li>
    </ul>
    
    <h2>Features</h2>
    <ul>
      <li><strong>Data Preprocessing:</strong> Automatically loads images from organized directories (<code>datasets/yes</code> and <code

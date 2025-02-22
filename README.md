
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
      <li><strong>Data Preprocessing:</strong> Automatically loads images from organized directories (<code>datasets/yes</code> and <code>datasets/no</code>), resizes them to a consistent input size (64x64), and normalizes the data.</li>
      <li><strong>CNN Model Training:</strong> Constructs a CNN with multiple convolutional and pooling layers to extract features from MRI images, followed by dense layers for classification.</li>
      <li><strong>Model Testing:</strong> Includes a testing script to evaluate the model on individual images and print prediction results.</li>
      <li><strong>Graphical User Interface:</strong> Provides a user-friendly GUI that allows users to load an image, display it, and receive an immediate classification result.</li>
      <li><strong>Model Saving:</strong> Saves the trained model in an H5 file format for later use or deployment.</li>
    </ul>
    
    <h2>Usage</h2>
    <ol>
      <li>
        <strong>Training the Model:</strong>
        <ul>
          <li>Run <code>mainTrain.py</code> to preprocess the dataset and train the CNN model using images stored in the <code>datasets</code> folder (separated into <code>yes</code> and <code>no</code> subdirectories).</li>
          <li>The model is trained over a set number of epochs (10 in this case) and then saved to a file (e.g., <code>tumor10EpCat.h5</code>).</li>
        </ul>
      </li>
      <li>
        <strong>Testing the Model:</strong>
        <ul>
          <li>Execute <code>mainTest.py</code> to load the trained model and perform a prediction on a sample image located in the <code>pred</code> folder.</li>
          <li>The script resizes the image to the required input dimensions, performs the classification, and prints out the results.</li>
        </ul>
      </li>
      <li>
        <strong>Using the GUI Application:</strong>
        <ul>
          <li>Launch <code>app.py</code> to open a graphical user interface where you can load any image from your computer.</li>
          <li>Once loaded, the image is displayed, and clicking the "Classify" button will process the image through the model, displaying whether a tumor is detected or not.</li>
        </ul>
      </li>
      <li>
        <strong>Directory Structure:</strong>
        <ul>
          <li><code>datasets/</code> contains two folders: <code>yes/</code> (images with tumors) and <code>no/</code> (images without tumors).</li>
          <li><code>pred/</code> holds images for testing predictions.</li>
          <li>The project files (<code>mainTrain.py</code>, <code>mainTest.py</code>, <code>app.py</code>, and model files) are organized in the project’s root directory.</li>
        </ul>
      </li>
    </ol>
    
    <h2>Future Improvements</h2>
    <ul>
      <li><strong>Data Augmentation:</strong> Implement techniques to artificially expand the dataset (e.g., rotations, flips, scaling) to improve model generalization.</li>
      <li><strong>Advanced Architectures:</strong> Experiment with more sophisticated CNN architectures or transfer learning methods to enhance detection accuracy.</li>
      <li><strong>Performance Visualization:</strong> Integrate tools to visualize training progress (e.g., loss and accuracy plots) and monitor model performance in real time.</li>
      <li><strong>GUI Enhancements:</strong> Expand the GUI to support batch processing, additional image formats, and display more detailed prediction metrics.</li>
      <li><strong>Hyperparameter Tuning:</strong> Incorporate automated methods for hyperparameter tuning to optimize the model’s performance.</li>
      <li><strong>Deployment Optimization:</strong> Explore options to optimize the model for deployment on mobile or web platforms, ensuring efficient and robust real-world performance.</li>
    </ul>


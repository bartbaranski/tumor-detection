<h1>Deep Learning for Automated Brain Tumor Detection in MRI Images</h1>

<h2>Conference Poster -  6th Polish Conference on Artificial Intelligence, PP-RAI 2025, 7-9 April 2025, Katowice</h2>
<p>https://bartbaranski.github.io/tumor-detection/MRI_tumor_poster_bb.pdf</p>

<h2>Jupyter File</h2>
<p>https://bartbaranski.github.io/tumor-detection/braintumor.html</p>

<h2>Description</h2>
<p>
  This repository contains the code and associated poster for the project “Deep Learning for Automated Brain Tumor Detection in MRI Images.” The project aims to develop an automated method for detecting brain tumors in MRI images using a Convolutional Neural Network (CNN). A curated dataset of 3060 brain MRI images from Kaggle’s Br35H :: Brain Tumor Detection 2020 collection is employed. Images from the “yes” (tumorous) and “no” (non-tumorous) subsets (3000 images total) were used for training and validation in an 80:20 split, with each image resized to 64×64 pixels, normalized, and its label converted to one-hot encoding. The final model achieved a training accuracy of 99.08% (loss = 0.0322), a validation accuracy of 97.12% (loss = 0.1130), and a test accuracy of 98.00% (loss = 0.1565). Comprehensive evaluation using precision, recall, and F1 score, along with confusion matrices, demonstrates the model’s robust performance and strong potential for clinical application.
</p>

<h2>Technologies</h2>
<ul>
  <li>Python</li>
  <li>TensorFlow / Keras</li>
  <li>OpenCV</li>
  <li>PIL (Python Imaging Library)</li>
  <li>NumPy</li>
  <li>Scikit-learn</li>
  <li>Tkinter</li>
  <li>Matplotlib</li>
  <li>LaTeX (BeamerPoster)</li>
</ul>

<h2>Technologies Description</h2>
<p>
  This project is implemented in Python using TensorFlow and Keras for the construction, training, and evaluation of deep learning models. OpenCV and PIL are utilized for image processing and augmentation, ensuring that the MRI images are consistently preprocessed. NumPy provides essential data     structures for numerical computations, while scikit-learn is used for dataset splitting and evaluation metrics such as confusion matrices and classification reports. Keras Tuner is employed to perform advanced hyperparameter tuning—including batch size, number of convolutional layers, filters, kernel sizes, dropout rate, and learning rate—to optimize the model. Visualization of training dynamics and evaluation outcomes is achieved through Matplotlib and Seaborn. The project documentation also includes a conference poster produced using LaTeX with the BeamerPoster package.
</p>
<h2>Features</h2>
<ul>
  <li><strong>Automated Tumor Detection:</strong> Implements a CNN-based approach for automated detection of brain tumors in MRI images.</li>
  <li><strong>High Performance:</strong> The final CNN model achieves outstanding accuracy - 98% on the test set—with high precision and recall, minimizing the risk of missed diagnoses.</li>
  <li><strong>Data Preprocessing:</strong> Images are resized, normalized, and encoded consistently to ensure reliable input for the CNN.</li>
  <li><strong>Advanced Hyperparameter Tuning:</strong> Keras Tuner is used to systematically optimize key hyperparameters (including batch size), resulting in an architecture that performs significantly better than baseline methods.</li>
  <li><strong>Robust Evaluation:</strong> Comprehensive performance metrics (accuracy, loss, precision, recall, F1 score) and detailed evaluation (confusion matrix, classification report) provide insight into model efficacy.</li>
  <li><strong>Visualizations:</strong> Training and validation curves, a confusion matrix heatmap, and a comparative bar chart highlight performance trends and confirm robustness.</li>
</ul>


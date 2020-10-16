This is a repo containing all the work for tensorflow specialisation on coursera provided by deeplearning.ai
## Course 1 - Introduction to TensorFlow for Artificial Intelligence, Machine Learning, and Deep Learning

Started with the introduction to simple Neural Network implemented using TensorFlow <br>
a. First practical implemented through housing price prediction <br>
b. Second handwritten recognition using callback function with the epochs terminating at set accuracy termination after the epoch is completed. <br>
c. Improving the accuracy and precision for a dataset using Convolutional layer and single max pooling.<br>
    1. Convolutions are a way to extract particular features from a image. Technically, A convolution is the simple application of a filter to an input that results in an activation. Repeated application of the same filter to an input results in a map of activations called a feature map, indicating the locations and strength of a detected feature in an input, such as an image.<br>
  2. Pooling layers are placed immediately after CNN declaration. It takes the input from the user as a feature map which comes out convolutional networks and prepares a condensed feature map. Pooling layers help in creating layers with neurons of previous layers.<br>
d. Handling Complex Images with three convolutional layers model of CNN. Callback function to cancel training incase it reaches 99.99% in training the model.<br>

Activation Function are used to get the output of the node. The major activation functions used here are relu and sigmoid. ReLu is Rectified linear Unit and is used in almost all deep learning networks. The fucntion is given by R(z)=max(0,z). It shows the shape of a ramp fucntion. The next activation function is the Sigmoid which is a S - Shape curve and has an output between (0,1). It is used majorly in probability cases because of its output range.<br>

<h3> So overall main concepts here : -</h3><br>
1. Callback function<br>
2. Activation function<br>
3. Convolution and Pooling in training layers of CNN<br>

## Course 2 - Convolutional Neural Networks in Tensorflow

a. Splitting the whole data into sets validation and training data. The validation data is used majorly for giving us the info about adjusting our hyperparameters.<br>
The loss function used here is Binary Crossentropy which is used when we have binary classification i.e. distinguishing between two sets of classes which the question utilises i.e. Cats vs Dogs. The model is trainied for two epochs and then validation and the testing accuracy and loss are plotted on using matplotlib library.<br>
b. Data  Augmentation is one of the ways to improve model accuracy by modifying the images to a certain level. Be it magnification, rotation,  Skewing, Zooming, Shearing etc. This helps us to get closer to the training data as the model's accuracy increases.<br>
c. Transfer learning is an optimization that allows rapid progress or improved performance when modeling the second task which is because it uses pre-trained model for developing the second model. It gives better performance of the model.<br>
d. Multi Class Classifier is used in case we have to distinguish between three or more classes like Rock,Papers and Scissors. The only changes that we make here from the binary classification are to the loss function which is changed to "Categorical_Crossentropy" and the last layer's activation function set to "softmax".

<h3> So overall main concepts here : -</h3><br>
1. Validation Data<br>
2. Data Augmentation<br>
3. Transfer Learning<br>
4. Binary and Categorical Crossentropy <br>
5. Softmax Activation Fucntion<br>


## Course 3 - Natural Language Processing using Tensorflow

a. Tokenisation is one of the most important part of NLP. It is the process of defining each word as a token and then making a dictionary of it using keys and words. Simply it's the process of splitting the text into smaller tokens. Padding is one of the ways of making the length of each line uniform. Incase of shortage, zeroes are added in front or last of the sequence depending on how the padding is set or incase of excess we can also truncate the data from either sides.<br>
b. In case of prediction if it finds a word which is not there in the training set, we have a oov_tok set equal to something which replaces the word. CNN model is used for doing predictive modelling with the output layer set to softmax activation. <br>
c. Corpus is a large collection of texts. Every text in the csv file is appended to the corpus. LSTM is long short term memory which is a recurrent neural network and carries the cell state from the previous to the next cell state which is used for predicting the words ahead based on training data.<br>

<h3> So overall main concepts here : -</h3><br>
1. Tokenisation
2. Corpus
3. LSTM / Recurrent Neural Network

## Course 4 - Sequence, Time Series and Prediction


 

# Iris flower classification using FastAPI

## About the Dataset
The Iris flower data set is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in his 1936 paper The use of multiple measurements in taxonomic problems. It is sometimes called Anderson's Iris data set because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species. The data set consists of 50 samples from each of three species of Iris (Iris Setosa, Iris virginica, and Iris versicolor). Four features were measured from each sample: the length and the width of the sepals and petals, in centimeters. <br>
<img src="https://editor.analyticsvidhya.com/uploads/51518iris%20img1.png"/>

Python Notebook: <br>
https://www.kaggle.com/code/venkatkrishnan/iris-data-tensorflow-neural-network

Saving model
* h5 = model.save('/kaggle/working/something.h5')
* pb = tf.saved_model.save(model, "my_model")

Run using: <br>
`uvicorn main:app`

Don't forget that FastAPI supports API preview through: <br> 
`http://<ip>:<port>/docs`

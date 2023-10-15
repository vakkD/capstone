# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing import image
# from tensorflow.keras.applications.vgg16 import preprocess_input
# import numpy as np

# # load the saved model
# model = load_model('L:/!school/!uni/!classes/sem2-2023/software technology/assignments/assignment 2/code/model.h5')

# # load an image from file
# image_path = "L:/!school/!uni/!classes/sem2-2023/software technology/assignments/assignment 2/lung_colon_image_set/lung_image_sets/lung_scc/lungscc4.jpeg"
# img = image.load_img(image_path, target_size=(224, 224))

# # Convert the image to numpy array
# img_array = image.img_to_array(img)

# # The model expects 4D input hence expand dimensions
# img_batch = np.expand_dims(img_array, axis=0)

# # Preprocess the image
# img_preprocessed = preprocess_input(img_batch)

# # Make a prediction
# prediction = model.predict(img_preprocessed)

# # Print the prediction
# print(prediction)

# # If you want the index of the highest probability, use argmax
# print(np.argmax(prediction))  # If your model uses categorical encoding

# # If your model uses binary encoding and you want the output to be the predicted class, use round
# print(np.round(prediction)) 
import pickle

from PIL import Image
import numpy as np

# Open the image file
img = Image.open("L:/!school/!uni/!classes/sem2-2023/software technology/assignments/assignment 2/lung_colon_image_set/lung_image_sets/lung_scc/lungscc4.jpeg")

# Resize and convert the image into numpy array or any method of preprocessing
img = img.resize((64,64)) # replace this with whatever size your model was trained with
img_array = np.array(img)

# Reshape it to be the correct dimensions that your model expects.
# The '1' at the start indicates that we're predicting for 1 image
# You need to update this according to how your inputs were pre-processed
img_array = img_array.reshape(1, -1)

# Now load the saved model
with open('L:/!school/!uni/!classes/sem2-2023/software technology/assignments/assignment 2/code/rf_classifier.pkl', 'rb') as file:
    clf_from_pickle = pickle.load(file)

# Predict the class of the image
prediction = clf_from_pickle.predict(img_array)

print(prediction)


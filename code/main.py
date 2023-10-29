import tkinter as tk
import tkinter.ttk as ttk

window = tk.Tk()
window.geometry('306x344')

temp_label = tk.Label(window, text='Loading libraries')
temp_label.pack()


def load_libraries():
    temp_label.config(text='Loading libraries...')
    window.update_idletasks()
    
    global fd,pd,os,Image,ImageTk,np,tf
    import tensorflow as tf
    from PIL import Image, ImageTk
    import numpy as np
    from tensorflow.keras.optimizers import Adamax
    from tkinter import filedialog as fd
    import pandas as pd
    import os
    print('Libraries loaded')

    global loaded_model
    try:
        loaded_model = tf.keras.models.load_model('L:/!school/!uni/!classes/sem2-2023/software technology/assignments/assignment 2/code/newmodel.h5', compile=False)
    except FileNotFoundError:
        loaded_model = tf.keras.models.load_model('C:/Users/dylan/OneDrive/school/sem2-2023/software technology/assignments/assignment 2/code/newmodel.h5', compile=False)
    except:
        temp_label.config(text='Error: model not found')

    loaded_model.compile(Adamax(learning_rate=0.001), loss='categorical_crossentropy', metrics=['accuracy'])
    temp_label.destroy()

window.after(100, load_libraries)

file_predictions = []
filepath ='/'
selected_files =[]
num_selected_files =0

tk.Label(window, text ='Selected file(s)')
file_listbox =tk.Listbox(window, selectmode =tk.MULTIPLE)
file_listbox.pack()

def select_file():
    global filepath, selected_files, num_selected_files
    filenames =fd.askopenfilenames(title ='Select file(s)', initialdir =filepath, filetypes =[('Image', '*.jpeg .png')])
    selected_files =[file for file in filenames]
    num_selected_files =len(selected_files)
    filepath =selected_files[0]
    update_file_listbox()
    display_image()

def select_folder():
    global filepath, selected_files, num_selected_files
    directory =fd.askdirectory(title ='Select a directory', initialdir =filepath)
    selected_files =get_all_files(directory)
    num_selected_files =len(selected_files)
    filepath =selected_files[0]
    update_file_listbox()

def display_image():
    if num_selected_files ==1:
        img = Image.open(filepath)
        img = img.resize((128,128),Image.LANCZOS)
        image = ImageTk.PhotoImage(img)
        image_label.config(image = image)
        image_label.image = image
        window.geometry('306x462')
    else:
        image_label.config(image='')
        window.geometry('306x344')

def update_file_listbox():
    file_listbox.delete(0, tk.END)
    for file in selected_files:
        file_listbox.insert(tk.END, file.split('/')[-1])
        
    confidence_label.config(text='')
    predicted_label.config(text='')

def get_all_files(directory):
    files =[]
    extensions =['.jpg', '.jpeg', '.png']
    for path, _, filenames in os.walk(directory):
        for filename in filenames:
            if any(extension in filename.lower() for extension in extensions):
                files.append(os.path.join(path, filename))
    return files

def predict():
    global file_predictions
    
    file_predictions.clear()
    
    for file_path in selected_files:
        image =Image.open(file_path)
        img =image.resize((224, 224))
        img_array =tf.keras.preprocessing.image.img_to_array(img)
        img_array =np.expand_dims(img_array, 0)
        img_array =img_array / 255.0
    
        predictions =loaded_model.predict(img_array)
        class_labels ={
            0: 'Colon Adenocarcinoma',
            1: 'Colon Benign Tissue',
            2: 'Lung Adenocarcinoma',
            3: 'Lung Benign Tissue',
            4: 'Lung Squamous Cell Carcinoma'
        }
        predicted_class =np.argmax(predictions[0])
    
        class_prediction =class_labels[predicted_class]
        confidence =f'{round(predictions[0][predicted_class]*100, 2)}%'
        
        file_predictions.append({
            'File Name': file_path.split('/')[-1],
            'Predicted Class': class_prediction,
            'Confidence': confidence,
            'File Path': file_path
        })
    
    if num_selected_files  ==1:
        predicted_label.config(text =f'Predicted Class: {file_predictions[0]["Predicted Class"]}')
        confidence_label.config(text =f'Confidence: {file_predictions[0]["Confidence"]}')
    else:
        predictions_file_name  ='predictions'
        df =pd.DataFrame(file_predictions)
        df.to_excel(f'{predictions_file_name}.xlsx', index =False)
        predicted_label.config(text =f'Predictions saved to {predictions_file_name}.xlsx')
        confidence_label.config(text ='')

def open_image_grid():
    image_window =tk.Toplevel(window)
    image_window.title('Images')
    
    image_width =200
    image_height =200
    num_cols =4
    row =0
    col =0
    images =[]

    image_window.geometry(f'{(image_width*num_cols)+40}x{(image_height*2)+55}')

    canvas =tk.Canvas(image_window)
    canvas.pack(side =tk.LEFT, fill =tk.BOTH, expand =True)

    scrollbar =ttk.Scrollbar(image_window, orient =tk.VERTICAL, command =canvas.yview)
    scrollbar.pack(side =tk.RIGHT, fill =tk.Y)

    canvas.configure(yscrollcommand =scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion =canvas.bbox('all')))

    frame =tk.Frame(canvas)
    canvas.create_window((0, 0), window =frame, anchor =tk.NW)

    labels =[]
    for file_path in selected_files:
        image =Image.open(file_path)
        image =image.resize((image_width, image_height))
        photo =ImageTk.PhotoImage(image)

        label =tk.Label(frame, image =photo)
        label.image =photo
        label.grid(row =row, column =col)
        
        file_name_label =tk.Label(frame, text =file_path.split('/')[-1])
        file_name_label.grid(row =row+1, column =col)

        col +=1
        if col >=num_cols:
            col =0
            row += 2

        images.append(photo)
        labels.append(file_name_label)

    canvas.update()
    canvas.configure(scrollregion =canvas.bbox('all'))

open_file_button =tk.Button(window, text ='Select file(s)', command =select_file)
open_file_button.pack()

open_folder_button =tk.Button(window, text ='Select directory', command =select_folder)
open_folder_button.pack()

open_image_button =tk.Button(window, text ='Open image(s)', command =open_image_grid)
open_image_button.pack()

predict_button =tk.Button(window, text ='Predict', command =predict)
predict_button.pack()

image_label =tk.Label(window)
image_label.pack()

predicted_label =tk.Label(window)
predicted_label.pack()

confidence_label =tk.Label(window)
confidence_label.pack()

window.mainloop()
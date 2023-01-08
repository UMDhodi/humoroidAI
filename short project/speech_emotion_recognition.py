from numpy.core.fromnumeric import size
from numpy.lib.npyio import load
import librosa
import soundfiles
import os, glob, pickle
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier 
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

#Extract features (mfcc, chroma, mel) from a sound file
def extract_feature(file_name, mfcc, chroma, mel):
    with soundfile.SoundFile(file_name) as sound_file:
        x, sample_rate = librosa.load(file_name)
        if chroma:
            stft = np.abs(librosa.stft(x))
            result = np.array([])

        if mfcc:
            mfccs = np.mean(librosa.feature.mfcc(y=x, sr=sample_rate, n_mfcc=40).T, axis=0) 
            result = np.hstack((result, mfccs))

        if chroma:
            chroma = np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T, axis=0)    
            result =np.hstack((result, chroma))

        if mel:
            mel = np.mean(librosa.feature.melspectrogram(x, sr=sample_rate).T, axis=0)    
        return result

#Emotons in the RAVDESS dataset

emotions={
    '01':'neutral',
    '02':'calm',
    '03':'happy',
    '04':'sad',
    '05':'angry',
    '06':'fearful',
    '07':'disgust',
    '08':'surprised',
}            
observed_emotions = ['calm', 'happy', 'disgust', 'fearful']

#Load tha data and extract feature for each sound file
def load_data(test_size=0.2):
    x,y = [],[]
    actor = []
    for file in glob.glob("# wav file path input"):
        file_name = os.path.basename(file)
        emotion = emotions[file_name.split("_")[2]]
        if emotion not in observed_emotions:
            continue
        feature = extract_feature(file, mfcc=True, chroma=True, mel=True)
        x.append(feature)
        y.append(emotion)
    return train_test_split(np.array(x), y, test_size=test_size, random_state=9)    
#Split the dataset
x_train, x_test, y_train, y_test = load_data(text_size = 0.25)

#Get the shape of the training and testing datasets
print((x_train.shape[0], x_test.shape[0]))

#Get the number of feature extracted
print(f'Features extracted: {x_train.shape[1]}')

#Initialize the multi layer perceptron classifier
model = MLPClassifier(alpha=0.01, batch_size=256, epsilon=1e-08, hidden_layer_size=(300,), learning_rate='adaptive', max_iter=700)

#Train the model
model.fit(x_train, y_train)

#Predict for the test set
y_pred = model.predict(x_test)

#Calculate the accurancy of our model
accuracy = accuracy_score(y_true = y_test, y_pred = y_pred)
print("Accuracy: {:.2f}%".format(accuracy*100))

#Classification_report
print(classification_report(y_test, y_pred))

#Confusion_matrix
cm = confusion_matrix(y_test, y_pred)
df_cm = pd.DataFrame(cm)
sns.heatmap(df_cm, annot=True, fmt='')
plt.title('Confusion Matrix', size=20)
plt.xlabel('Predicted Labels', size=14)
plt.ylabel('Actual Labels', size=14)
plt.savefig('Initial_Model_Confusion Matrix.png')
plt.show()

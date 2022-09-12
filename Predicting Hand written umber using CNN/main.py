import keras
import tensorflow as tf
from keras.datasets import mnist
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Conv2D, Dense,Flatten


(x_train, y_train), (x_test, y_test) = mnist.load_data()
print(x_train[0].shape)
plt.imshow(x_train[0])
plt.show()

print(x_train.shape, y_train.shape)



#data visualization
#sinc CNN model needs to one more domenesion why?
x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)

#data preprocessing
#one hot tncoding the output column
#one-hot encode target column

y_train = tf.keras.utils.to_categorical(y_train,num_classes=None, dtype="float32")
y_test = tf.keras.utils.to_categorical(y_test, num_classes=None, dtype="float32")
print(y_train[0])
#plot the first image in the dataset
# print(x_train[0].shape)
# plt.imshow(x_train[0])
# plt.show()

#model building

model = Sequential()
model.add(Conv2D(64,kernel_size=3,activation="relu",input_shape=(28,28,1)))
model.add(Conv2D(32,kernel_size=3,activation="relu"))
model.add(Flatten())
model.add(Dense(10,activation="softmax"))

#compiling the model
model.compile(optimizer='adam',loss= "categorical_crossentropy",metrics=["accuracy"])
# model.compile(loss=keras.losses.categorical_crossentropy,optimizer=keras.optimizers.Adadelta(),metrics=['accuracy'])

#train the model
model.fit(x_train,y_train,epochs=3,validation_data=(x_test,y_test))
# hist = model.fit(x_train, y_train,batch_size=batch_size,epochs=epochs,verbose=1,validation_data=(x_test, y_test)
print("The model has successfully trained")
model.save('mnist.h5')
print("Saving the model as mnist.h5")

#evaluate the model
score = model.evaluate(x_test,y_test)
print(score)

#predict first 4 images in the test set
print(model.predict(x_test[:4]))


#build the GUI to predict handwriten


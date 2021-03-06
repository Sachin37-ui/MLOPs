


# ### Let's freeze all layers except the top 4 

# In[3]:


from keras.applications import VGG16

# VGG16 was designed to work on 224 x 224 pixel input images sizes
img_rows = 224
img_cols = 224 

# Re-loads the VGG16 model without the top or FC layers
model = VGG16(weights = 'imagenet', 
                 include_top = False, 
                 input_shape = (img_rows, img_cols, 3))


for layer in model.layers:
    layer.trainable = False
    
# Let's print our layers 
for (i,layer) in enumerate(model.layers):
    print(str(i) + " "+ layer.__class__.__name__, layer.trainable)


# ### Let's make a function that returns our FC Head

# In[5]:

units = int(256)

def addTopModel(bottom_model, num_classes,unit):
      top_model = bottom_model.output
      top_model = Flatten(name = "flatten")(top_model)
      top_model = Dense(unit, activation = "relu")(top_model)
      top_model = Dropout(0.3)(top_model)
      top_model = Dense(num_classes, activation = "softmax")(top_model)
      return top_model




from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D, ZeroPadding2D
from keras.layers.normalization import BatchNormalization
from keras.models import Model

num_classes = 17

FC_Head = addTopModel(model, num_classes,units)

modelnew = Model(inputs=model.input, outputs=FC_Head)
print(modelnew.summary())

 





# ### Loading our Flowers Dataset

# In[9]:
from keras.preprocessing.image import ImageDataGenerator

train_data_dir = '/root/17_flowers/17_flowers/train'
validation_data_dir = '/root/17_flowers/17_flowers/validation'

train_datagen = ImageDataGenerator(
      rescale=1./255,
      rotation_range=20,
      width_shift_range=0.2,
      height_shift_range=0.2,
      horizontal_flip=True,
      fill_mode='nearest')
 
validation_datagen = ImageDataGenerator(rescale=1./255)
 
# Change the batchsize according to your system RAM
train_batchsize = 16
val_batchsize = 10
 
train_generator = train_datagen.flow_from_directory(
        train_data_dir,
        target_size=(img_rows, img_cols),
        batch_size=train_batchsize,
        class_mode='categorical')
 
validation_generator = validation_datagen.flow_from_directory(
        validation_data_dir,
        target_size=(img_rows, img_cols),
        batch_size=val_batchsize,
        class_mode='categorical',
        shuffle=False)


# ### Training our top layers

# In[ ]:

from keras.optimizers import RMSprop
from keras.callbacks import ModelCheckpoint, EarlyStopping
                   
checkpoint = ModelCheckpoint("flowers_vgg.h5",
                        monitor="val_loss",
                        mode="min",
                        save_best_only = True,
                        verbose=1)

earlystop = EarlyStopping(monitor = 'val_loss', 
                          min_delta = 0, 
                          patience = 3,
                          verbose = 1,
                          restore_best_weights = True)

# we put our call backs into a callback list
callbacks = [earlystop, checkpoint]

# Note we use a very small learning rate 
modelnew.compile(loss = 'categorical_crossentropy',
              optimizer = RMSprop(lr = 0.001),
              metrics = ['accuracy'])

nb_train_samples = 957
nb_validation_samples = 60
epochs = 2
batch_size = 16

history = modelnew.fit_generator(
     train_generator,
     steps_per_epoch = nb_train_samples // batch_size,
     epochs = epochs,
     callbacks = callbacks,
     validation_data = validation_generator,
     validation_steps = nb_validation_samples // batch_size)
modelnew.save("flowers_vgg.h5")
acc = history.history['accuracy']
final_acc = max(acc)
final_acc = final_acc*100
print(final_acc)
if(final_acc<=85):
   import smtplib
   s=smtplib.SMTP('smtp.gmail.com',587)
   s.starttls()
   s.login("tendlysachin8@gmail.com","Sarthak2@15")
   message="your model succesfully trained but didn't get the desired accuracy"
   s.sendmail("tendlysachin8@gmail.com","sm026552@gmail.com",message)
   print("mail sent")
   s.quit()
  
else:
   import smtplib
   s=smtplib.SMTP('smtp.gmail.com',587)
   s.starttls()
   s.login("tendlysachin8@gmail.com","Sarthak2@15")
   message="your model successfully trained and this time your model achieved desired accuracy "
   s.sendmail("tendlysachin8@gmail.com","sm026552@gmail.com",message)
   print("mail sent")
   s.quit()
  
  
  

    


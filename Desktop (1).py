#!/usr/bin/env python
# coding: utf-8

# In[ ]:


1 what does RGBA stand for ?

ans Red-Green-Blue-Alpha
    


# In[ ]:


get_ipython().set_next_input('2. From the Pillow module, how do you get the RGBA value of any images');get_ipython().run_line_magic('pinfo', 'images')

ans  Pillow offers the ImageColor. getcolor() function so you don't have to memorize RGBA values for the colors you want to use. This function takes a color name string as its first argument, and the string 'RGBA' as its second argument, and it returns an RGBA tuple.


# In[ ]:


get_ipython().set_next_input('3. What is a box tuple, and how does it work');get_ipython().run_line_magic('pinfo', 'work')

ans The box. tuple submodule provides read-only access for the tuple userdata type. It allows, for a single tuple: selective retrieval of the field contents, retrieval of information about size, iteration over all the fields, and conversion to a Lua table..


# In[1]:


get_ipython().set_next_input('4. Use your image and load in notebook then, How can you find out the width and height of an Image object');get_ipython().run_line_magic('pinfo', 'object')


# In[2]:


from PIL import Image
  
filepath = "cat.jpg"
img = Image.open("C:\\Users\\ACER\\OneDrive\\Desktop\\cat\\cat.jpg")
  
width,height = img.size
  

print("The height of the image is: ", height)
print("The width of the image is: ", width)


# In[ ]:


get_ipython().set_next_input('5. What method would you call to get Image object for a 100×100 image, excluding the lower-left quarter of it');get_ipython().run_line_magic('pinfo', 'it')

ans from PIL import Image

      # Open the image file
    image = Image.open('image_file.png')

      # Crop the image to exclude the lower-left quarter
    cropped_image = image.crop((0, 0, 50, 50))

      # Display the cropped image
    cropped_image.show()


# In[ ]:


get_ipython().set_next_input('6. After making changes to an Image object, how could you save it as an image file');get_ipython().run_line_magic('pinfo', 'file')

and. from PIL import Image

# Open the original image file
img = Image.open('original_image.jpg')

# Make changes to the Image object

# Save the Image object as a new JPEG file
img.save('new_image.jpg', 'JPEG')


# In[ ]:


get_ipython().set_next_input('7. What module contains Pillow’s shape-drawing code');get_ipython().run_line_magic('pinfo', 'code')

ans from PIL import Image, ImageDraw


# In[ ]:


get_ipython().set_next_input('8. Image objects do not have drawing methods. What kind of object does? How do you get this kind of object');get_ipython().run_line_magic('pinfo', 'object')

ans Image objects in the Pillow library (PIL) do not have built-in drawing methods. Instead, you can use the ImageDraw module to create a separate ImageDraw object that you can use to draw shapes and other graphical elements on the image.

To get an ImageDraw object, you need to create it using the ImageDraw.Draw() method and pass in the Image object you want to draw on.


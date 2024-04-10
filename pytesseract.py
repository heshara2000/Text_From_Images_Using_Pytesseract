#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pytesseract
pytesseract.pytesseract.tesseract_cmd =r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


# In[2]:


import cv2


# In[ ]:


img=cv2.imread('C:\\Users\\HP\\Desktop\\4.png')
cv2.imshow('sampple image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[5]:


text=pytesseract.image_to_string(img)
print(text)


# In[ ]:





# In[ ]:





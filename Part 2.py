#!/usr/bin/env python
# coding: utf-8

# In[42]:


class Book(object):
    author = ""
    title = ""
  
    def __init__(self,author,title):
        self.author = author
        self.title = title
  
    def display(self):
        y = "%s written by %s" % (self.title,self.author)
        print(y)

book1 = Book("John Steinbeck", "Of Mice and Men")
book2 = Book("Harper Lee", "To Kill a Mockingbird")

book1.display()
book2.display()


#!/usr/bin/env python
# coding: utf-8

# In[4]:


from textblob import TextBlob
from flask import Flask
from flask import render_template, request


# In[5]:


app = Flask(__name__)


# In[6]:


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        test = request.form.get("text")
        print(text)
        r = TextBlob(text).sentiment
        return(render_template("index.html", results=r))
    else:
        return(render_template("index.html", results="waiting..."))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:





# In[ ]:





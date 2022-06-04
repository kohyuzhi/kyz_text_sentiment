#!/usr/bin/env python
# coding: utf-8

# In[6]:


from textblob import TextBlob
from flask import Flask
from flask import render_template, request


# In[7]:


app = Flask(__name__)


# In[8]:


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form.get("text")
        print(text)
        r = TextBlob(text).sentiment
        return(render_template("index.html", result=r))
    else:
        return(render_template("index.html", result="waiting..."))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:





# In[ ]:





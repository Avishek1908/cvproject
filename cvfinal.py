# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from rake_nltk import Rake
import pke
import random 
import tkinter

from tkinter import *
 

datasets=pd.read_csv('cvforms.csv')
Question2=pd.read_csv('QandA.csv')
#Results2=pd.DataFrame(columns=('questions','answers'))
datsets2= datasets['School Name']
#dataCV=datasets[['CGPA', 'Years of experience', 'Number of paper publications','Internships', 'Skills', 'Number of projects','Completed certified courses']]
datasets.columns
dataCV1=datasets.loc[:,'CGPA':'Adhaar']
dataCV1.drop('Fresher/ Experienced',axis=1,inplace=True)
dataCV1.drop('Email Address',axis=1,inplace=True)
#dataCV1.loc[dataCV1.column_name condition, 'new column name'] = 'value if condition is met'
dataCV1['Internships']=dataCV1.Internships.map({'<=2':'0.4','2-4':'0.8','4-6':'1.2','6-8':'1.6','> 8':'2.0'})
dataCV1.rename(columns = {'Years of experience': 'experience'}, inplace = True) 
dataCV1.rename(columns = {'Number of projects ': 'projects'}, inplace = True) 
dataCV1.rename(columns = {'Number of paper publications ': 'publications'}, inplace = True) 
datasetCVX=dataCV1['experience']
dataCV1['experience']=dataCV1.experience.map({'<=2 years':'1.0','2-4 years':'2.0','4-6 years':'3.0','> 8 years':'4.0'})
dataCV1['experience'].fillna(0.0,inplace=True)
dataCV1['publications']=dataCV1.publications.map({'<=2':'0.2','2-4':'0.4','4-6':'0.6','6-8':'0.8','> 8':'1.0'})
dataCV1['projects']=dataCV1.projects.map({'<=2':'0.2','2-4':'0.4','4-6':'0.6','6-8':'0.8','> 8':'1.0'})
dataCV1.rename(columns = {'Completed certified courses ': 'courses'}, inplace = True)
dataCV1['courses']=dataCV1.courses.map({'<=2':'0.1','2-4':'0.2','4-6':'0.3','6-8':'0.4','> 8':'0.5'})
dataCV1.columns



dataCV1['CGPA'] = dataCV1['CGPA'].astype(np.float32)
dataCV1['experience'] = dataCV1['experience'].astype(np.float32)
dataCV1['publications'] = dataCV1['publications'].astype(np.float32)
dataCV1['courses'] = dataCV1['courses'].astype(np.float32)
dataCV1['Internships'] = dataCV1['Internships'].astype(np.float32)
dataCV1['projects'] = dataCV1['projects'].astype(np.float32)

col=dataCV1.sum(axis = 1)
df=pd.DataFrame(data=col.values,columns=['total'])
#col.rename(columns={0:'Total'}, inplace=True)
#dataCV1.drop('Skills',axis=1,inplace=True)
#df.drop('c',axis=1,inplace=True)
df['result']=np.where(df['total']<12,'false','true')

    #x_derived.append(t)
    
#y = pd.DataFrame(x_derived)     
r = Rake()
#r.extract_keywords_from_text("DOM stands for Document Object Model and is responsible for how various objects in a document interact with each other. DOM is required for developing web pages, which includes objects like paragraph, links, etc. These objects can be operated to include actions like add or delete. DOM is also required to add extra capabilities to a web page. On top of that, the use of API gives an advantage over other existing models.")
#r.get_ranked_phrases()

x= Question2.iloc[:,1].values
x = list(x)
x_derived = []
for s in list(x):
        r.extract_keywords_from_text(str(s))
        t = r.get_ranked_phrases()
        #print(s, t)
        x_derived.append(','.join(t))         
        
column_values = pd.Series(x_derived)
col_val = str(column_values)
Question2.insert(loc=0, column="keywordsFinal", value=column_values)        
        

ques= ""
ans = ""
inp= "" 
"""
"""
#tkinter
#export dataframe to csv
#def exx(window):
 #   window.destroy()
    
    
    
def submit():
    
    '''runs the submit button'''#next chosen question
       #print(s, t)

    
    #Question2.drop('keywordssssssssssss',axis=1,inplace=True)
    #y
    #z= pd.concat([Question2,column_values],axis=1, join="inner")
    #z
    #export_csv = y.to_csv(r'C:\Users\91812\Desktop\Machine Leaning course\QandA.csv', columns=, header=True)
    """dataCV1['Skills'].values.tolist()
    dataCV1.dtypes
    h=dataCV1.Skills[0]
    h
    g = h.split(',', 10)
    g[0]"""
    
    #p = Question2[Question2['Skills'].str.match('Scri')]
    #p.where(Question2.values==dataCV1.values)
    #outputted first question under scripting skill
    #ques = p.Questions[0]
    
    #taken input 
    inp = answer.get()
    blah.set(str(inp))
    
    r.extract_keywords_from_text(inp)
    temp = r.get_ranked_phrases()
    temp #extracted the keywords into a list
        
    #Results2 = Results2.set_value(len(Results2), 'questions', new)
    #Results2=Results2.set_value(len(Results2), 'answers', inp)
    

    
    
    
    
    
    
    """tempstring = (','.join(temp)) 
    tempstring#extracted keywords into a string
    
    #temp2 = tempstring.split(",") #stores keywords of users answer.
    #temp2
    #q = Question2['keywordsFinal'].str.contains(temp2[1])
    #temp2[1]
    
    keywordlist = Question2['keywordsFinal']
    keywordlist = pd.DataFrame(keywordlist)
    #keywordlist.loc['keywordsFinal']
    
     aaku=keywordlist.at[1,'keywordsFinal'].split(",")
     aaku[1]
     aaku
    
    quesdf = Question2.loc[:, 'Questions']#dataframe of only questions column 
     
    """
    count2=[]
    j=0
    k = ""
    type(count2)
    # count= []
    for rows in Question2['Questions']:
      #  print(rows)
        # break
         count= 0
         for i in temp:
             k=i
             if(k in str(rows)):
                 #print(rows)
                 count = count +1
         count2.append(count)        
                 
     
                 
                 
                 
                
                 
         
                 
        
    c = max(count2)
    c   
       
    #i =  random.choice() 
    
    indextomap = count2.index(c)
    indextomap
    
    ques = Question2.loc[indextomap, 'Questions']
    blah.set(str(ques))
    new.set(ques)
    
    if (c == 0):
        v = Question2['Questions']
        ques=random.choice(v) 
    
    
    #Results2 = Results2.set_value(len(Results2), 'questions', new)
    #Results2=Results2.set_value(len(Results2), 'answers', inp)    
    
   
        
        
    
window =tkinter.Tk()
window.title("CV")

window.configure(background ="#ffd600")


Label(window).grid(row = 0,columnspan = 6)
Label(window,text = "Question : ",bg ="#ffd600",justify=LEFT).grid(row = 1,column = 0)
Label(window,text = "Type answer here: ",bg = "#ffd600",justify=LEFT).grid(row = 3, column = 0)
scoreLabel =Label(window,bg = "#ffd600")
scoretxt = Label(window,text ="Your score is: ?",bg = "#ffd600")
scoreLabel.grid(row=5,column = 2)
scoretxt.grid(row = 6,column = 2)
p = Question2[Question2['Skills'].str.match('Scri')]
ques = p.Questions[0]
new = StringVar()
new.set(ques)
question=Label(window,bg = "white",textvariable = new,justify=LEFT)
question.grid(row =1,column=1)

#Label(window,textvariable = new ,bg = "#ffd600",justify=LEFT).grid(row = 4, column = 0)


blah = StringVar()

answer = Entry(window,bg ="white",width = 30)
answer.grid(row = 6,column=1)

# make a submit button

Button(window,text= "Submit",bg = "white",command = submit).grid(row = 3,column = 2)
#Button(window,text= "Exit",bg = "white",command = exx).grid(row = 4,column = 2)


mainloop()

#end


















   
        
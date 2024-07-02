from flask import Flask as fk,render_template,abort,Response,request,redirect,url_for
import requests

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import urllib.request as ur
from dotenv import load_dotenv as dot
import os
def secure():
  dot()
link=os.getenv('url') 
api_key=os.getenv('api_key')
city=os.getenv('city')


client = MongoClient(link, server_api=ServerApi('1'))
mydb = client["todolist"]
mycol = mydb["do"]
app = fk(__name__)
def get_weather():
    try:
     url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    
     response = requests.get(url)
     return response.json()
    except:
       print('error occurred')
       return f'error occurred, check the api key'
def insert_database():
    task=''
    detail=''
    if request.method=='POST':
        task=request.form.get('task')
        detail=request.form.get('detail')
    if(task=='')and(detail==''):
        exit 
    else:
     insert_data={'task':task,'detail':detail}    
     mycol.insert_one(insert_data)
    
def data_retrive():
    result=[]
    
    final_data=mycol.find({},{'_id':0})
    try:
     for x in final_data:
       result.append(x)
     print(result)
     return result
    except:
       return f'Error occurred'

    


@app.route('/',methods=['POST','GET'])
def start():
   
    weather=get_weather()
   
    insert_database()
    data=data_retrive()
    return render_template("main_page.html",weather=weather,data=data,len=len(data))

@app.route("/delete/<todo_detail>")
def delete(todo_detail):
    try:
     mycol.delete_one({"detail":todo_detail})
     return redirect('/')
    except Exception as e:
       print(e)
       return f'Error Occured'
    

    
    
    
 
  



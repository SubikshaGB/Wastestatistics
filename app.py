#import dash
#from dash.dependencies import Output, Event
#import dash_core_components as dcc
#import dash_html_components as html
import plotly
import random
import plotly.express as px
from collections import deque
import mysql.connector
import pandas as pd
from flask import *
import itertools
app=Flask(__name__)
@app.route('/get_data')
def get_data(y):
	conn =mysql.connector.connect(host='localhost',user='root',passwd='Alohomora123',db='WMS')
	cursor=conn.cursor()
	sql="select L.area_name,W.total_waste_generated from waste_details W,location L where W.area_code=L.area_code and W.g_year=%s"
	cursor.execute(sql,(y,))
	records=cursor.fetchall()
	print(records)
	df1=records
	df=pd.DataFrame([j for j in i] for i in df1)
	df.rename(columns={0:'Area name',1:'Total waste generated'},inplace=True)
	fig = px.pie(df, values='Total waste generated', names='Area name', title='Have an idea how much waste we generate?')
	fig.show()
@app.route('/',methods=['POST','GET'])
def main_data():
	if request.method=="POST":
		yar=request.form["yr"]
		print(yar)
		yar=str(yar)
		'''conn =mysql.connector.connect(host='localhost',user='root',passwd='Alohomora123',db='WMS')
		cursor=conn.cursor()
		sql="select L.area_name,W.total_waste_generated from waste_details W,location L where W.area_code=L.area_code and W.g_year=%s "
		cursor.execute(sql,(yar,))
		desc = cursor.description
		column_names = ['States','TW','Year']
		data = [dict(zip(column_names, row))  
        for row in cursor.fetchall()]
		print(data)
		maxtstate=max(data,key=data.get)
		maxtw=data[maxstate]
		print(maxtstate)'''
		get_data(yar)
	return render_template("index.html")
if __name__=="__main__":
	app.run()
  

from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
   tabla = pd.read_csv("db1.csv", sep=";")
   df_bios=pd.DataFrame(tabla)
   df_bios1=df_bios.head()
   df_html= df_bios1.to_html()
   return render_template("index.html", tablas=[df_html])
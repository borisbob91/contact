from interface.tkinker_import import *
import urllib.request, json
import requests

window = tkinter.Tk()

w = 500
h = 500

canvas = tk.Canvas(window, width=w, height=h)
canvas.pack()


class volley:
	def __init__(self):
		pass

url = 'https://api.covidtracking.com/v1/states/current.json'

with  urllib.request.urlopen(url) as url:
	data = json.loads(url.read().decode())
	#print(data)

file = requests.get(url)
print("*"*10)
print(file.json())



qs = ''' SELECT T1.Name
FROM <table1> T1 JOIN
     #TempSearch ts
     ON T1.Name LIKE CONCAT('%', Ts.Value, '%')
GROUP BY t1.Name
HAVING COUNT(*) = (SELECT COUNT(*) FROM #TempSearch); '''



if not None:



	pass

if None :


	pass
	if not None:
		
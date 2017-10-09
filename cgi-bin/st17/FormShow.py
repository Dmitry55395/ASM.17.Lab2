import cgi, pickle,cgitb,codecs,sys,datetime,os
def HeaderPrint():
    print("""Content-type:text/html\n
<html>
<head><title>Menu</title></head>
<body>
<h3>Menu</h3>""")

def ShowTable(l):
    print("""<table border="1">
     <caption>Dish</caption>
     <tr>
      <th>Name</th>
      <th>Price</th>
      <th>Grams</th>
      <th>Description</th>
      <th>Bonus</th>
      <th>Calories</th>
     </tr>""")
    l()
    print("</table>")

def ShowLink(q,selfurl):
    print("""<input type=hidden name=type value=0>
<a href="{0}?type=0&student={1}">Add Dish</a><br>
<a href="{0}?type=1&student={1}">Add Vip Dish</a><br>""".format(selfurl, q.getvalue("student")))

def FooterPrint():
    print("""</body>
</html>""")

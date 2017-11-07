<form action = "/cgi-bin/lab2.py">
<input type = "hidden" name = "student" value = {0}>
<input type = "hidden" name = "id" value = "{1}">
<input type = "hidden" name = "act" value = "save_reg">
<input type = "hidden" name = "obj" value = "2">
<b>Number:</b> <input type = "text" name = "number" value = {2}>
<b>Name: </b><input type = "text" name = "name" value = {3}>
<b>Surname: </b><input type = "text" name = "surname" value = {4}>
<input type = "submit" value = "Save">
</form>
<a href="?student={0}"><font color="orange" size="10">Back</font></a>
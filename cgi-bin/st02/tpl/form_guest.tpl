<form action = "/cgi-bin/lab2.py">
<input type = "hidden" name = "student" value = {0}>
<input type = "hidden" name = "id" value = "{1}">
<input type = "hidden" name = "act" value = "save_guest">
<input type = "hidden" name = "obj" value = "1">
<b>Name: </b><input type = "text" name = "name" value = {2}>
<b>Surname: </b><input type = "text" name = "surname" value = {3}>
<input type = "submit" value = "Save">
</form>
<a href="?student={0}"><font color="orange" size="10">Back</font></a>
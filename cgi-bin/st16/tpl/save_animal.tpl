<form action="/cgi-bin/lab2.py" align="center">
	<br>
	<table align="center" border=0>		
		<input type="hidden" name = "student" value={1} />
		<input type="hidden" name = "animal_id" value={2} />
		<input type="hidden" name = "is_parent" value={3} />
		<input type="hidden" name = "action" value="save_animal" />
		
		<a href="{0}?student={1}">Back to the menu</a><br>
		<tr>
			<td>
				Nickname:
			</td>
			<td>
				<input value = "{4}" type="text" name="nickname"><br>
			</td>
		</tr>
		<tr>
			<td>
				Limbs count:
			</td>
			<td>
				<input value = "{5}" type="text" name="limbs_count"><br>
			</td>
		</tr>
		<br>
		<tr>
			<td colspan=2 align=center>
				<input value='Save' type="submit" style="width:100px">
			</td>
		</tr>		
	</table>
</form>
<br>
<tr>
	<td align="center" width=15>
		{1}
	</td>
	<td align="center" width=100>
		{2}
	</td>
	<td align="center" width=100>
		{3}
	</td>
	<td align="center" width=100>
		{4}
	</td>
	<td>
		<!-- <form action="/cgi-bin/lab2.py?student={0}&action=add_animal">
			<input type="submit" value="Edit" />
			<input type="hidden" name = "student" value={0} />
			<input type="hidden" name = "action" value="add_animal" />
		</form> -->
		<input type="button" value="Edit" onclick="window.location.href='?student={0}&animal_id={1}&action=show_edit'" />
		<input type="button" value="Delete" onclick="window.location.href='?student={0}&animal_id={1}&action=remove_animal'" />
	</td>

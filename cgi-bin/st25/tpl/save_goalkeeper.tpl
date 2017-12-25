<form action="/cgi-bin/lab2.py" align="center">
	<br>
	<table align="center" border=0>		
		<input type="hidden" name = "student" value={1} />
		<input type="hidden" name = "player_id" value={2} />
		<input type="hidden" name = "is_parent" value={3} />
		<input type="hidden" name = "action" value="save_player" />
		
		<a href="{0}?student={1}">Back to the menu</a><br>
		<tr>
			<td>
				Playername:
			</td>
			<td>
				<input value = "{4}" type="text" name="playername"><br>
			</td>
		</tr>
		<tr>
			<td>
				Raiting:
			</td>
			<td>
				<input value = "{5}" type="text" name="raiting"><br>
			</td>
		</tr>
		<tr>
			<td>
				Reaction:
			</td>
			<td>
				<input value = "{6}" type="text" name="reaction"><br>
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
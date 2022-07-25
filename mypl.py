import vihar as vh

vh = vh.ViHar()

end = ''

while True:
	a = input('ViHar V0 : ')
	if a == 'exec':
		end = end.split('!>=<!')
		for cmd in end:
			vh.compile(vh.sorting(cmd))
		end = ''
	else:
		end += f'{a}'
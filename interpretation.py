import vihar as vh

vh = vh.ViHar()

end = ''

while True:
	a = input('ViHar V1 : ')
	if a == 'vhe':
		end = end.split('!=!')
		vh.compile(end)
		end = ''
	else:
		end += a

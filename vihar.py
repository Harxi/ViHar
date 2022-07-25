import os
import sys

class ViHar(object):
	def __init__(self):
		self.memory = {}
		for x in range(0x1, 0x10065):
			self.memory[x] = None
		self.commands = {
			'0': 'exit()',
			'1': 'self.restart()',
			'2': 'self.send',
			'3': 'self.move'
		}
	
	def bite(self, text):
		return len(text.encode('utf-8'))
	
	def sorting(self, commands):
		return commands.split(' ')
		
	def restart(self):
		os.execv(sys.executable, ['python'] + sys.argv)
	def move(self, position, data, mode='2'):
		try:
			self.memory[int(position)]
		except:
			print(f'Position {position} is not defined')
		else:
			position = int(position)
			if mode == '1':
				self.memory[position] = self.memory[int(data)]
			elif mode == '2':
				if self.bite(data) > 0x10065//2:
					print('Memory limit exceeded')
				else:
					self.memory[position] = data

	def send(self, position):
		print(str(self.memory[int(position)]).replace('(/)SPACE(/)', ' '), end='')
	
	def compile(self, input: list):
		for indx, content in enumerate(input):
			content = content.split(':')
			if content[0] == '0':
				eval(self.commands['0'])
			elif content[0] == '1':
				eval(self.commands['1'])
			elif content[0] == '2':
				eval(f"{self.commands['2']}('{content[1]}')")
			elif content[0] == '3':
				eval(f"{self.commands['3']}('{content[1]}', '{content[2]}', '{content[3]}')")
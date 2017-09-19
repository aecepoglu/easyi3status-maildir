from os import path as osPath, listdir
from statusModule import EasyI3StatusModule

class Module(EasyI3StatusModule):
	def __init__(self, config):
		self.path = None
		self.label = (config['label'] + ' ') if 'label' in config else ''
		self.hideCount = config.get('hideCount', False)
		self.hideIfZero = config.get('hideIfZero', False)
		self.value = {
			'full_text': '✉',
			'name': 'maildir',
			'separator_block_width': 20
		}
		self.values = [self.value]

		if 'path' in config:
			dirPath = config['path']

			if osPath.exists(dirPath):
				self.path = dirPath
			else:
				self.err('ERR:bad_path')
		else:
			self.err('ERR:no_path')
	def update(self):
		if not self.path:
			return

		folderDir = osPath.join(self.path, 'new')

		count = len([
			name for name in listdir(folderDir)# if osPath.isfile(osPath.join(folderDir, name))
		])

		if count is 0 and self.hideIfZero:
			if len(self.values) > 0:
				self.values.clear()
		else:
			if len(self.values) == 0:
				self.values.append(self.value)

			tokens = [
				self.label,
				' ✉'
			]
			if not self.hideCount:
				tokens.insert(1, str(count))

			self.value['full_text'] = ' '.join(tokens)
			self.value['color'] = '#9090ff' if count > 0 else None
	def err(self, msg):
		self.value['full_text'] = msg
		self.value['color'] = '#ff0000'

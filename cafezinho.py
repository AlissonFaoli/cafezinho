class Cafezinho:

	def __init__(self, quantidade:float):
		if quantidade > 500.0:
			self.quantidade = 500.0
		else:
			self.quantidade = quantidade


	def __str__(self):
		return f'Quantidade de café na xícara: {self.quantidade}g'

	
	def __float__(self):
		return self.quantidade


	def tomar(self, goladas=1):
		if self.tem_cafe():
			self.quantidade -= 50*goladas
		return self.quantidade

	
	def tem_cafe(self):
		if self.quantidade > 0:
			return True
		return False

	
	def encher(self):
		if not self.tem_cafe():
			self.quantidade += 500.0
		else:
			self.quantidade += 500.0 - self.quantidade


cafezinho = Cafezinho(500)

while True:
	if cafezinho.tem_cafe():
		cafezinho.tomar()
	else:
		cafezinho.encher()
	print(cafezinho)

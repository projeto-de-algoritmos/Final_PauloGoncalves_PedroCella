# Classe para definir um novo trabalho a ser feito
class trabalho:
	
	def __init__(self, comeco:float ,final:float,prioridade=float, nome:str = None) -> None:
		"""
		nome:str
			Nome da tarefa que deve ser feita
		

		"""
		if nome == None:
			return ValueError

		self.nome = nome
		self.comeco = comeco
		self.final = final
		self.prioridade = prioridade
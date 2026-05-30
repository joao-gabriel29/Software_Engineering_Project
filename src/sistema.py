class Tarefa:
    def __init__(self, id_tarefa, titulo, descricao, prioridade):
        self.id = id_tarefa
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade  
        self.concluida = False

    def exibir(self):
        status = "Concluída" if self.concluida else "Pendente"
        emoji_prioridade = "1 " if self.prioridade == "Alta" else "2" if self.prioridade == "Média" else "3"
        print(f"ID: {self.id} | {emoji_prioridade} Prioridade: {self.prioridade:<5} | {self.titulo} - {self.descricao} [{status}]")


class GerenciadorTarefas:
    def __init__(self):
        self.lista_tarefas = []
        self.proximo_id = 1

    def criar_tarefa(self, titulo, descricao, prioridade):
        nova_tarefa = Tarefa(self.proximo_id, titulo, descricao, prioridade)
        self.lista_tarefas.append(nova_tarefa)
        self.proximo_id += 1
        print("\nTarefa criada com sucesso!")

    def listar_todas(self):
        if not self.lista_tarefas:
            print("\nNenhuma tarefa cadastrada.")
            return
        
        peso_prioridade = {"Alta": 1, "Média": 2, "Baixa": 3}
        
        tarefas_ordenadas = sorted(self.lista_tarefas, key=lambda t: peso_prioridade.get(t.prioridade, 2))

        print("\n--- TODAS AS TAREFAS (ORDENADAS POR PRIORIDADE) ---")
        for tarefa in tarefas_ordenadas:
            tarefa.exibir()

    def listar_concluidas(self):
        tarefas_concluidas = [t for t in self.lista_tarefas if t.concluida]
        
        if not tarefas_concluidas:
            print("\nNenhuma tarefa concluída até o momento.")
            return
        
        peso_prioridade = {"Alta": 1, "Média": 2, "Baixa": 3}
        tarefas_concluidas_ordenadas = sorted(tarefas_concluidas, key=lambda t: peso_prioridade.get(t.prioridade, 2))
        
        print("\n--- TAREFAS CONCLUÍDAS (ORDENADAS POR PRIORIDADE) ---")
        for tarefa in tarefas_concluidas_ordenadas:
            tarefa.exibir()

    def concluir_tarefa(self, id_tarefa):
        for tarefa in self.lista_tarefas:
            if tarefa.id == id_tarefa:
                if tarefa.concluida:
                    print("\n Esta tarefa já estava concluída!")
                else:
                    tarefa.concluida = True
                    print(f"\n Parabéns! Tarefa '{tarefa.titulo}' marcada como concluída, marcha no progresso.")
                return
        print("\nTarefa não encontrada, ta chapando?")

    def deletar_tarefa(self, id_tarefa):
        for tarefa in self.lista_tarefas:
            if tarefa.id == id_tarefa:
                self.lista_tarefas.remove(tarefa)
                print(f"\n Tarefa '{tarefa.titulo}' excluída com sucesso e não falamos mais disso...")
                return
        print("\nTarefa não encontrada.")


def menu():
    gerenciador = GerenciadorTarefas()

    while True:
        print("\n==============================")
        print("    TECHFLOW TASK MANAGER     ")
        print("==============================")
        print("1. Criar Nova Tarefa (Create)")
        print("2. Listar Todas as Tarefas (Read - Por Prioridade)")
        print("3. Ver Apenas Tarefas Concluídas")
        print("4. Concluir uma Tarefa (Update)")
        print("5. Excluir uma Tarefa (Delete)")
        print("6. Sair do Sistema")
        
        opcao = input("\nEscolha uma opção (1-6): ")

        if opcao == "1":
            titulo = input("Digite o título da tarefa: ")
            descricao = input("Digite a descrição da tarefa: ")
            
            print("\nSelecione o grau de prioridade:")
            print("1. Alta")
            print("2. Média")
            print("3. Baixa")
            p_opcao = input("Escolha (1-3): ")
            prioridade = "Alta" if p_opcao == "1" else "Baixa" if p_opcao == "3" else "Média"
            
            gerenciador.criar_tarefa(titulo, descricao, prioridade)
            
        elif opcao == "2":
            gerenciador.listar_todas()
            
        elif opcao == "3":
            gerenciador.listar_concluidas()
            
        elif opcao == "4":
            gerenciador.listar_todas()
            try:
                id_atualizar = int(input("\nDigite o ID da tarefa que deseja concluir: "))
                gerenciador.concluir_tarefa(id_atualizar)
            except ValueError:
                print("\n Por favor, digite um número válido para o ID, cabeção.")
                
        elif opcao == "5":
            gerenciador.listar_todas()
            try:
                id_deletar = int(input("\nDigite o ID da tarefa que deseja excluir: "))
                gerenciador.deletar_tarefa(id_deletar)
            except ValueError:
                print("\n Por favor, digite um número válido para o ID.")
                
        elif opcao == "6":
            print("\nFechando o sistema. Chega de trabalhar, irmão, não aguento mais essa miséria.")
            break
        else:
            print("\n Opção inválida! Escolha um número de 1 a 6.")

if __name__ == "__main__":
    menu()

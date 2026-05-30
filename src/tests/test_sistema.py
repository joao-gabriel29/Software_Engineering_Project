from src.sistema import GerenciadorTarefas

def test_criar_tarefa_com_sucesso():
    gerenciador = GerenciadorTarefas()
    gerenciador.criar_tarefa("Testar Sistema", "Garantir o funcionamento")

    assert len(gerenciador.lista_tarefas) == 1
    assert gerenciador.lista_tarefas[0].titulo == "Testar Sistema"

def adicionar_produtos(produtos):
    nome = input("Digite qual produto você deseja adicionar: ")
    quantidade = int(input("Digite a quantidade do produto que você deseja adicionar: "))
    valor = float(input("Digite o valor do produto: "))
    total_produto = valor * quantidade

    produto = {"nome": nome, "quantidade": quantidade, "valor": valor, 'total_produto': total_produto}
    produtos.append(produto)
    print("Produto adicionado com sucesso!")


def visualizar_produtos(produtos):
    if not produtos:
        print("Não existem nenhum produto.")
    else:
        for produto in produtos:
            print(f"Produto: {produto['nome']}, Quantidade: {produto['quantidade']}, Valor unitário: {produto['valor']}, Total: {produto['total_produto']}")

        valor_total = sum(produto['total_produto'] for produto in produtos)
        print(f"Valor total: {valor_total}")

def atualizar_produto(produtos):
    if not produtos:
        print("Não existem nenhum produto.")
    else:
        visualizar_produtos(produtos)
        num_produto = int(input("Digite o número do produto a ser atualizado: "))
        num_produto -= 1
        if 0 <= num_produto < len(produtos):
            novo_nome = input("Digite o novo nome do produto a ser atualizado: ")
            produtos[num_produto]["nome"] = novo_nome
            nova_quantidade = int(input("Digite a quantidade nova do produto a ser atualizado: "))
            produtos[num_produto]['quantidade'] = nova_quantidade
            novo_valor = float(input("Digite a valor nova do produto a ser atualizado: "))
            produtos[num_produto]['valor'] = novo_valor
            produtos['total'] = produtos['quantidade'] * produtos['valor_unitario']

            print("Produto atualizado.")

def remover_produto(produtos, produto):
    visualizar_produtos(produtos)
    nome_produto = input('Digite o nome do produto a ser removido: ')
    if produto in produtos:
        if produto['nome'] == nome_produto:
            produtos.remove(produto)
            print("Produto removido com sucesso.")
            return
        print("Produto não encontrado.")


def calcular_valor_total(produtos, valor_somado=0):
    valor_somado = sum(produto['total_produto'] for produto in produtos)
    print (valor_somado)



def menu():
    produtos = []

    while True:
        print("\nMenu:")
        print("1. Adicionar produto")
        print("2. Listar produtos")
        print("3. Remover produto")
        print("4. Atualizar produto")
        print("5. Soma total")
        print("6. Sair")

        opcao = int(input("Digite a opção que você deseja: "))

        if opcao == 1:
            adicionar_produtos(produtos)
        elif opcao == 2:
            visualizar_produtos(produtos)
        elif opcao == 3:
            remover_produto(produtos)
        elif opcao == 4:
            atualizar_produto(produtos)
        elif opcao == 5:
            calcular_valor_total(produtos)
        elif opcao == 6:
            print("Saindo...")
            break
        else:
            print("Opção inválida.")


menu()

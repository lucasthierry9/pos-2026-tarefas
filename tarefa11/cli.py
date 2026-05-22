import users_wrapper as u

while True:
    print("1 - Listar usuários")
    print("2 - Detalhar usuário") 
    print("3 - Criar usuário")
    print("4 - Editar usuário") 
    print("5 - Deletar usuário")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("Lista de usuários:")
        users = u.list()
        if users:
            for user in users:
                print(f"ID: {user['id']}, Nome: {user['name']}")
        else:
            print("Nenhum usuário encontrado.")
    
    if opcao == "2":
        user_id = input("Digite o ID do usuário: ")
        user = u.read(user_id)
        if user:
            print(f"Nome: {user['name']}")
            print(f"Email: {user['email']}")
            print(f"Telefone: {user['phone']}")
        else:
            print("Usuário não encontrado.")

    if opcao == "3":
        print("Digite os dados do novo usuário:")
        user = {}
        user["name"] = input("Nome: ")
        user["email"] = input("Email: ")
        user["phone"] = input("Telefone: ")
        criar = u.create(user)
        if criar:
            print("Usuário criado com sucesso.")
        else:
            print("Erro ao criar usuário.")
    
    if opcao == "4":
        user_id = input("Digite o ID do usuário: ")
        user = u.read(user_id)
        if user:
            print(f"Nome: {user['name']}")
            print(f"Email: {user['email']}")
            print(f"Telefone: {user['phone']}")
            user["name"] = input("Digite o novo nome do usuário: ")
            user["email"] = input("Digite o novo email do usuário: ")
            user["phone"] = input("Digite o novo telefone do usuário: ")
            editar = u.update(user_id, user)
            if editar:
                print("Usuário atualizado com sucesso.")
            else:
                print("Erro ao atualizar usuário.")
    
    if opcao == "5":
        user_id = input("Digite o ID do usuário: ")
        user = u.read(user_id)
        if user:
            print(f"Nome: {user['name']}")
            print(f"Email: {user['email']}")
            print(f"Telefone: {user['phone']}")
            exclusao = u.delete(user_id)
            if exclusao:
                print("Usuário excluído com sucesso.")
            else:
                print("Erro ao excluir usuário.")

    if opcao == "6":
        break
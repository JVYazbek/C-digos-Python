class Usuario:
    def __init__(self, ra, nome):
        self.ra = ra
        self.nome = nome
        self.livros_emprestados = []

    def emprestar_livro(self, livro):
        self.livros_emprestados.append(livro)

    def devolver_livro(self, livro):
        if livro in self.livros_emprestados:
            self.livros_emprestados.remove(livro)
            return True
        return False

    def listar_livros(self):
        if not self.livros_emprestados:
            print(f"O usuário {self.nome} não possui livros emprestados.")
        else:
            print(f"Livros com {self.nome}:")
            for livro in self.livros_emprestados:
                print(f"- {livro.titulo}")

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            return True
        return False

    def devolver(self):
        self.disponivel = True

    def __str__(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"Título: {self.titulo} | Autor: {self.autor} | Status: {status}"

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []

    def cadastrar_livro(self, livro):
        if any(l.titulo.lower() == livro.titulo.lower() for l in self.livros):
            print("Erro: Já existe um livro cadastrado com este título.")
            return False
        self.livros.append(livro)
        print("Livro cadastrado com sucesso!")
        return True

    def cadastrar_usuario(self, usuario):
        if any(u.ra == usuario.ra for u in self.usuarios):
            print("Erro: Já existe um usuário cadastrado com este RA.")
            return False
        self.usuarios.append(usuario)
        print("Usuário cadastrado com sucesso!")
        return True

    def realizar_emprestimo(self, ra, titulo_livro):
        usuario = next((u for u in self.usuarios if u.ra == ra), None)
        livro = next((l for l in self.livros if l.titulo.lower() == titulo_livro.lower()), None)

        if not usuario:
            print("Erro: Usuário não encontrado.")
        elif not livro:
            print("Erro: Livro não encontrado.")
        elif not livro.disponivel:
            print("Erro: Este livro já está emprestado.")
        else:
            livro.emprestar()
            usuario.emprestar_livro(livro)
            print(f"Empréstimo de '{livro.titulo}' realizado para {usuario.nome}!")

    def realizar_devolucao(self, ra, titulo_livro):
        usuario = next((u for u in self.usuarios if u.ra == ra), None)
        if not usuario:
            print("Erro: Usuário não encontrado.")
            return

        livro = next((l for l in usuario.livros_emprestados if l.titulo.lower() == titulo_livro.lower()), None)
        
        if livro:
            livro.devolver()
            usuario.devolver_livro(livro)
            print(f"Devolução de '{livro.titulo}' realizada com sucesso!")
        else:
            print("Erro: Este usuário não possui este livro para devolver.")

    def listar_livros_disponiveis(self):
        disponiveis = [l for l in self.livros if l.disponivel]
        if not disponiveis:
            print("Não há livros disponíveis no momento.")
        else:
            print("\n--- Livros Disponíveis ---")
            for l in disponiveis:
                print(l)

    def listar_livros_emprestados_usuario(self, ra):
        usuario = next((u for u in self.usuarios if u.ra == ra), None)
        if usuario:
            usuario.listar_livros()
        else:
            print("Erro: Usuário não encontrado.")

# --- Menu de Interação ---
def menu():
    biblioteca = Biblioteca()
    
    while True:
        print("1. Cadastrar um livro")
        print("2. Cadastrar um novo usuário")
        print("3. Realizar um empréstimo")
        print("4. Realizar uma devolução")
        print("5. Listar livros disponíveis")
        print("6. Listar livros emprestados ao usuário")
        print("7. Finalizar")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            titulo = input("Título do livro: ")
            autor = input("Autor do livro: ")
            biblioteca.cadastrar_livro(Livro(titulo, autor))
        
        elif opcao == '2':
            ra = input("RA do usuário: ")
            nome = input("Nome do usuário: ")
            biblioteca.cadastrar_usuario(Usuario(ra, nome))
            
        elif opcao == '3':
            ra = input("RA do usuário: ")
            titulo = input("Título do livro: ")
            biblioteca.realizar_emprestimo(ra, titulo)
            
        elif opcao == '4':
            ra = input("RA do usuário: ")
            titulo = input("Título do livro: ")
            biblioteca.realizar_devolucao(ra, titulo)
            
        elif opcao == '5':
            biblioteca.listar_livros_disponiveis()
            
        elif opcao == '6':
            ra = input("RA do usuário: ")
            biblioteca.listar_livros_emprestados_usuario(ra)
            
        elif opcao == '7':
            print("Sistema encerrado.")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
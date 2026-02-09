# função callback
def cumprimentar(nome):
    print("Olá, " + nome)


def processarUsuario(callback):
    nome = "João"
    callback(nome) # Executa o callback

processarUsuario(cumprimentar)

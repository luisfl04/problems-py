class Lista:
    def __init__(self, value = 0, next = None):
        self.next = next
        self.value = value

def addTwonumbers(l1, l2):
    cabecalho_ficticio = Lista()
    atual = cabecalho_ficticio
    carregamento = 0

    while l1 or l2 or carregamento:
        x = l1.value if l1 else 0
        y = l2.value if l2 else 0 

        soma_total = x + y + carregamento
        carregamento = soma_total // 10

        atual.next = Lista(soma_total % 10)
        atual = atual.next
    
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return cabecalho_ficticio.next


l1 = Lista(3, Lista(1, Lista(3)))
l2 = Lista(4, Lista(9, Lista(1)))

resultado = addTwonumbers(l1, l2)

while resultado:
    print(resultado.value)
    resultado = resultado.next
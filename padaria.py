# padaria.py

def main():
    print("Registro de pedido - Padaria")
    nome_cliente = input("Digite o nome do cliente: ")
    nome_produto = input("Digite o nome do produto: ")
    
    try:
        preco = float(input("Digite o preço do produto: R$ "))
        quantidade = int(input("Digite a quantidade: "))
    except ValueError:
        print("Erro: preço deve ser número e quantidade deve ser inteiro.")
        return
    
    total = preco * quantidade
    
    print("\n=== Resumo do Pedido ===")
    print(f"Cliente: {nome_cliente}")
    print(f"Produto: {nome_produto}")
    print(f"Preço unitário: R$ {preco:.2f}")
    print(f"Quantidade: {quantidade}")
    print(f"Total a pagar: R$ {total:.2f}")

if __name__ == "__main__":
    main()

preco_hamburguer = 25.00
preco_batata = 15.00
preco_refrigerante = 8.00

print("=== CARDÁPIO ===")
print(f"Hambúrguer: R$ {preco_hamburguer:.2f}")
print(f"Batata frita: R$ {preco_batata:.2f}")
print(f"Refrigerante: R$ {preco_refrigerante:.2f}")

quantidade_hamburguer = int(input("\nQuantos hambúrgueres você deseja? "))
quantidade_batata = int(input("Quantas batatas fritas você deseja? "))
quantidade_refrigerante = int(input("Quantos refrigerantes você deseja? "))

subtotal_hamburguer = preco_hamburguer * quantidade_hamburguer
subtotal_batata = preco_batata * quantidade_batata
subtotal_refrigerante = preco_refrigerante * quantidade_refrigerante

subtotal = (
    subtotal_hamburguer
    + subtotal_batata
    + subtotal_refrigerante
)

taxa_servico = subtotal * 0.10
total = subtotal
total += taxa_servico

pessoas = int(input("\nEm quantas pessoas a conta será dividida? "))

desconto = 0.00

if pessoas > 4:
    desconto = total * 0.05
    total -= desconto

resposta_gorjeta = input(
    "Deseja deixar uma gorjeta extra? Digite sim ou não: "
).strip().lower()

quer_gorjeta = resposta_gorjeta == "sim"
gorjeta_extra = 0.00

if quer_gorjeta:
    gorjeta_extra = float(input("Digite o valor da gorjeta extra: R$ "))
    total += gorjeta_extra

valor_por_pessoa = total / pessoas

print("\n=== RESUMO DA CONTA ===")
print(f"Hambúrgueres: R$ {subtotal_hamburguer:.2f}")
print(f"Batatas fritas: R$ {subtotal_batata:.2f}")
print(f"Refrigerantes: R$ {subtotal_refrigerante:.2f}")
print(f"Subtotal: R$ {subtotal:.2f}")
print(f"Taxa de serviço (10%): R$ {taxa_servico:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Gorjeta extra: R$ {gorjeta_extra:.2f}")
print(f"Total da conta: R$ {total:.2f}")
print(f"Valor por pessoa: R$ {valor_por_pessoa:.2f}")

if total > 200:
    print("Atenção: o total da conta ultrapassou R$ 200,00.")
else:
    print("O total da conta não ultrapassou R$ 200,00.")

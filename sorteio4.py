import flet as ft
import random
def app(page: ft.Page):
    lista_nomes = []
    nome = ft.TextField(label="Digite os nomes que serão sorteados")

    def tecla(t: ft.KeyboardEvent):
        page.add(
            ft.Text(f"Tecla pressionada: {i.key}")
        )

    def adicionar(a):
        lista_nomes.append(nome.value)

        for posicao, nome_adicionado in enumerate(lista_nomes, start=1):
            saida = (f"{posicao}° {nome_adicionado.upper()}")
            # print(f"{posicao}° {nome_adicionado}")

        page.scroll = 'always'
        page.add(
            ft.Text(saida)
        )
        nome.value = ''
        page.update()
        # print(lista_nomes)


    def sorteio(e):
        if lista_nomes:
            escolhido = random.choice(lista_nomes)

            page.add(
                ft.Text(f"O sorteado é {escolhido.upper()}"),

            )

            page.update()

            # print(escolhido)
        else:
            page.add(
                ft.Text("Não há nada para ser sorteado")
            )



    # Adicionando botoes na page
    page.add(
        nome,
        ft.ElevatedButton("Adicionar", on_click=adicionar),
        ft.ElevatedButton("Sortear", on_click=sorteio)

    )

ft.app(target=app)
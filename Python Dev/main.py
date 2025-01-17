import flet as ft

def main(pagina):
    titulo = ft.Text("Hashzap")

    chat = ft.Column()

    def msg_tunel(mensagem):
        texto = ft.Text(mensagem)
        chat.controls.append(texto)
        pagina.update()

    pagina.pubsub.subscribe(msg_tunel)


    def enviar_msg(evento):
        nome_usuario = nome.value
        txt_campo_mensagem = c_enviarmensagem.value
        mensagem = f"{nome_usuario}: {txt_campo_mensagem}"
        pagina.pubsub.send_all(mensagem)
        c_enviarmensagem.value = ""
        pagina.update()

    c_enviarmensagem = ft.TextField(label="Digite sua mensagem aqui")
    b_enviar = ft.FilledButton("Enviar", on_click=enviar_msg)
    linha_enviar = ft.Row([c_enviarmensagem, b_enviar])

    
    def entrar_chat(evento):
        popup.open = False
        pagina.remove(titulo, button)
        pagina.add(chat)
        pagina.add(linha_enviar)
        
        nome_usuario = nome.value
        mensagem = f"{nome_usuario}: Entrou no chat"
        pagina.pubsub.send_all(mensagem)
        pagina.update()
    
    titulo_popup = ft.Text("Bem vindo ao Hashzap")
    nome = ft.TextField()
    botton_popup = ft.FilledButton("Entrar no chat", on_click=entrar_chat)
    popup = ft.AlertDialog(title=titulo_popup, content=nome, actions=[botton_popup])

    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    button = ft.FilledButton("Iniciar Chat", on_click=abrir_popup)

    pagina.add(titulo)
    pagina.add(button)

ft.app(main, view=ft.WEB_BROWSER, port=7777) # Usado para executar a função com o flet
import chainlit as cl
import requests

MAKE_WEBHOOK_URL = "https://hook.us2.make.com/mn8gnb5ov1ehe1iwygyx1jphavkfxlb9"

@cl.on_chat_start
async def start():
    await cl.Message(
        content="Saludos, Señor. Soy Trinity. Sistema en línea. ¿Qué instrucciones tiene para la agenda de hoy?"
    ).send()

@cl.on_message
async def main(message: cl.Message):
    msg = cl.Message(content="")
    await msg.send()

    try:
        response = requests.post(
            MAKE_WEBHOOK_URL, 
            json={"message": message.content, "user": "Señor"},
            timeout=30
        )

        if response.status_code == 200:
            try:
                 data = response.json()
                 reply_text = data.get("response", "Operación procesada con éxito, Señor.")
            except ValueError:
                 reply_text = response.text if response.text else "Entendido, Señor."
        else:
            reply_text = f"Disculpe, Señor, el servidor respondió con el código {response.status_code}."
    except Exception as e:
        reply_text = f"Error de conexión: {str(e)}"

    msg.content = reply_text
    await msg.update()

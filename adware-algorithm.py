import webbrowser
import time

# Fica em loop para exibir anúncios indesejados
while True:
    # Abre um anúncio em uma nova aba do navegador
    webbrowser.open_new_tab("http://site-de-anuncio.com")

    # Dorme por 10 minutos antes de exibir o próximo anúncio
    time.sleep(600)

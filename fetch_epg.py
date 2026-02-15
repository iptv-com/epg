import requests
import gzip

def baixar_e_salvar():
    # Fonte de dados de EPG para o Brasil (padrão XMLTV)
    url_fonte = "https://iptv-org.github.io/epg/guides/br.xml"
    
    print("Iniciando a captura da grade de programação (Brasil)...")
    
    try:
        response = requests.get(url_fonte, timeout=30)
        if response.status_code == 200:
            # Garante que a pasta existe e salva o guia
            import os
            if not os.path.exists('guides'):
                os.makedirs('guides')
                
            with open("guides/brazil.xml", "w", encoding="utf-8") as f:
                f.write(response.text)
            print("Guia brazil.xml gerado com sucesso!")
        else:
            print(f"Erro na fonte: {response.status_code}")
    except Exception as e:
        print(f"Falha na automação: {e}")

if __name__ == "__main__":
    baixar_e_salvar()

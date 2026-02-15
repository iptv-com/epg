# 📅 IPTV-com EPG (Guia de Programação)

> O cérebro por trás da sua TV. Este repositório fornece o guia de programação (XMLTV) atualizado automaticamente para os canais brasileiros do projeto **IPTV-com**.

---

### 🔗 Link Direto (EPG)
Utilize o link abaixo no seu player favorito para carregar a grade de horários:

`https://raw.githubusercontent.com/iptv-com/epg/main/guides/brazil.xml`

---

### 🤖 Como funciona a Automação?
Este repositório é 100% autônomo. Não há intervenção humana aqui:

1.  **Sincronização:** Diariamente, às 00:30, nosso bot GitHub Action "acorda".
2.  **Coleta:** Ele busca as grades de programação mais recentes.
3.  **Processamento:** O arquivo `brazil.xml` é regenerado com as informações de horários, títulos e descrições dos programas.
4.  **Entrega:** O novo guia é publicado automaticamente no GitHub Pages.



---

### 🛠️ Como integrar à sua Lista M3U
Para que o seu player exiba a programação corretamente, sua lista deve começar com a tag `x-tvg-url` apontando para este repositório:

```m3u
#EXTM3U x-tvg-url="[https://raw.githubusercontent.com/iptv-com/epg/main/guides/brazil.xml](https://raw.githubusercontent.com/iptv-com/epg/main/guides/brazil.xml)"

#EXTINF:-1 tvg-id="TVBrasil.br", TV Brasil
http://link-do-canal.m3u8

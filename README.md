<h1 align="center"> 
    <p>Web Scraping IMDB</p>
</h1>

## 📚Sobre
Este repositório oferece um básico código de Web Scraping que eu aprendi a fazer vendo um vídeo no Youtube. Ele é simples mas me deu uma base muito boa em Web Scraping que é uma área muito interessante, e, obviamente, o código pode mutar-se para ser usado em outras realidades que forem necessárias.

## 💻Funcionalidades
O código implementa um sistema para a captura e depuração de dados. Os dados são dos 25 melhores filmes do IMDB, o código faz solicitações ao site e o mesmo responde com as informações relevantes para o sistema. A visualização destes dados pode ser feita entrando no documento <strong>"imdb.json"</strong>. As funcionalidades principais incluem:

- Visualização Formatada em json e csv
- O spider coleta as seguintes informações de cada filme:
    - **Titulos**: Nome do filme.
    - **Ano**: Ano de lançamento.
    - **Avaliacao**: Nota do filme no IMDb.
## Adicionais
Para evitar bloqueios, o spider inclui um `User-Agent` e `Referer` nos cabeçalhos da requisição para se parecer com um navegador comum. Isso ajuda a contornar restrições do site IMDb.

## 🔨Ferramentas

- [Python](https://www.python.org)
- [Scrapy](https://scrapy.org)

## 👨🏾‍🏫Requisitos de Pré-instalação

- Python 3.11.4
- Scrapy 2.11.2  

## 🏹Instalação

1. Clone este repositório:

```bash
    $ git clone https://github.com/natan3LiR/Web-Scraping-IMDB.git
```
2. Entre no diretório
```bash
    $ Web-Scraping-IMDB
```

[![pt-br](https://img.shields.io/badge/translate-EN-blue?style=for-the-badge&logo=googletranslate&logoColor=4285F4)](/README.md)

# Tudo Celular Scraper

Scraper de informações de celulares do site tudocelular.com, escrito em Python e que extrai dados marca, modelo, preço e salva em arquivos JSON.

## Como usar

1. Clone o repositório para a sua máquina local:

    ```bash
    git clone https://github.com/Ruy-Araujo/
    ```

2. Instale as dependências:

    ```bash
    cd tudo_celular
    pip install -r requirements.txt
    ```

3. Execute o scraper:

    ```bash
    scrapy crawl tudo_celular -o tudo_celular.json
    ```

O scraper irá extrair dados dos celulares disponiveis no site tudocelular.com e salvar em um arquivo JSON no diretório do projeto.

## Detalhes técnicos

O scraper usa o framework [Scrapy](https://scrapy.org/) para fazer o parsing do HTML da página de fichas tecnicas dos celulares e descrições, extrair informações como marca, modelo, ano de lançamento, etc.

Os dados brutos estão disponiveis [aqui](data/)

## Contribuindo

Se você quiser contribuir para este projeto, sinta-se à vontade para abrir uma issue ou enviar um pull request.

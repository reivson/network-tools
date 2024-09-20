# Network Tools

## Visão Geral
Este projeto é uma aplicação web baseada em Flask que fornece várias ferramentas de teste de rede através de uma interface HTTP simples. A aplicação oferece funcionalidades como ping, traceroute, telnet, verificação de endereço IP, consulta de variáveis de ambiente, consulta DNS e varredura de portas.

## Estrutura do Projeto
```
network-tools/
│
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── main.py
│   ├── requirements.txt
│   │
│   └── network_tests/
│       ├── __init__.py
│       ├── dns_utils.py
│       ├── envcheck.py
│       ├── ipaddr.py
│       ├── ping.py
│       ├── port_scanner.py
│       ├── routes.py
│       ├── telnet.py
│       └── traceroute.py
│
└── Dockerfile
```

## Requisitos
- Docker
- Python 3
- Flask 2.0.1
- Werkzeug 2.0.1

## Instalação e Execução

### Usando Docker
1. Clone o repositório:
   ```
   git clone https://github.com/reivson/network-tools.git
   cd network-tools
   ```

2. Construa a imagem Docker:
   ```
   docker build -t network-tools .
   ```

3. Execute o contêiner:
   ```
   docker run -p 80:80 network-tools
   ```

A aplicação estará disponível em `http://localhost:80`.

### Execução Local (sem Docker)
1. Clone o repositório:
   ```
   git clone https://github.com/reivson/network-tools.git
   cd network-tools/app
   ```

2. Crie e ative um ambiente virtual:
   ```
   python3 -m venv venv
   source venv/bin/activate  # No Windows use `venv\Scripts\activate`
   ```

3. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

4. Execute a aplicação:
   ```
   python -m app.main
   ```

A aplicação estará disponível em `http://localhost:80`.

## Funcionalidades e Uso

A aplicação oferece as seguintes funcionalidades:

### 1. DNS Lookup
- **Rota:** `/network/dns/<domain>`
- **Descrição:** Realiza uma consulta DNS para um domínio específico.
- **Exemplo:** `/network/dns/example.com`
- **Retorno:** JSON com o resultado da consulta DNS.

### 2. Verificação de Variáveis de Ambiente
- **Rotas:** 
  - `/network/env/<var_name>`: Verifica uma variável de ambiente específica.
  - `/network/env`: Lista todas as variáveis de ambiente.
- **Exemplo:** `/network/env/PATH`
- **Retorno:** JSON com o valor da variável de ambiente ou todas as variáveis.

### 3. Obtenção de Endereço IP
- **Rota:** `/network/ipaddr`
- **Descrição:** Retorna informações sobre os endereços IP do sistema.
- **Retorno:** Texto plano com as informações de IP.

### 4. Ping
- **Rota:** `/network/ping/<target>`
- **Descrição:** Realiza um ping para um alvo específico.
- **Exemplo:** `/network/ping/8.8.8.8`
- **Retorno:** Texto plano com o resultado do ping.

### 5. Varredura de Portas
- **Rota:** `/network/portscan/<host>`
- **Parâmetros de consulta:** `start` (porta inicial, padrão 1), `end` (porta final, padrão 1024)
- **Descrição:** Realiza uma varredura de portas em um host específico.
- **Exemplo:** `/network/portscan/example.com?start=80&end=100`
- **Retorno:** JSON com os resultados da varredura de portas.

### 6. Telnet
- **Rota:** `/network/telnet/<host>/<int:port>`
- **Descrição:** Tenta estabelecer uma conexão Telnet com um host e porta específicos.
- **Exemplo:** `/network/telnet/example.com/80`
- **Retorno:** Texto plano com o resultado da tentativa de conexão Telnet.

### 7. Traceroute
- **Rota:** `/network/traceroute/<target>`
- **Descrição:** Realiza um traceroute para um alvo específico.
- **Exemplo:** `/network/traceroute/example.com`
- **Retorno:** Texto plano com o resultado do traceroute.

## Configuração
A configuração da aplicação é gerenciada através da classe `Config` em `config.py`. Atualmente, apenas a `SECRET_KEY` está definida, que é obtida de uma variável de ambiente ou usa um valor padrão.

## Desenvolvimento
Para adicionar novas funcionalidades ou modificar as existentes, você pode editar os arquivos correspondentes no diretório `network_tests/`. O arquivo `routes.py` contém as definições das rotas Flask para cada funcionalidade.

### Adicionando uma Nova Funcionalidade
1. Crie um novo arquivo Python no diretório `network_tests/` para implementar a lógica da nova funcionalidade.
2. Adicione a rota correspondente no arquivo `routes.py`.
3. Importe a nova função no arquivo `routes.py` e use-a na definição da rota.

## Notas de Segurança
- Certifique-se de usar esta ferramenta apenas em redes e sistemas para os quais você tem permissão explícita para testar.
- A varredura de portas e outras funcionalidades podem ser consideradas maliciosas se usadas sem autorização.
- Considere implementar autenticação e autorização para restringir o acesso à aplicação em ambientes de produção.
- As funções de telnet e varredura de portas podem ser especialmente sensíveis e devem ser usadas com cautela.

## Contribuição
Para contribuir com o projeto:
1. Faça um fork do repositório
2. Crie uma nova branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Faça commit de suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## Licença
[Adicione informações sobre a licença do projeto aqui]

## Suporte
Para suporte, por favor abra uma issue no repositório GitHub do projeto.

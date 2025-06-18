# 🤖 Assistente Financeiro para Telegram

Um chatbot inteligente para gestão financeira pessoal desenvolvido em Python para hackathons. O bot utiliza processamento de linguagem natural (NLP) com Hugging Face para interpretar comandos em português brasileiro e oferece funcionalidades completas de controle financeiro.

## 🚀 Funcionalidades

### 💰 Gestão de Transações
- **Registrar Entradas**: Vendas, serviços, recebimentos
- **Registrar Saídas**: Despesas, custos, pagamentos
- **Categorização automática**: Organize suas transações por categoria

### 📝 Controle de Fiados
- **Registro inteligente**: Use linguagem natural para registrar vendas a prazo
  - Exemplo: *"200 reais fiado para João Carlos pagar dia 26 de julho"*
- **Gestão de pendências**: Consulte e quite fiados pendentes
- **Notificações automáticas**: Alertas 5, 3 e 1 dia antes do vencimento

### 📊 Relatórios Financeiros
- **Períodos flexíveis**: Hoje, últimos 7 dias, mês atual, mês anterior, geral
- **Análise completa**: Entradas, saídas, saldo e histórico de transações
- **Visualização clara**: Dados formatados e organizados

### 💡 Guia Inteligente
- **Análise de margem**: Cálculo automático da margem de lucro
- **Dicas personalizadas**: Sugestões baseadas no desempenho financeiro
- **Insights estratégicos**: Orientações para crescimento do negócio

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+**
- **python-telegram-bot**: Interface com API do Telegram
- **Hugging Face Transformers**: Processamento de linguagem natural
- **SQLite**: Banco de dados local
- **APScheduler**: Sistema de notificações
- **dateparser**: Processamento de datas em português
- **Flask**: Framework web (opcional para webhooks)

## 📦 Instalação

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/chatbot-financeiro.git
cd chatbot-financeiro
```

### 2. Instale as dependências
```bash
pip install -r requirements.txt
```

### 3. Configure o projeto

#### Método Rápido (Recomendado)
```bash
# Execute o script de configuração
python setup.py
```

#### Método Manual
1. Converse com [@BotFather](https://t.me/botfather) no Telegram
2. Crie um novo bot com `/newbot`
3. Copie o token fornecido
4. Configure as variáveis de ambiente:

#### Método 1: Arquivo .env (Recomendado)
```bash
# 1. Copie o arquivo de exemplo
cp env.example .env

# 2. Edite o arquivo .env e substitua 'seu_token_aqui' pelo token real
```

#### Método 2: Variáveis de ambiente do sistema
```bash
# Windows
set TELEGRAM_BOT_TOKEN=seu_token_aqui

# Linux/Mac
export TELEGRAM_BOT_TOKEN=seu_token_aqui
```

#### Método 3: Arquivo de configuração local
```bash
# 1. Copie o arquivo de exemplo
cp config_example.py config.py

# 2. Edite config.py e substitua 'SEU_TOKEN_AQUI' pelo token real
```

**⚠️ IMPORTANTE:** Nunca commite o token real no Git! O arquivo `config.py` está no `.gitignore` por segurança.

### 4. Execute o bot
```bash
python bot.py
```

## 🎯 Como Usar

### Iniciando o Bot
1. Inicie uma conversa com seu bot no Telegram
2. Digite `/start` ou uma saudação simples como "Olá"
3. Use os botões do menu para navegar pelas funcionalidades

### Registrando Transações
#### Entradas
1. Clique em "💰 Registrar Entrada"
2. Digite o valor (ex: 1500.50)
3. Informe a categoria (ex: Vendas)

#### Saídas
1. Clique em "💸 Registrar Saída"
2. Digite o valor
3. Informe a categoria (ex: Aluguel)

### Gerenciando Fiados
#### Novo Fiado
1. Clique em "📝 Fiados" → "➕ Registrar Novo Fiado"
2. Descreva em linguagem natural:
   - *"100 para Maria Silva pagar semana que vem"*
   - *"250 reais fiado João vencimento 15/12/2024"*
   - *"200 para Ana pagamento daqui 1 mês"*

#### Quitando Fiados
1. Vá em "📝 Fiados" → "✅ Zerar Pendência"
2. Selecione o fiado da lista
3. O valor será automaticamente adicionado às entradas

### Acompanhando Finanças
#### Relatórios
- Acesse "📊 Relatório"
- Escolha o período desejado
- Visualize entradas, saídas e saldo

#### Guia Inteligente
- Clique em "💡 Guia Inteligente"
- Receba dicas baseadas na sua margem de lucro
- Siga as sugestões de crescimento

## 🔒 Segurança e Configuração para GitHub

### ⚠️ Informações Sensíveis
Este projeto está configurado para ser seguro ao publicar no GitHub:

- **Token do bot**: Nunca é commitado diretamente no código
- **Banco de dados**: Excluído do Git (contém dados pessoais)
- **Arquivos de configuração**: Apenas exemplos são versionados

### 📂 Arquivos Importantes
- `env.example`: Template para variáveis de ambiente
- `config_example.py`: Template para configurações
- `.gitignore`: Lista arquivos sensíveis excluídos do Git

### 🛡️ Boas Práticas
1. **Use o arquivo .env** para tokens e chaves sensíveis
2. **Copie apenas os arquivos de exemplo** quando clonar o repositório
3. **Nunca commite** arquivos com dados reais
4. **Mantenha backup** do seu banco de dados local

## 🔧 Configuração Avançada

### Modelos NLP
O bot utiliza modelos da Hugging Face para NLP. Você pode alterar os modelos no arquivo `config.py`:

```python
DEFAULT_NLP_MODEL = 'pierreguillou/bert-base-cased-squad-v1.1-portuguese'
FALLBACK_NLP_MODEL = 'Babelscape/wikineural-multilingual-ner'
```

### Notificações
As notificações são enviadas automaticamente. Configure os dias no arquivo `config.py`:

```python
NOTIFICATION_DAYS = [5, 3, 1]  # Dias antes do vencimento
```

### Webhook (Produção)
Para usar em produção com webhook, configure:

```python
WEBHOOK_URL = 'https://seu-servidor.com/webhook'
```

## 📁 Estrutura do Projeto

```
chatbot-financeiro/
├── bot.py                 # Arquivo principal do bot
├── config.py             # Configurações
├── database.py           # Gerenciamento do banco de dados
├── nlp_processor.py      # Processamento de linguagem natural
├── notifications.py      # Sistema de notificações
├── utils.py              # Funções utilitárias
├── requirements.txt      # Dependências
├── README.md            # Este arquivo
└── gestao_financeira.db # Banco de dados (criado automaticamente)
```

## 🎨 Exemplos de Uso

### Registros com NLP
```
"200 para João pagar amanhã"
"150 reais Maria Silva vencimento 15/12"
"300 fiado Ana próxima semana"
"500 para Carlos daqui 1 mês"
```

### Categorias Sugeridas
- **Entradas**: Vendas, Serviços, Consultoria, Comissões
- **Saídas**: Aluguel, Material, Transporte, Marketing, Alimentação

## 🐛 Solução de Problemas

### Bot não responde
1. Verifique se o token está correto
2. Confirme se o bot está rodando
3. Verifique a conexão com internet

### Erro no NLP
1. Os modelos são baixados automaticamente na primeira execução
2. Verifique a conexão com internet
3. Em caso de erro, o bot usa fallbacks manuais

### Banco de dados
- O arquivo SQLite é criado automaticamente
- Em caso de corrupção, delete `gestao_financeira.db` para recriar

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 🏆 Características para Hackathon

- **Desenvolvimento rápido**: Estrutura modular e bem organizada
- **Funcional do primeiro uso**: Sem configurações complexas
- **Interface intuitiva**: Botões claros e navegação simples
- **IA integrada**: NLP real com Hugging Face
- **Completo**: Todas as funcionalidades de um sistema financeiro
- **Escalável**: Código preparado para produção

## 📞 Suporte

Para dúvidas ou suporte:
- Abra uma issue no GitHub
- Envie um e-mail para [carlosferreira.ttech@gmail.com]

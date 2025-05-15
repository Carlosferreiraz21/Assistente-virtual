# Chatbot Financeiro para Telegram

## 📝 Descrição
Bot para Telegram desenvolvido em Python para gerenciamento de finanças pessoais. O bot permite registrar receitas e despesas, gerar relatórios financeiros e receber dicas personalizadas baseadas no comportamento financeiro do usuário.

## 🛠️ Tecnologias Utilizadas
- Python 3.x
- python-telegram-bot v20.7
- SQLAlchemy (ORM para banco de dados)
- PyTorch + Transformers (Processamento de Linguagem Natural)
- Flask 3.0.0
- Pandas e NumPy (Análise de dados)
- SQLite (Banco de dados)

## 📁 Estrutura do Projeto
```
Chatbot-ia/
├── bot.py                 # Arquivo principal do bot
├── requirements.txt       # Dependências do projeto
├── database/             # Módulos relacionados ao banco de dados
├── handlers/             # Manipuladores de comandos e mensagens
├── nlp/                  # Módulos de processamento de linguagem natural
├── responses/            # Templates de respostas
├── services/            # Serviços auxiliares
├── utils/               # Utilitários e configurações
└── finance.db           # Banco de dados SQLite
```

## ⚙️ Funcionalidades Implementadas

### 1. Gestão de Usuários
- Registro automático de novos usuários
- Armazenamento de dados básicos do usuário

### 2. Gestão Financeira
- Registro de receitas
- Registro de despesas
- Categorização automática de transações
- Cálculo de saldo atual
- Cálculo de lucro bruto e líquido

### 3. Relatórios
- Relatório financeiro detalhado
- Histórico das últimas 5 entradas
- Histórico das últimas 5 saídas
- Totalizadores por período

### 4. Interface
- Menu interativo com botões
- Comandos intuitivos
- Respostas formatadas com emojis
- Interface amigável e responsiva

### 5. Inteligência Artificial
- Processamento de linguagem natural para entender intenções
- Sistema de dicas personalizadas baseado no comportamento financeiro
- Categorização inteligente de transações

## 🚀 Como Executar

1. Clone o repositório
```bash
git clone [URL_DO_REPOSITORIO]
cd Chatbot-ia
```

2. Crie e ative um ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instale as dependências
```bash
pip install -r requirements.txt
```

4. Configure o arquivo .env
```
TELEGRAM_TOKEN=seu_token_aqui
```

5. Execute o bot
```bash
python bot.py
```

## 📋 Comandos Disponíveis
- `/start` - Inicia o bot e mostra o menu principal
- `/help` - Mostra a ajuda e lista de comandos
- `/receita VALOR DESCRIÇÃO` - Registra uma nova receita
- `/despesa VALOR DESCRIÇÃO` - Registra uma nova despesa

## 🔄 Fluxo de Desenvolvimento

### Fase 1: Estrutura Inicial
- ✅ Criação da estrutura de diretórios
- ✅ Implementação do bot.py com funcionalidades básicas
- ✅ Configuração do sistema de NLP

### Fase 2: Banco de Dados
- ✅ Criação das tabelas com SQLAlchemy
- ✅ Implementação de funções CRUD
- ✅ Integração com o bot

### Fase 3: Funcionalidades Avançadas
- ✅ Sistema de relatórios
- ✅ Dicas personalizadas
- ✅ Interface interativa
- ✅ Processamento de linguagem natural

## 📈 Próximos Passos
1. Implementar sistema de backup automático
2. Adicionar gráficos nos relatórios
3. Implementar metas financeiras
4. Adicionar suporte a múltiplas moedas
5. Implementar sistema de categorias personalizadas

## 🔒 Segurança
- Dados armazenados localmente em SQLite
- Sem armazenamento de dados sensíveis
- Processamento de linguagem natural local

## 🤝 Contribuição
Contribuições são bem-vindas! Por favor, leia as diretrizes de contribuição antes de submeter pull requests.

## 📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes. 
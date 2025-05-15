# Assistente Virtual para Pequenos Negócios – Talento TECH 2025

> Projeto em desenvolvimento durante o Hackathon do curso técnico em Tecnologia da Informação e Comunicação (TIC), com foco em **Transformação Digital, Inovação e Empreendedorismo**.

---

# Assistente Financeiro Inteligente via Telegram

Um chatbot desenvolvido em Python para ajudar pequenos empreendedores na gestão financeira de seus negócios. Através de mensagens em linguagem natural e botões interativos no Telegram, o bot registra vendas, saídas, gera relatórios e até dá dicas inteligentes com o apoio de IA.

## 💻 Tecnologias Utilizadas

| Categoria | Tecnologia | Finalidade |
|:---|:---|:---|
| Linguagem de Programação | Python 3.x | Desenvolvimento do backend e integração com IA |
| Framework Bot | python-telegram-bot v20.7 | Interface com a API do Telegram |
| ORM | SQLAlchemy | Mapeamento objeto-relacional para banco de dados |
| IA & NLP | PyTorch + Transformers | Processamento de linguagem natural e análise |
| Framework Web | Flask 3.0.0 | Servidor web e endpoints da API |
| Análise de Dados | Pandas e NumPy | Processamento e análise de dados financeiros |
| Banco de Dados | SQLite | Armazenamento local de dados financeiros |
| Integração de IA | Hugging Face API | Geração de respostas automáticas |
| Hospedagem | PythonAnywhere | Deploy da aplicação |
| Versionamento | Git + GitHub | Controle de versões e colaboração |
| Assistente de Código | Cursor.ai | Agilização do desenvolvimento |

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

## 🧠 Funcionalidades Principais

### 🗣️ Interação Natural com IA
O usuário pode iniciar ações com mensagens como:
> "Quero registrar uma venda"  
> "Como está meu lucro?"  
> "Me dá uma dica?"

A IA interpreta a intenção e apresenta **botões interativos** com as opções.

### Menu de Ações (via Botões)

- **📈 Registrar Entrada**  
  Valor + Categoria. Fica em modo registro até o usuário digitar "sair".

- **📉 Registrar Saída**  
  Valor + Categoria. Também permanece no modo até o usuário sair.

- **💰 Lucro Líquido**  
  Entradas - Saídas do período.

- **📊 Lucro Bruto**  
  Mostra valores brutos acumulados.

- **💵 Saldo Atual**  
  Total de entradas - total de saídas.

- **📑 Relatório**  
  Resumo detalhado com entradas, saídas e totalizadores.

- **💡 Dica Inteligente**  
  A IA analisa a margem de lucro atual e sugere melhorias:
  - < 10%: risco de prejuízo
  - 10%–25%: margem aceitável
  - > 25%: excelente desempenho

## ⚙️ Funcionalidades Implementadas

### 1. Gestão de Usuários
- Registro automático de novos usuários
- Armazenamento de dados básicos do usuário

### 2. Gestão Financeira
- Registro de receitas e despesas
- Categorização automática de transações
- Cálculo de saldo e lucros
- Análise de margem de lucro

### 3. Relatórios
- Relatório financeiro detalhado
- Histórico das últimas transações
- Totalizadores por período
- Análise de desempenho

### 4. Interface
- Menu interativo com botões
- Comandos em linguagem natural
- Respostas formatadas com emojis
- Interface amigável e intuitiva

### 5. Inteligência Artificial
- Processamento de linguagem natural
- Sistema de dicas personalizadas
- Análise de comportamento financeiro
- Categorização inteligente

## 🚀 Como Executar

1. Clone o repositório
```bash
git clone https://github.com/Carlosferreiraz21/Assistente-virtual.git
cd Assistente-virtual
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

## 🔄 Status do Desenvolvimento

### Fase 1: ✅ Estrutura Inicial
- Estrutura de diretórios
- Bot básico funcional
- Sistema de NLP

### Fase 2: ✅ Banco de Dados
- Tabelas SQLAlchemy
- Funções CRUD
- Integração bot-banco

### Fase 3: ✅ Funcionalidades Avançadas
- Sistema de relatórios
- Dicas inteligentes
- Interface interativa
- NLP avançado

## 📈 Próximos Passos
1. Backup automático
2. Gráficos nos relatórios
3. Metas financeiras
4. Múltiplas moedas
5. Categorias personalizadas

## 🔒 Segurança
- Dados locais em SQLite
- Sem dados sensíveis
- NLP processado localmente

## 🤝 Contribuição
Contribuições são bem-vindas! Por favor, leia as diretrizes de contribuição antes de submeter pull requests.

## 📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

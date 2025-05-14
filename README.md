# Assistente Virtual para Pequenos Negócios – Talento TECH 2025

> Projeto em desenvolvimento durante o Hackathon do curso técnico em Tecnologia da Informação e Comunicação (TIC), com foco em **Transformação Digital, Inovação e Empreendedorismo**.

---

# Assistente Financeiro Inteligente via Telegram

Um chatbot desenvolvido em Python para ajudar pequenos empreendedores na gestão financeira de seus negócios. Através de mensagens em linguagem natural e botões interativos no Telegram, o bot registra vendas, saídas, gera relatórios e até dá dicas inteligentes com o apoio de IA.


---

## 💻 Tecnologias Utilizadas

| Categoria | Tecnologia | Finalidade |
|:---|:---|:---|
| Linguagem de Programação | Python | Desenvolvimento do backend e integração com IA |
| Framework Web | Flask | Criação do servidor, rotas e renderização das páginas HTML |
| Frontend | HTML5, CSS3, Bootstrap 5 | Interface responsiva, estilização e usabilidade |
| Banco de Dados | SQLite | Armazenamento local de entradas, saídas e informações financeiras |
| Integração de IA | Hugging Face API | Geração de respostas automáticas para o Assistente Virtual |
| Hospedagem | PythonAnywhere | Deploy da aplicação Flask com banco de dados SQLite |
| Versionamento de Código | Git + GitHub | Controle de versões e colaboração em equipe |
| Gerador de Código Assistido | Cursor.ai | Agilizar a geração de código backend, frontend e integração com IA |


---

## 🎯 Objetivo

Fornecer uma solução prática, acessível e inteligente para microempreendedores organizarem sua vida financeira sem precisar entender de planilhas ou aplicativos complexos. Toda a interação acontece no Telegram, de forma simples e humanizada.

---

## 🧠 Funcionalidades Principais

### 🗣️ Interação Natural com IA
O usuário pode iniciar ações com mensagens como:
> “Quero registrar uma venda”  
> “Como está meu lucro?”  
> “Me dá uma dica?”

A IA interpreta a intenção e apresenta **botões interativos** com as opções.

###  Menu de Ações (via Botões)

- **Registrar Entrada**  
  Valor + Categoria. Fica em modo registro até o usuário digitar "sair".

- **Registrar Saída**  
  Valor + Categoria. Também permanece no modo até o usuário sair.

- **Lucro Líquido**  
  Entradas - Saídas do período.

- **Lucro Bruto e Total**  
  Mostra valores brutos e totais acumulados.

- **Saldo Atual**  
  Total de entradas - total de saídas.

- **Gerar Relatório**  
  Resumo semanal: entradas, saídas, lucro, saldo e categorias.

- **🤖 Dica Inteligente**  
  A IA analisa a margem de lucro atual e sugere melhorias:
  - < 10%: risco de prejuízo
  - 10%–25%: margem aceitável
  - > 25%: excelente, mantém ou amplia

---

## 🧩 Funcionalidades Adicionais

- **Identificação por Telegram ID** (para múltiplos usuários)
- **Validação de dados**: evita registros inválidos
- **Confirmações antes de salvar** (ex: "Confirma entrada de R$500 para aluguel?")
- **/ajuda**: tutorial com exemplos
- **/ultimas**: últimos 5 registros
- **Mensagens de erro com sugestões de ação**

---

## 🚀 Funcionalidades Inovadoras

- **Agendamento de cobranças fiado**  
  O bot envia lembrete no dia do vencimento.

- **Alerta de prejuízo**  
  Caso o saldo fique negativo ou a margem caia.

- **IA com memória simples**  
  Usa últimos comandos para personalizar respostas.

- **Categorias customizáveis**  
  Ex: "Adicionar categoria: marketing"

- **Análise de tendência semanal**

- **Modo simulado**  
  Para testar sem salvar dados reais.

- **Exportação em CSV**

- **Sistema de metas**  
  Defina meta de lucro ou saldo e receba avisos automáticos.


## 📄 Licença

Projeto desenvolvido para fins educacionais, com código aberto para estudos, contribuições e reaproveitamento com créditos.

---


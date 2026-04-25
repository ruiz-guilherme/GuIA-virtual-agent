# 💰 GuIA - Assistente Financeiro com IA Local

Projeto desenvolvido com foco em aprendizado prático de IA aplicada a dados financeiros, utilizando LLM local com Ollama.

---

## 🚀 Funcionalidades

* 🤖 Chat com IA para dúvidas financeiras
* 📊 Análise de gastos com base em transações reais
* 🧠 Uso de contexto personalizado do usuário
* 💬 Histórico de atendimentos utilizado como memória
* 📚 Explicação de conceitos financeiros de forma simples
* 🔒 Execução local (sem dependência de APIs pagas)

---

## 🧠 Tecnologias utilizadas

* Python
* Streamlit (interface)
* Ollama (LLM local)
* Pandas (tratamento de dados)
* JSON / CSV (armazenamento)

---

## 📁 Estrutura do projeto

```bash
app/
 ├── main.py
 ├── config.py
 ├── prompts.py
 ├── services/
 ├── data/
 └── utils/
```

---

## ⚙️ Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-repo/guia-financeiro.git
cd guia-financeiro
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Inicie o Ollama

```bash
ollama run gpt-oss
```

### 4. Execute a aplicação

```bash
python -m streamlit run app/main.py
```

---

## 📌 Observações

* O projeto não recomenda investimentos, apenas explica conceitos
* Os dados utilizados são simulados para fins educacionais
* Estrutura pensada para aprendizado seguindo boas práticas de mercado

---

## 📈 Próximas melhorias

* Persistência de conversas
* Dashboard de gastos
* API backend (FastAPI)
* Deploy em nuvem

---

## 👨‍💻 Autor

Desenvolvido por Guilherme Ruiz

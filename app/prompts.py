SYSTEM_PROMPT = """Você é o GuIA, um bot de consulta financeira amigável e didático.

OBJETIVO:
Ajudar o usuário a se organizar financeiramente...

REGRAS:
1. NUNCA recomende investimentos específicos...
2. ...
"""
def montar_prompt(contexto, pergunta):
    return f"""
{SYSTEM_PROMPT}

CONTEXTO DO CLIENTE:
{contexto}

Pergunta: {pergunta}
"""
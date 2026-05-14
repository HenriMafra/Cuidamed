# CuidaMed

[![CI](https://github.com/HenriMafra/Cuidamed/actions/workflows/ci.yml/badge.svg)](https://github.com/HenriMafra/Cuidamed/actions/workflows/ci.yml)

**Aplicação publicada:** [https://cuidamed.streamlit.app/](https://cuidamed.streamlit.app/)  
**Repositório:** [https://github.com/HenriMafra/Cuidamed](https://github.com/HenriMafra/Cuidamed)

Gerenciador de horários de medicamentos com interface CLI e web, criado para apoiar idosos, cuidadores e familiares na organização de rotinas de medicação.

## Problema Real

Erros na administração de medicamentos são comuns em rotinas com vários remédios, horários e doses. Esquecimentos, doses duplicadas e interrupções de tratamento podem prejudicar especialmente idosos e pessoas que dependem de cuidadores.

## Proposta de Solução

O CuidaMed permite cadastrar, listar, buscar, atualizar e remover medicamentos com horário e quantidade de doses por dia. A aplicação também consulta a API pública OpenFDA para exibir informações complementares sobre medicamentos, como nome genérico, fabricante, via de administração, indicações e advertências.

Na versão `2.0.0`, os dados podem ser persistidos em um banco PostgreSQL hospedado no Supabase. Para desenvolvimento sem credenciais, o projeto mantém fallback local em JSON.

## Público-alvo

- Idosos com rotina de medicação.
- Cuidadores e técnicos de enfermagem domiciliar.
- Familiares responsáveis por organizar medicamentos de parentes.

## Funcionalidades

- Adicionar medicamento.
- Listar medicamentos cadastrados.
- Buscar por nome ou parte do nome.
- Atualizar nome, horário e doses.
- Remover medicamento.
- Persistir dados no Supabase.
- Consultar informações públicas via OpenFDA.
- Usar por CLI ou por interface web Streamlit.

## Tecnologias Utilizadas

- Python 3.9+
- Streamlit
- Supabase/PostgreSQL
- Requests
- Pytest
- Ruff
- GitHub Actions

## Instalação

```powershell
git clone https://github.com/HenriMafra/Cuidamed.git
cd Cuidamed
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

Em Linux/macOS:

```bash
source .venv/bin/activate
```

## Configuração do Supabase

Crie um projeto no Supabase e aplique a migração:

```powershell
supabase login
supabase link --project-ref SEU_PROJECT_REF
supabase db push
```

Também é possível copiar o SQL de `supabase/migrations/20260514024319_create_medicamentos_table.sql` e executar no SQL Editor do Supabase.

Configure as variáveis de ambiente:

```powershell
$env:SUPABASE_URL="https://SEU_PROJECT_REF.supabase.co"
$env:SUPABASE_KEY="SUA_CHAVE_ANON_OU_PUBLISHABLE"
$env:CUIDAMED_STORAGE="supabase"
```

No Streamlit Cloud, configure os mesmos valores em **Settings > Secrets**:

```toml
SUPABASE_URL = "https://SEU_PROJECT_REF.supabase.co"
SUPABASE_KEY = "SUA_CHAVE_ANON_OU_PUBLISHABLE"
CUIDAMED_STORAGE = "supabase"
```

## Execução

CLI:

```powershell
python src/main.py
```

Web local:

```powershell
streamlit run app.py
```

## Testes

```powershell
pytest tests/ -v
```

## Lint

```powershell
ruff check app.py src/ tests/
```

## CI

O workflow em `.github/workflows/ci.yml` executa em push e pull request:

- Instalação das dependências.
- Lint com Ruff.
- Testes automatizados com Pytest.

## Estrutura do Projeto

```text
Cuidamed/
├── .github/workflows/ci.yml
├── app.py
├── src/
│   ├── __init__.py
│   ├── api.py
│   ├── main.py
│   ├── medicamentos.py
│   └── supabase_repository.py
├── supabase/
│   └── migrations/
│       └── 20260514024319_create_medicamentos_table.sql
├── tests/
│   ├── test_integracao.py
│   ├── test_medicamentos.py
│   └── test_supabase_storage.py
├── CHANGELOG.md
├── README.md
├── pyproject.toml
└── requirements.txt
```

## Versão Atual

`2.0.0`

## Integrantes

- Henri Felipe Marques Mafra

## Autor

Henri Felipe Marques Mafra  
Ciência de Dados e Machine Learning — UniCEUB  
3º Semestre — 2026  
Brasília, DF - Brasil

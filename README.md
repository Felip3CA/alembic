# Configurar alembic
## ----------------------------------------------------
## Inicializar o alembic - No terminal:
### alembic init alembic
### ou
### python -m alembic init alembic
## -----------------------------------------------------------------

# Configurar a conexão com db
## ------------------------------------------------
### Abra o arquivo: almbic.init
### Procure pela linha:
#### sqlalchemy.url = driver://user.pass@localhost/dbname

### Altere para a conexão com o seu banco
#### sqlalchemy.url = sqlite:///escola.db
### ---------------------------------------------------------------------

# Conectando o alembic ao SqlAlchemy
# ------------------------------------
## Abra o arquivo: alembic/env.py
## Importe o Base do seu projeto. exemplos:
### from models import Base

## Depois, encontre a linha:
### target_metadata = None
## e altera para:
### target_metadata = Base.metadata
#Models é o arquivo onde fica as classes (tabelas)
#instalar o alembic

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()

engine = create_engine("sqlite:///escola.db")

Session = sessionmaker(bind=engine)

#Tabelas Curso e Aluno (1:N) um curso tem muitos alunos

class Curso(Base):
    __tablename__ = "cursos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    carga_horaria = Column(Integer, nullable=False)

    alunos = relationship("Aluno",back_populates="cursos") #comunicação

    def __repr__(self):
        return f"Curso = id:{self.id} - nome:{self.nome} - carga horária:{self.carga_horaria}"
    
class Aluno(Base):
    __tablename__ = "alunos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)

    curso_id = Column(Integer, ForeignKey("cursos.id")) #relação entre o curso para vários alunos
    cursos = relationship("Curso", back_populates="alunos")

    def __repr__(self):
        return f"Curso = id:{self.id} - nome:{self.nome} - email:{self.email}"
    

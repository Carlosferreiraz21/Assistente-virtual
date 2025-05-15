from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, Float, String, Boolean, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    
    id_telegram = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    data_criacao = Column(DateTime, default=datetime.now)
    
    # Relacionamentos
    entradas = relationship("Entrada", back_populates="usuario")
    saidas = relationship("Saida", back_populates="usuario")
    metas = relationship("Meta", back_populates="usuario")

class Entrada(Base):
    __tablename__ = 'entradas'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id_telegram'), nullable=False)
    valor = Column(Float, nullable=False)
    categoria = Column(String(50), nullable=False)
    data = Column(DateTime, default=datetime.now)
    fiado = Column(Boolean, default=False)
    
    # Relacionamento
    usuario = relationship("Usuario", back_populates="entradas")

class Saida(Base):
    __tablename__ = 'saidas'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id_telegram'), nullable=False)
    valor = Column(Float, nullable=False)
    categoria = Column(String(50), nullable=False)
    data = Column(DateTime, default=datetime.now)
    
    # Relacionamento
    usuario = relationship("Usuario", back_populates="saidas")

class Meta(Base):
    __tablename__ = 'metas'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id_telegram'), nullable=False)
    tipo = Column(String(50), nullable=False)  # 'economia', 'receita', 'despesa'
    valor = Column(Float, nullable=False)
    data_criacao = Column(DateTime, default=datetime.now)
    
    # Relacionamento
    usuario = relationship("Usuario", back_populates="metas")

# Criar o engine e as tabelas
engine = create_engine('sqlite:///finance.db')
Base.metadata.create_all(engine) 
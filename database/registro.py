from datetime import datetime
from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import desc, create_engine, Column, Integer, Float, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    
    id = Column(Integer, primary_key=True)
    id_telegram = Column(Integer, unique=True, nullable=False)
    nome = Column(String, nullable=False)
    data_cadastro = Column(DateTime, default=datetime.now)

class Entrada(Base):
    __tablename__ = 'entradas'
    
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, nullable=False)
    valor = Column(Float, nullable=False)
    categoria = Column(String, nullable=False)
    fiado = Column(Boolean, default=False)
    data = Column(DateTime, default=datetime.now)

class Saida(Base):
    __tablename__ = 'saidas'
    
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, nullable=False)
    valor = Column(Float, nullable=False)
    categoria = Column(String, nullable=False)
    data = Column(DateTime, default=datetime.now)

class Meta(Base):
    __tablename__ = 'metas'
    
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, nullable=False)
    tipo = Column(String, nullable=False)
    valor = Column(Float, nullable=False)
    data_criacao = Column(DateTime, default=datetime.now)

# Configuração do banco de dados
engine = create_engine('sqlite:///finance.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

def get_session() -> Session:
    """Cria e retorna uma nova sessão do banco de dados."""
    return Session()

def registrar_usuario(id_telegram: int, nome: str) -> Usuario:
    """
    Registra um novo usuário ou retorna o existente.
    
    Args:
        id_telegram: ID do usuário no Telegram
        nome: Nome do usuário
    
    Returns:
        Usuario: Objeto do usuário criado/encontrado
    """
    with get_session() as session:
        usuario = session.query(Usuario).filter_by(id_telegram=id_telegram).first()
        if not usuario:
            usuario = Usuario(id_telegram=id_telegram, nome=nome)
            session.add(usuario)
            session.commit()
        return usuario

def registrar_entrada(usuario_id: int, valor: float, categoria: str, fiado: bool = False) -> bool:
    """
    Registra uma nova entrada financeira no banco de dados.
    
    Args:
        usuario_id: ID do usuário no Telegram
        valor: Valor da entrada
        categoria: Categoria da entrada
        fiado: Se a entrada é fiada ou não
        
    Returns:
        bool: True se o registro foi bem sucedido, False caso contrário
    """
    try:
        session = Session()
        nova_entrada = Entrada(
            usuario_id=usuario_id,
            valor=valor,
            categoria=categoria,
            fiado=fiado,
            data=datetime.now()
        )
        session.add(nova_entrada)
        session.commit()
        return True
    except Exception:
        session.rollback()
        return False
    finally:
        session.close()

def registrar_saida(
    usuario_id: int,
    valor: float,
    categoria: str,
    data: Optional[datetime] = None
) -> Optional[float]:
    """
    Registra uma nova saída financeira.
    
    Args:
        usuario_id: ID do usuário no Telegram
        valor: Valor da saída
        categoria: Categoria da saída
        data: Data da saída (default: datetime.now())
    
    Returns:
        Optional[float]: Valor da saída registrada, None se houver erro
    """
    try:
        with get_session() as session:
            saida = Saida(
                usuario_id=usuario_id,
                valor=valor,
                categoria=categoria,
                data=data or datetime.now()
            )
            session.add(saida)
            session.commit()
            return valor
    except Exception:
        return None

def consultar_entradas(
    usuario_id: int,
    categoria: Optional[str] = None,
    data_inicio: Optional[datetime] = None,
    data_fim: Optional[datetime] = None,
    apenas_fiado: bool = False
) -> List[Entrada]:
    """
    Consulta entradas financeiras com filtros opcionais.
    
    Args:
        usuario_id: ID do usuário no Telegram
        categoria: Filtrar por categoria específica
        data_inicio: Data inicial para filtro
        data_fim: Data final para filtro
        apenas_fiado: Retornar apenas entradas fiadas
    
    Returns:
        List[Entrada]: Lista de entradas encontradas
    """
    with get_session() as session:
        query = session.query(Entrada).filter(Entrada.usuario_id == usuario_id)
        
        if categoria:
            query = query.filter(Entrada.categoria == categoria)
        if data_inicio:
            query = query.filter(Entrada.data >= data_inicio)
        if data_fim:
            query = query.filter(Entrada.data <= data_fim)
        if apenas_fiado:
            query = query.filter(Entrada.fiado == True)
            
        return query.order_by(desc(Entrada.data)).all()

def consultar_saidas(
    usuario_id: int,
    categoria: Optional[str] = None,
    data_inicio: Optional[datetime] = None,
    data_fim: Optional[datetime] = None
) -> List[Saida]:
    """
    Consulta saídas financeiras com filtros opcionais.
    
    Args:
        usuario_id: ID do usuário no Telegram
        categoria: Filtrar por categoria específica
        data_inicio: Data inicial para filtro
        data_fim: Data final para filtro
    
    Returns:
        List[Saida]: Lista de saídas encontradas
    """
    with get_session() as session:
        query = session.query(Saida).filter(Saida.usuario_id == usuario_id)
        
        if categoria:
            query = query.filter(Saida.categoria == categoria)
        if data_inicio:
            query = query.filter(Saida.data >= data_inicio)
        if data_fim:
            query = query.filter(Saida.data <= data_fim)
            
        return query.order_by(desc(Saida.data)).all()

def registrar_meta(
    usuario_id: int,
    tipo: str,
    valor: float
) -> Meta:
    """
    Registra uma nova meta financeira.
    
    Args:
        usuario_id: ID do usuário no Telegram
        tipo: Tipo da meta ('economia', 'receita', 'despesa')
        valor: Valor da meta
    
    Returns:
        Meta: Objeto da meta criada
    """
    with get_session() as session:
        meta = Meta(
            usuario_id=usuario_id,
            tipo=tipo,
            valor=valor
        )
        session.add(meta)
        session.commit()
        return meta

def consultar_metas(usuario_id: int, tipo: Optional[str] = None) -> List[Meta]:
    """
    Consulta metas financeiras do usuário.
    
    Args:
        usuario_id: ID do usuário no Telegram
        tipo: Filtrar por tipo específico de meta
    
    Returns:
        List[Meta]: Lista de metas encontradas
    """
    with get_session() as session:
        query = session.query(Meta).filter(Meta.usuario_id == usuario_id)
        
        if tipo:
            query = query.filter(Meta.tipo == tipo)
            
        return query.order_by(desc(Meta.data_criacao)).all() 
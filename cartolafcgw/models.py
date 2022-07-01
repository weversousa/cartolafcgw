from cartolafcgw.database import db


class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer)
    time_nome = db.Column(db.String(30), nullable=False)
    primeiro_nome = db.Column(db.String(16), nullable=False)
    segundo_nome = db.Column(db.String(10), nullable=False)
    ultimo_nome = db.Column(db.String(16))
    url_escudo = db.Column(db.String)

    __table_args__ = (
        db.PrimaryKeyConstraint('id', name='pk_usuarios'),
    )

    def __init__(
        self, id, time_nome, primeiro_nome, segundo_nome, ultimo_nome,
        url_escudo=None
    ):
        self.id = id
        self.time_nome = time_nome
        self.primeiro_nome = primeiro_nome
        self.segundo_nome = segundo_nome
        self.ultimo_nome = ultimo_nome
        self.url_escudo = url_escudo

    def __repr__(self):
        return f'''Usuario(id={self.id}, time_nome={self.time_nome}, 
        primeiro_nome={self.primeiro_nome})'''


class Rodada(db.Model):
    __tablename__ = 'rodadas'

    id = db.Column(db.Integer)
    inicio = db.Column(db.DateTime, nullable=False)
    fim = db.Column(db.DateTime, nullable=False)

    __table_args__ = (
        db.PrimaryKeyConstraint('id', name='pk_rodadas'),
        db.UniqueConstraint('inicio', name='uq_inicio'),
        db.UniqueConstraint('fim', name='uq_fim')
    )

    def __init__(self, id, inicio, fim):
        self.id = id
        self.inicio = inicio
        self.fim = fim

    def __repr__(self):
        return f'Rodada(id={self.id}, inicio={self.inicio}, fim={self.fim})'


class Ponto(db.Model):
    __tablename__ = 'pontos'

    usuario_id = db.Column(db.Integer)
    rodada_id = db.Column(db.Integer)
    total = db.Column(db.Numeric(5,2))

    __table_args__ = (
        db.PrimaryKeyConstraint('usuario_id', 'rodada_id', name='pk_pontos'),
        db.ForeignKeyConstraint(
            ['usuario_id'], ['usuarios.id'], name='fk_pontos_usuarios'
        ),
        db.ForeignKeyConstraint(
            ['rodada_id'], ['rodadas.id'], name='fk_pontos_rodadas'
        )
    )

    def __init__(self, usuario_id, rodada_id, total):
        self.usuario_id = usuario_id
        self.rodada_id = rodada_id
        self.total = total

    def __repr__(self):
        return f'''Usuario(id=, time_nome=, 
        primeiro_nome={self.total})'''


class RankingLigaView(db.Model):
    __tablename__ = 'ranking_liga'

    total = db.Column(db.Numeric(5,2), primary_key=True)
    time_nome = db.Column(db.String(30))
    usuario_nome = db.Column(db.Text)
    url_escudo = db.Column(db.String)

    def __repr__(self):
        return f'RankingLigaView(total={self.total}, time_nome={self.time_nome}, \
usuario_nome={self.usuario_nome})'


class RankingMesView(db.Model):
    __tablename__ = 'ranking_mes'

    total = db.Column(db.Numeric(5,2), primary_key=True)
    mes = db.Column(db.Numeric)
    mes_nome = db.Column(db.Text)
    time_nome = db.Column(db.String(30))
    usuario_nome = db.Column(db.Text)
    url_escudo = db.Column(db.String)

    def __repr__(self):
        return f'Ranking_nomeView(total={self.total}, \
mes_nome={self.mes_nome}, time_nome={self.time_nome}, \
usuario_nome={self.usuario_nome})'


class RankingMitoView(db.Model):
    __tablename__ = 'ranking_mito'

    total = db.Column(db.Numeric(5,2), primary_key=True)
    rodada_id = db.Column(db.Integer)
    time_nome = db.Column(db.String(30))
    usuario_nome = db.Column(db.Text)
    url_escudo = db.Column(db.String)

    def __repr__(self):
        return f'RankingMitoView(total={self.total}, time_nome={self.time_nome}, \
usuario_nome={self.usuario_nome})'


class RankingTurnoView(db.Model):
    __tablename__ = 'ranking_turno'

    total = db.Column(db.Numeric(5,2), primary_key=True)
    turno = db.Column(db.Integer)
    time_nome = db.Column(db.String(30))
    usuario_nome = db.Column(db.Text)
    url_escudo = db.Column(db.String)

    def __repr__(self):
        return f'RankingTurnoView(total={self.total}, turno={self.turno}, \
time_nome={self.time_nome}, usuario_nome={self.usuario_nome})'


class GraficoLigaView(db.Model):
    __tablename__ = 'grafico_liga'

    rodada_id = db.Column(db.Integer, primary_key=True)
    posicao = db.Column(db.Integer)
    time_nome = db.Column(db.Text, primary_key=True)

    def __repr__(self):
        return f'GraficoLigaView( total_acumulado={self. total_acumulado}, \
time_nome={self.time_nome}'

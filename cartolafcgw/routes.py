from flask import redirect, render_template, url_for

from cartolafcgw.api import CartolaFC
from cartolafcgw.database import db
from cartolafcgw.graficos import LigaGrafico
from cartolafcgw.models import RankingTurnoView, RankingLigaView, RankingMesView, RankingMitoView, GraficoLigaView, Ponto


def config(app):

    @app.route('/')
    def index():
        return redirect(url_for('dashboard'))

    @app.route('/api.gw-cartola')
    def api():
        cfc = CartolaFC(app.config['X_GLB_TOKEN'])

        # status_mercado
        # 4 Mercado em manutenção
        # 2 fechado
        # 1 aberto

        # rodada_atual

        # atletas
        # mensagem: "Rodada inválida".

        rodadas = cfc.rodadas()
        mercado = cfc.mercado()
        time = cfc.time(25395518, mercado['rodada_atual'])
        atletas = cfc.atletas(mercado['rodada_atual'])
        liga = cfc.liga('gw-altino-fc')
        atleta = cfc.atleta(25395518)

        return {
            'Rodadas': rodadas,
            'Mercado': mercado,
            'Time': time,
            'Atletas': atletas,
            'Liga': liga,
            'Atleta': atleta
        }

    @app.route('/dashboard')
    def dashboard():
        cfc = CartolaFC(app.config['X_GLB_TOKEN'])
        mercado = cfc.mercado()
        if mercado['status_mercado'] == 1:
            status_mercado = 'aberto'
        elif mercado['status_mercado'] == 2:
            status_mercado = 'fechado'
        elif mercado['status_mercado'] == 4:
            status_mercado = 'em manutenção'
        grafico = LigaGrafico()
        ranking_turno = RankingTurnoView.query.first()
        ranking_mito = RankingMitoView.query.first()[0]
        atualizado_ate = db.session.query(db.func.max(Ponto.rodada_id)).first()
        context = {
            'title': 'Dashboard',
            'ranking_liga': [
                {
                    'total': usuario.total,
                    'posicao': n,
                    'time_nome': usuario.time_nome,
                    'usuario_nome': usuario.usuario_nome,
                    'url_escudo': usuario.url_escudo,
                }
                for n, usuario in enumerate(RankingLigaView.query.all(), 1)
            ],
            'ranking_mes': [
                {
                    'total': usuario.total,
                    'mes_nome': usuario.mes_nome[0:3],
                    'time_nome': usuario.time_nome,
                    'usuario_nome': usuario.usuario_nome,
                    'url_escudo': usuario.url_escudo,
                }
                for n, usuario in enumerate(RankingMesView.query.all(), 1)
            ],
            'ranking_mito': {
                'total': ranking_mito.total,
                'rodada': ranking_mito.rodada_id,
                'time_nome': ranking_mito.time_nome,
                'usuario_nome': ranking_mito.usuario_nome,
                'url_escudo': ranking_mito.url_escudo,
            },
            'ranking_turno': {
                'total': ranking_turno.total,
                'turno': ranking_turno.turno,
                'time_nome': ranking_turno.time_nome,
                'usuario_nome': ranking_turno.usuario_nome,
                'url_escudo': ranking_turno.url_escudo
             },
             'grafico': grafico.criar_figura(),
             'rodada_atual': mercado['rodada_atual'],
             'status_mercado': status_mercado,
             'atualizado_ate': atualizado_ate
        }
        return render_template('dashboard.html', **context)

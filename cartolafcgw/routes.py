from flask import redirect, render_template, url_for

from cartolafcgw.api import CartolaFC
from cartolafcgw.models import RankingTurnoView, RankingLigaView, RankingMesView, RankingMitoView


def config(app):

    @app.route('/')
    def index():
        return redirect(url_for('dashboard'))

    @app.route('/api.gw-cartola')
    def api():
        cfc = CartolaFC(app.config['X_GLB_TOKEN'])

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
        ranking_turno = RankingTurnoView.query.first()
        ranking_mito = RankingMitoView.query.first()
        context = {
            'title': 'Dashboard',
            'ranking_liga': [
                {
                    'total': usuario.total,
                    'posicao': f'{n}º',
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
             }
        }
        return render_template('dashboard.html', **context)

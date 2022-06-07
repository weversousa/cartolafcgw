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
        def meses(mes):
            match mes:
                case 4:
                    return 'ABRIL'
                case 5:
                    return 'MAIO'
                case 6:
                    return 'JUNHO'

        context = {
            'title': 'Dashboard',
            'ranking_liga': [
                {
                    'total': usuario.total,
                    'posicao': f'{n}º',
                    'time_nome': usuario.time_nome,
                    'primeiro_nome': usuario.primeiro_nome,
                    'segundo_nome': usuario.segundo_nome,
                    'url_escudo': usuario.url_escudo,
                }
                for n, usuario in enumerate(RankingLigaView.query.all(), 1)
            ],
            'ranking_mes': [
                {
                    'total': usuario.total,
                    'mes': meses(usuario.mes),
                    'time_nome': usuario.time_nome,
                    'primeiro_nome': usuario.primeiro_nome,
                    'segundo_nome': usuario.segundo_nome,
                    'url_escudo': usuario.url_escudo,
                }
                for n, usuario in enumerate(RankingMesView.query.all(), 1)
            ],
            'ranking_mito': [
                {
                    'total': usuario.total,
                    'rodada': usuario.rodada_id,
                    'time_nome': usuario.time_nome,
                    'primeiro_nome': usuario.primeiro_nome,
                    'segundo_nome': usuario.segundo_nome,
                    'url_escudo': usuario.url_escudo,
                }
                for usuario in RankingMitoView.query.all()
            ],
            'ranking_turno': [
                {
                    'total': usuario.total,
                    'turno': usuario.turno,
                    'time_nome': usuario.time_nome,
                    'primeiro_nome': usuario.primeiro_nome,
                    'segundo_nome': usuario.segundo_nome,
                    'url_escudo': usuario.url_escudo,
                }
                for usuario in RankingTurnoView.query.all()
            ]
        }
        return render_template('dashboard.html', **context)

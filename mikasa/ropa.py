import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from mikasa.db import get_db

bp = Blueprint('ropa', __name__, url_prefix='/ropa')

@bp.route('/agrega', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        tipo = request.form['tipo']
        descripcion = request.form['descripcion']
        costo = request.form['costo']
        veces = request.form['veces']
        comentarios = request.form['comentarios']
        db = get_db()
        error = None

        if not tipo:
            error = 'Que tipo es?'
        elif not descripcion:
            error = 'Necesitamos la descripcion.'
        elif not costo:
            error = 'Necesitamos el costo.'
        elif db.execute(
            'SELECT id FROM descripcion WHERE descripcion = ?', (descripcion,)
        ).fetchone() is not None:
            error = ' {} ya esta registrada.'.format(descripcion)

        if error is None:
            db.execute(
                'INSERT INTO ropa (tipo, descripcion, costo, veces, comentarios) VALUES (?, ?, ?, ?, ?)',
                (tipo, descripcion, costo, veces, comentarios))
            db.commit()
            return redirect(url_for('/')) #E: Cambiar por revision

        flash(error)

    return render_template('posesiones/agregaRopa.html')
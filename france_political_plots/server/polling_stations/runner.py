from .builder import Dashboard



app = Dashboard().make()
server = app.server
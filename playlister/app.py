from flask import Flask, render_template

app = Flask(__name__)

#@app.route('/')
#def index():
#	"""Return homepage."""
#	return render_template('home.html', msg='Hello, world!')

playlists = [
		{ 'title': 'Choba Playlist', 'description': 'Select a song' },
		{ 'title': '80\'s Music', 'description': 'Don\'t stop believing!' }
		]

@app.route('/')
def playlists_index():
	"""Show all playlists."""
	return render_template('playlists_index.html', playlists=playlists)

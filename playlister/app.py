from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

client = MongoClient()
db = client.Playlister
playlists = db.playlists

app = Flask(__name__)

#@app.route('/')
#def index():
#	"""Return homepage."""
#	return render_template('home.html', msg='Hello, world!')

# playlists = [
#		{ 'title': 'Choba Playlist', 'description': 'Select a song' },
#		{ 'title': '80\'s Music', 'description': 'Don\'t stop believing!' }
#		]

@app.route('/')
def playlists_index():
	"""Show all playlists."""
	return render_template('playlists_index.html', playlists=playlists.find())

@app.route('/playlists/new')
def playlists_new():
	"""Create a new playlist."""
	return render_template('playlists_new.html')

@app.route('/playlists', methods=['POST'])
def playlists_submit():
#    """Submit a new playlist."""
#    print(request.form.to_dict())
#    return redirect(url_for('playlists_index'))

#@app.route('/playlists', methods=['POST'])
#def playlists_submit():
    """Submit a new playlist."""
    playlist = {
        'title': request.form.get('title'),
        'description': request.form.get('description')
    }
    playlists.insert_one(playlist)
    return redirect(url_for('playlists_index'))

import datetime
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
    return render_template('playlists_new.html', playlist={}, title='New Playlist')

@app.route('/playlists', methods=['POST'])
def playlists_submit():
    """Submit a new playlist."""
    playlist = {
        'title': request.form.get('title'),
        'description': request.form.get('description'),
        'videos': request.form.get('videos').split(),
        'created_at': datetime.now()
    }
    print(playlist)
    playlist_id = playlists.insert_one(playlist).inserted_id
    return redirect(url_for('playlists_show', playlist_id=playlist_id))
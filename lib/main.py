# from database import session
# import click
# from models import Artist, Album, Genre

# def main():
#     while True:
#         print('Welcome to the music app')
#         print('1. Add an artist')
#         print('2. Add an album')
#         print('3. Add a genre')
#         print('4. Delete an album')
#         print('5. Search albums by artist')
#         print('6. List all artists')
#         print('7. List all genres')
#         print('8. Check all the albums')
#         print('0. Exit')

#         choice = input('Enter your choice: ')

#         if choice == '1':
#             create_artist()
#         elif choice == '2':
#             create_album()
#         elif choice == '3':
#             create_genre()
#         elif choice == '4':
#             delete_album()
#         elif choice == '5':
#             search_albums_by_artist()
#         elif choice == '6':
#             list_all_artists()
#         elif choice == '7':
#             list_all_genres()
#         elif choice == '8':
#             album_details = all_album_details()
#             for album in album_details:
#                 print('Album Name:', album['name'])
#                 print('Artist:', album['artist'])
#                 print('Genre:', album['genre'])
#                 print('')
#         elif choice == '0':
#             print('Closing application...')
#             break
#         else:
#             click.echo('Invalid choice')
#             click.echo('')
            

# def create_artist():
#     stage_name = input("Enter artist's stage name: ")
#     real_name = input("Enter artist's real name: ")
#     new_artist = Artist(stage_name=stage_name, real_name=real_name)
#     session.add(new_artist)
#     session.commit()
#     click.echo('New artist created')
#     click.echo('')

# def create_album():
#     name = input("Enter album's name: ")
#     artists = session.query(Artist).all()
#     genres = session.query(Genre).all()
    
#     print('Select an artist:')
#     for i, artist in enumerate(artists, 1):
#         print(f"{i}. {artist.stage_name}")
    
#     artist_choice = int(input('Enter the number for the artist: ')) - 1
#     selected_artist = artists[artist_choice]
    
#     print('Select a genre:')
#     for i, genre in enumerate(genres, 1):
#         print(f"{i}. {genre.name}")
    
#     genre_choice = int(input('Enter the number for the genre: ')) - 1
#     selected_genre = genres[genre_choice]
    
#     new_album = Album(name=name, artist=selected_artist, genre=selected_genre)
#     session.add(new_album)
#     session.commit()
#     click.echo('New album created successfully!')
#     click.echo('')

# def create_genre():
#     name = input("Enter genre's name: ")
#     new_genre = Genre(name=name)
#     session.add(new_genre)
#     session.commit()
#     click.echo('New genre created successfully!')
#     click.echo('')

# def all_album_details():
#     albums = session.query(Album).all()
#     album_details = []
#     if albums:
#         for album in albums:
#             album_details.append({
#                 'name': album.name,
#                 'artist': album.artist.stage_name,
#                 'genre': album.genre.name
#             })
#     return album_details


# def delete_album():
#     album_name = input("Enter the name of the album to delete: ")
#     album_to_delete = session.query(Album).filter_by(name=album_name).first()
    
#     if album_to_delete:
#         session.delete(album_to_delete)
#         session.commit()
#         click.echo(f'Album "{album_name}" deleted successfully.')
#         click.echo('')
        
#     else:
#         click.echo(f'Album "{album_name}" not found.')

# def search_albums_by_artist():
#     artist_name = input("Enter the name of the artist to search for albums: ").title()
#     artist = session.query(Artist).filter_by(stage_name=artist_name).first()
    
#     if artist:
#         albums = artist.albums
#         if albums:
#             click.echo(f'Albums by {artist_name}:')
#             for album in albums:
#                 click.echo(album.name)
                
#         else:
#             click.echo(f'No albums found for artist "{artist_name}".')
#             click.echo('')
#     else:
#         click.echo(f'Artist "{artist_name}" not found.')
#         click.echo('')
        
# def list_all_artists():
#     artists = session.query(Artist).all()
    
#     if artists:
#         click.echo('List of all artists:')
#         for artist in artists:
#             click.echo(artist.stage_name)
#         click.echo('')
            
#     else:
#         click.echo('No artists found.')

# def list_all_genres():
#     genres = session.query(Genre).all()
    
#     if genres:
#         click.echo('List of all genres:')
#         for genre in genres:
#             click.echo(genre.name)
#         click.echo('')
            
#     else:
#         click.echo('No genres found.')


# if __name__ == '__main__':
#     main()
import click
from database import session
from models import Artist, Album, Genre

def main():
    while True:
        click.echo('Welcome to the music app')
        click.echo('1. Add an artist')
        click.echo('2. Add an album')
        click.echo('3. Add a genre')
        click.echo('4. Delete an album')
        click.echo('5. Search albums by artist')
        click.echo('6. List all artists')
        click.echo('7. List all genres')
        click.echo('8. Check all the albums')
        click.echo('0. Exit')

        choice = click.prompt('Enter your choice', type=int)

        if choice == 1:
            create_artist()
        elif choice == 2:
            create_album()
        elif choice == 3:
            create_genre()
        elif choice == 4:
            delete_album()
        elif choice == 5:
            search_albums_by_artist()
        elif choice == 6:
            list_all_artists()
        elif choice == 7:
            list_all_genres()
        elif choice == 8:
            album_details()
        elif choice == 0:
            click.echo('Closing application...')
            break
        else:
            click.echo('Invalid choice')
            click.echo('')

@click.option('--stage_name', prompt="Enter artist's stage name", help="The stage name of the artist")
@click.option('--real_name', prompt="Enter artist's real name", help="The real name of the artist")
def create_artist(stage_name, real_name):
    new_artist = Artist(stage_name=stage_name, real_name=real_name)
    session.add(new_artist)
    session.commit()
    click.echo('New artist created')
    click.echo('')


@click.option('--name', prompt="Enter album's name", help="The name of the album")
@click.option('--artist', prompt="Select an artist", type=click.Choice([artist.stage_name for artist in session.query(Artist).all()]), help="The artist of the album")
@click.option('--genre', prompt="Select a genre", type=click.Choice([genre.name for genre in session.query(Genre).all()]), help="The genre of the album")
def create_album(name, artist, genre):
    selected_artist = session.query(Artist).filter_by(stage_name=artist).first()
    selected_genre = session.query(Genre).filter_by(name=genre).first()
    
    new_album = Album(name=name, artist=selected_artist, genre=selected_genre)
    session.add(new_album)
    session.commit()
    click.echo('New album created successfully!')
    click.echo('')

@click.option('--name', prompt="Enter genre's name", help="The name of the genre")
def create_genre(name):
    new_genre = Genre(name=name)
    session.add(new_genre)
    session.commit()
    click.echo('New genre created successfully!')
    click.echo('')

def album_details():
    albums = session.query(Album).all()
    if albums:
        for album in albums:
            click.echo(f'Album Name: {album.name}')
            click.echo(f'Artist: {album.artist.stage_name}')
            click.echo(f'Genre: {album.genre.name}')
            click.echo('')
    else:
        click.echo('No albums found.')

@click.option('--album_name', prompt="Enter the name of the album to delete", help="The name of the album to delete")
def delete_album(album_name):
    album_to_delete = session.query(Album).filter_by(name=album_name).first()
    
    if album_to_delete:
        session.delete(album_to_delete)
        session.commit()
        click.echo(f'Album "{album_name}" deleted successfully.')
        click.echo('')
        
    else:
        click.echo(f'Album "{album_name}" not found.')

@click.option('--artist_name', prompt="Enter the name of the artist to search for albums", help="The name of the artist to search for albums")
def search_albums_by_artist(artist_name):
    artist = session.query(Artist).filter_by(stage_name=artist_name).first()
    
    if artist:
        albums = artist.albums
        if albums:
            click.echo(f'Albums by {artist_name}:')
            for album in albums:
                click.echo(album.name)
                
        else:
            click.echo(f'No albums found for artist "{artist_name}".')
            click.echo('')
    else:
        click.echo(f'Artist "{artist_name}" not found.')
        click.echo('')

def list_all_artists():
    artists = session.query(Artist).all()
    
    if artists:
        click.echo('')
        click.echo('List of all artists:')
        for artist in artists:
            click.echo(artist.stage_name)
        click.echo('')
            
    else:
        click.echo('No artists found.')

def list_all_genres():
    genres = session.query(Genre).all()
    
    if genres:
        click.echo('')
        click.echo('List of all genres:')
        for genre in genres:
            click.echo(genre.name)
        click.echo('')
            
    else:
        click.echo('No genres found.')

if __name__ == '__main__':
    main()
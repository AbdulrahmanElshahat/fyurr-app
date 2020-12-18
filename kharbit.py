# # class Venue(db.Model):
# #     __tablename__ = 'venue'

# #     id = db.Column(db.Integer, primary_key=True)
# #     name = db.Column(db.String)
# #     genres = db.Column(db.String())
# #     address = db.Column(db.String(120))
# #     city = db.Column(db.String(120))
# #     state = db.Column(db.String(120))
# #     phone = db.Column(db.String(120))
# #     website = db.Column(db.String())
# #     facebook_link = db.Column(db.String(120))
# #     seeking_talent = db.Column(db.String())
# #     seeking_description = db.Column(db.String())
# #     image_link = db.Column(db.String(500))  
# #     # TODO: implement any missing fields, as a database migration using Flask-Migrate

# # class Artist(db.Model):
# #     __tablename__ = 'artist'

# #     id = db.Column(db.Integer, primary_key=True)
# #     name = db.Column(db.String)
# #     genres = db.Column(db.String(120))
# #     city = db.Column(db.String(120))
# #     state = db.Column(db.String(120))
# #     phone = db.Column(db.String(120))
# #     website = db.Column(db.String())
# #     facebook_link = db.Column(db.String(120))
# #     seeking_venue = db.Column(db.String())
# #     seeking_description = db.Column(db.String())
# #     image_link = db.Column(db.String(500))
    

# #     # TODO: implement any missing fields, as a database migration using Flask-Migrate

# class Show(db.Model):
#     __tablename__ = 'show'
#     id = db.Column(db.Integer, primary_key=True)
#     start_time = db.Column(db.DateTime)
#     venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'), nullable=False)
#     venue_name = db.relationship('Venue', backref=db.backref('shows'))
#     artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)
#     artist = db.relationship('Artist', backref=db.backref('shows'))


venue given data 

# data1={
#     "id": 1,
#     "name": "The Musical Hop",
#     "genres": ["Jazz", "Reggae", "Swing", "Classical", "Folk"],
#     "address": "1015 Folsom Street",
#     "city": "San Francisco",
#     "state": "CA",
#     "phone": "123-123-1234",
#     "website": "https://www.themusicalhop.com",
#     "facebook_link": "https://www.facebook.com/TheMusicalHop",
#     "seeking_talent": True,
#     "seeking_description": "We are on the lookout for a local artist to play every two weeks. Please call us.",
#     "image_link": "https://images.unsplash.com/photo-1543900694-133f37abaaa5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=60",
    
    
  #   "past_shows": [{
  #     "artist_id": 4,
  #     "artist_name": "Guns N Petals",
  #     "artist_image_link": "https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80",
  #     "start_time": "2019-05-21T21:30:00.000Z"
  #   }],
  #   "upcoming_shows": [],
  #   "past_shows_count": 1,
  #   "upcoming_shows_count": 0,
  # }
  # data2={
  #   VALUES ('The Dueling Pianos Bar', '["Classical", "R&B", "Hip-Hop"]' , '335 Delancey Street', 'New York', 'NY', '914-003-1132', 'https://www.theduelingpianos.com','https://www.facebook.com/theduelingpianos','False', ' ','https://images.unsplash.com/photo-1497032205916-ac775f0649ae?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80');
  #   "past_shows": [],
  #   "upcoming_shows": [],
  #   "past_shows_count": 0,
  #   "upcoming_shows_count": 0,
  # }
  # data3={
  #   "id": 3,

  #   VALUES ('Park Square Live Music & Coffee' , '["Rock n Roll", "Jazz", "Classical", "Folk"]', '34 Whiskey Moore Ave', 'San Francisco','CA','415-000-1234','https://www.parksquarelivemusicandcoffee.com','https://www.facebook.com/ParkSquareLiveMusicAndCoffee','False','','https://images.unsplash.com/photo-1485686531765-ba63b07845a7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=747&q=80');
 
  #   "past_shows": [{
  #     "artist_id": 5,
  #     "artist_name": "Matt Quevedo",
  #     "artist_image_link": "https://images.unsplash.com/photo-1495223153807-b916f75de8c5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80",
  #     "start_time": "2019-06-15T23:00:00.000Z"
  #   }],
  #   "upcoming_shows": [{
  #     "artist_id": 6,
  #     "artist_name": "The Wild Sax Band",
  #     "artist_image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80",
  #     "start_time": "2035-04-01T20:00:00.000Z"
  #   }, {
  #     "artist_id": 6,
  #     "artist_name": "The Wild Sax Band",
  #     "artist_image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80",
  #     "start_time": "2035-04-08T20:00:00.000Z"
  #   }, {
  #     "artist_id": 6,
  #     "artist_name": "The Wild Sax Band",
  #     "artist_image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80",
  #     "start_time": "2035-04-15T20:00:00.000Z"
  #   }],
  #   "past_shows_count": 1,
  #   "upcoming_shows_count": 1,
  # }


  # artist route given data 

  # {
  #   "id": 4,
  #   "name": "Guns N Petals",
  # }, {
  #   "id": 5,
  #   "name": "Matt Quevedo",
  # }, {
  #   "id": 6,
  #   "name": "The Wild Sax Band",
  # }


  artists given data 
INSERT INTO artist (name, genres, city, state, phone, website, facebook_link,seeking_venue, seeking_description,image_link)
VALUES ('Guns N Petals','["Rock n Roll"]','San Francisco','CA','326-123-5000','https://www.gunsnpetalsband.com','https://www.facebook.com/GunsNPetals','True','Looking for shows to perform at in the San Francisco Bay Area!','https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80');
  # data1={
    
  #   "name": "",
  #   "genres": ,
  #   "city": "",
  #   "state": "",
  #   "phone": "",
  #   "website": "",
  #   "facebook_link": "",
  #   "seeking_venue": ,
  #   "seeking_description": "",
  #   "image_link": "",
  #   "past_shows": [{
  #     "venue_id": 1,
  #     "venue_name": "The Musical Hop",
  #     "venue_image_link": "https://images.unsplash.com/photo-1543900694-133f37abaaa5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=60",
  #     "start_time": "2019-05-21T21:30:00.000Z"
  #   }],
  #   "upcoming_shows": [],
  #   "past_shows_count": 1,
  #   "upcoming_shows_count": 0,
  # }

  INSERT INTO artist (name, genres, city, state, phone, website, facebook_link,seeking_venue, seeking_description,image_link)
VALUES ('Matt Quevedo','["Jazz"]','New York','NY','300-400-5000',' ','https://www.facebook.com/mattquevedo923251523','False','','https://images.unsplash.com/photo-1495223153807-b916f75de8c5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80');
  # data2={
  #   "id": 5,
  #   "name": "",
  #   "genres": ,
  #   "city": "",
  #   "state": "",
  #   "phone": "",
  #   "facebook_link": "",
  #   "seeking_venue": ,
  #   "image_link": "",
  #   "past_shows": [{
  #     "venue_id": 3,
  #     "venue_name": "Park Square Live Music & Coffee",
  #     "venue_image_link": "https://images.unsplash.com/photo-1485686531765-ba63b07845a7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=747&q=80",
  #     "start_time": "2019-06-15T23:00:00.000Z"
  #   }],
  #   "upcoming_shows": [],
  #   "past_shows_count": 1,
  #   "upcoming_shows_count": 0,
  # }

  INSERT INTO artist (name, genres, city, state, phone, website, facebook_link,seeking_venue, seeking_description,image_link)
VALUES ('The Wild Sax Band','["Jazz", "Classical"]','San Francisco','CA','432-325-5432',' ','','False','','https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80');
  # data3={
  #   "id": 6,
  #   "name": "",
  #   "genres": ,
  #   "city": "",
  #   "state": "",
  #   "phone": "",
  #   "seeking_venue": False,
  #   "image_link": "",
  #   "past_shows": [],
  #   "upcoming_shows": [{
  #     "venue_id": 3,
  #     "venue_name": "Park Square Live Music & Coffee",
  #     "venue_image_link": "https://images.unsplash.com/photo-1485686531765-ba63b07845a7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=747&q=80",
  #     "start_time": "2035-04-01T20:00:00.000Z"
  #   }, {
  #     "venue_id": 3,
  #     "venue_name": "Park Square Live Music & Coffee",
  #     "venue_image_link": "https://images.unsplash.com/photo-1485686531765-ba63b07845a7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=747&q=80",
  #     "start_time": "2035-04-08T20:00:00.000Z"
  #   }, {
  #     "venue_id": 3,
  #     "venue_name": "Park Square Live Music & Coffee",
  #     "venue_image_link": "https://images.unsplash.com/photo-1485686531765-ba63b07845a7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=747&q=80",
  #     "start_time": "2035-04-15T20:00:00.000Z"
  #   }],
  #   "past_shows_count": 0,
  #   "upcoming_shows_count": 3,
  # }


  show given data 

  INSERT INTO show (start_time, artist_id, venue_id, upcoming)
  VALUES('2019-05-21T21:30:00.000Z','3','3','False');
  VALUES('2019-06-15T23:00:00.000Z','2','1','False');
  VALUES('2035-04-01T20:00:00.000Z','1','2','True');
  VALUES('2035-04-08T20:00:00.000Z','3','1','True');
  VALUES('2035-04-15T20:00:00.000Z','2','3','True');


  # {
  #   "venue_id": 1,
  #   "venue_name": "The Musical Hop",
  #   "artist_id": 4,
  #   "artist_name": "Guns N Petals",
  #   "artist_image_link": "https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80",
  #   "start_time": ""
  # }, {
  #   "venue_id": 3,
  #   "venue_name": "Park Square Live Music & Coffee",
  #   "artist_id": 5,
  #   "artist_name": "Matt Quevedo",
  #   "artist_image_link": "https://images.unsplash.com/photo-1495223153807-b916f75de8c5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80",
  #   "start_time": ""
  # }, {
  #   "venue_id": 3,
  #   "venue_name": "Park Square Live Music & Coffee",
  #   "artist_id": 6,
  #   "artist_name": "The Wild Sax Band",
  #   "artist_image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80",
  #   "start_time": ""
  # }, {
  #   "venue_id": 3,
  #   "venue_name": "Park Square Live Music & Coffee",
  #   "artist_id": 6,
  #   "artist_name": "The Wild Sax Band",
  #   "artist_image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80",
  #   "start_time": ""
  # }, {
  #   "venue_id": 3,
  #   "venue_name": "Park Square Live Music & Coffee",
  #   "artist_id": 6,
  #   "artist_name": "The Wild Sax Band",
  #   "artist_image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80",
  #   "start_time": ""
  # }
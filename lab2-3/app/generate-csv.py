import random


class CsvGenerator:
    file_name = 'generated.csv'
    first_name = ['Bill', 'Deny', 'Bryan', 'Oleg', 'Tirion', 'Tony', 'Johny', 'Josh', 'Jolie', 'Mary', 'Kate', 'Brett']
    last_name = ['Flesher', 'Maron', 'Callen', 'Beetz', 'Marshmello', 'Lanister', 'Stark', 'Phoenix', 'Conroy', 'Ellis']
    birthplace = ['Ukraine Kyiv Povstanska 3A', 'Ukraine Lviv Naykova 4B', 'USA New York Windmill Hill Rd 37',
                  'Japan Hiroshima Peace Boul 12', 'Netherlands Amsterdam Javastraat']
    birthdate = ['2019-01-12', '2018-01-16', '2019-02-15', '2019-03-19', '2019-05-01']
    photo = ['photo 1', 'photo 2', 'photo 3', 'photo 4', 'photo 5', 'photo 6', 'photo 7', 'photo 8']
    image = ['image 1', 'image 2', 'image 3', 'image 4', 'image 5', 'image 6', 'image 7', 'image 8']
    title = ['IT', 'Interstellar', 'The Lord of the Rings', 'Oblivion', 'Need for Speed', 'Iron Man', 'Captain America',
             'The Last Man', 'Spider-Man', 'Holston', 'The Proposal', 'Funny Story', 'Poms', 'Ma',
             'World of Warcraft', 'For the Birds', 'Booksmart']
    typeOfGenre = ['Adventure', 'Fiction', 'Fantasy', 'Science', 'Detective', 'Soap Opera', 'Drama', 'Poem', 'Horror']
    budget = ['9900$', '1500$', '19800$', '37100$', '10000$', '32800$', '50000$', '345770$', '70000$', '10000$',
              '87000$', '100000$', '99000$']
    gross = ['150000$', '3600000$', '110000$', '2250000$', '1993000$', '310000$', '500000$', '8730000$', '991300$',
             '1000010$', '1365000$', '2030000$', '870000$', '1364000$', '2300000$']
    information = ['Wrapped filming on November first.', 'Is set to cost a reported $100 million.',
                   'Halle Berry broke three ribs while filming the movie',
                   'Gabriel Iglesias was in the running to play the Genie.',
                   'Tom Hardy was rumored for the role of Jafar.', 'Millie Bobby Browns film debut.',
                   'Mothras roar in the film is a modified version of her original roar.',
                   'Charles Dance saying "Long live the King."',
                   'Taron Egerton does all of his own singing in the film.',
                   'The film is named after the 1972 song of the same name.',
                   'Robert Downey Jr. was the only cast member who was entrusted with the entire film"s script.',
                   'This film marked Chapter Ten of Phase Three in the Marvel Cinematic Universe.',
                   'Title was announced with the first trailer that was released on December 7th 2018.']
    year = ['1999', '1991', '2003', '2007', '1867', '1979', '2013', '2016', '1996', '2018', '2019']
    description = ['May the Force be with you.', 'They call me Mister Tibbs!', 'The last war is coming...',
                   'If you build it he will come.', 'Houston we have a problem.', 'The last battle...',
                   'Is it safe?', 'Hasta la vista baby.', 'Chewie we are home.', 'These go to eleven.',
                   'It was Beauty killed the Beast.', 'They are here!', 'Nobody is perfect.', 'Wax on wax off.',
                   'Elementary my dear Watson.', 'Good morning Vietnam!', 'My precious.', 'Argo f— yourself.']
    nickname = ['aligator22', 'Jonh Wick', 'Stasana', 'OoFeel', 'Likethesilence', 'KekaineKektamine',
                'Master11', 'Anrew', 'Bigfoot', 'Epicstone', 'Killer228', 'Predator', 'EvilHunter01', 'flysheep',
                'korzhik', 'Rokfor', 'Rastaboss', 'Tanos13', 'Kavo', 'memandkek', 'Movie Maker', 'ozzy']
    email = ['prokent@i.ua', 'star007@gmail.com', 'starshoping@yahoo.com', 'msrocket@gmail.com', 'nightelf11@yahoo.com',
             'blackfury@i.ua', 'bosskokos@mail.ru']
    wathlist = ['The Avengers', 'Avatar', 'The Matrix', 'Aladin', 'Harry Potter', 'Star Wars', 'The Godfather',
                'Rayman', 'Trivia', 'The Tomorrow Man', 'The Proposal',
                'UglyDolls', 'Killer', 'Oldboy', 'Leon', 'Pikachu', 'Tom Sawyer', 'The Lost', 'Polaroid', 'Shazam!']
    rating = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    comment = ['Grate movie!', 'I really liked this movie', 'It is so boring', 'Brillant', 'So cruel', 'Awesome']

    cashreport = 500
    movie = 30
    actor = 250
    user = 220

    def Cash_Report(self, file):

        file.write('\nCash Report\n')
        for i in range(1, self.cashreport + 1):
            cashreport_budget = self.budget[random.randint(0, len(self.budget) - 1)]
            cashreport_gross = self.gross[random.randint(0, len(self.gross) - 1)]
            file.write('{budget},{gross}\n'.format(budget=cashreport_budget,
                                                   gross=cashreport_gross))

    def Interesting_Facts(self, file):
        file.write('\nInteresting Facts\n')
        for information in self.information:
            file.write('{information}\n'.format(information=information))

    def Movie(self, file):

        file.write('\nMovie\n')
        for i in range(1, self.movie + 1):
            movie_title = self.title[random.randint(0, len(self.title) - 1)]
            movie_year = self.year[random.randint(0, len(self.year) - 1)]
            movie_description = self.description[random.randint(0, len(self.description) - 1)]
            cashReport_id = random.randint(1, 181)
            interestingFacts_id = random.randint(1, 13)
            # movie_image = self.image[random.randint(0, len(self.image) -1)]
            file.write('{title},{year},{description},{cashReport_id},{interestingFacts_id}\n'.format(title=movie_title,
                                                                                                     year=movie_year,
                                                                                                     description=movie_description,
                                                                                                     cashReport_id=cashReport_id,
                                                                                                     interestingFacts_id=interestingFacts_id))

    def Actor(self, file):

        file.write('\nActor\n')
        for i in range(1, self.actor + 1):
            actor_first_name = self.first_name[random.randint(0, len(self.first_name) - 1)]
            actor_last_name = self.last_name[random.randint(0, len(self.last_name) - 1)]
            actor_birthplace = self.birthplace[random.randint(0, len(self.birthplace) - 1)]
            actor_birthdate = self.birthdate[random.randint(0, len(self.birthdate) - 1)]
            actor_photo = self.photo[random.randint(0, len(self.photo) - 1)]
            file.write('{first_name},{last_name},{birhplace},{birthdate},{photo}\n'.format(first_name=actor_first_name,
                                                                                           last_name=actor_last_name,
                                                                                           birhplace=actor_birthplace,
                                                                                           birthdate=actor_birthdate,
                                                                                           photo=actor_photo))

    def User(self, file):

        file.write('\nUser\n')
        for i in range(1, self.user + 1):
            user_nickname = self.nickname[random.randint(0, len(self.nickname) - 1)]
            user_birthdate = self.birthdate[random.randint(0, len(self.birthdate) - 1)]
            user_email = self.email[random.randint(0, len(self.email) - 1)]
            user_wathlist = self.wathlist[random.randint(0, len(self.wathlist) - 1)]
            user_photo = self.photo[random.randint(0, len(self.photo) - 1)]
            movie_id = random.randint(1, 30)
            file.write('{nickname},{birthdate},'
                       '{email},{watchlist},{photo},{movie_id}\n'.format(nickname=user_nickname,
                                                                         birthdate=user_birthdate,
                                                                         email=user_email,
                                                                         watchlist=user_wathlist,
                                                                         photo=user_photo,
                                                                         movie_id=movie_id))

    def Genre(self, file):

        file.write('\nGenre\n')
        for typeOfGenre in self.typeOfGenre:
            file.write('{type_of_genre}\n'.format(type_of_genre=typeOfGenre))

    def Rating(self, file):
        file.write('\nRating\n')
        for rating in range(1, self.user + 1):
            rating = self.rating[random.randint(0, len(self.rating) - 1)]
            user_id = random.randint(1, 219)
            file.write('{rating}, {user_id}\n'.format(rating=rating,
                                                      user_id=user_id))

    def Comment(self, file):
        file.write('\nComment\n')
        for i in range(1, self.user + 1):
            comment = self.comment[random.randint(0, len(self.comment) - 1)]
            user_id = random.randint(1, 219)
            file.write('{comment}, {user_id}\n'.format(comment=comment,
                                                       user_id=user_id))

    def generate_csv(self):
        """
        Generate csv file

        :return:
        """
        with open(self.file_name, 'w') as file:
            self.Cash_Report(file)
            self.Interesting_Facts(file)
            self.Movie(file)
            self.Actor(file)
            self.User(file)
            self.Genre(file)
            self.Rating(file)
            self.Comment(file)


if __name__ == '__main__':
    try:
        csv_generator = CsvGenerator()
        csv_generator.generate_csv()
        print("File successfully generated")
    except:
        print("Error")

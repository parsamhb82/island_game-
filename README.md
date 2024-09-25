# island_game-project documentation
simple island and bottle game implemented using django and rest framework is django-based web platform that allows users to play a simple game. The game involves navigating a virtual island, collecting bottles, and buying things from shop . The platform provides a user-friendly interface and includes features such as user registration, login, and game progress tracking.

#### Core Functionality
1. **Registration and Login**: Users can create accounts and log in to access the game at first a random x and y coordinates are generated for the user's island.
2. **Buying bottles**: users can buy bottles from the shop and each has different prices and each has different max chars and max radius

3. **Gameplay**: The game involves navigating a virtual island, collecting bottles, and buying things from shop and sending bottles to other players each bottle is send randomly to a player in the bottles radius by and by recieving bottles the players score increases and the players score is displayed on the screen.

4. **Score Tracking**: The platform keeps track of users' scores and provides a leaderboard to display the top players.

5. **User Authentication**: Access to the application is controlled through user authentication, utilizing Django’s authentication framework. Users must log in to access the platform's features.



#### Technical Details

- **Framework**: Developed using Django, a robust web framework for building scalable web applications.
- **Database**: Uses PostgreSQL for reliable and scalable data storage.
- **Authentication**: Implements Django’s authentication system with JWT-based token management for secure user access.
- **Permissions**: Incorporates custom permissions for superuser and for players.


#### Prerequisites
- Python 3.x
- Django 5.x
- PostgreSQL
- psycopg2
- others in requirements.txt

#### Installation and Setup

**Manual Installation**
1. Clone the repository:
    ```
    git clone https://github.com/username/project-name.git
    ```
2. Navigate to the project directory:
    ```
    cd project-name
    ```
3. Create a virtual environment and install dependencies:
    ```
    python -m venv env
    source env/bin/activate
    pip install -r requirements.txt
    ```
4. Configure the database and run migrations:
    ```
    python manage.py migrate
    ```
5. Start the development server:
    ```
    python manage.py runserver
    ```

---

### Usage

1. **Access the Admin Panel**:
   - Navigate to `http://localhost:8000/admin` to manage deliveries, users, and other data.

2. **Create a Superuser**:
   ```
   python manage.py createsuperuser
   ```

### End-Points

1. **Register**:
   - **Endpoint**: `/user/register/`
2. **Login**:
   - **Endpoint**: `/user/login/`
3. **refresh**:
   - **Endpoint**: `/user/refresh/`
4. **scoreboard**:
   - **Endpoint**: `/user/scoreboard/`
5. **sendbottle**:
   - **Endpoint**: `/bottle/send-bottle/`
6. **readsentbottle**:
   - **Endpoint**: `/bottle/read-sent-bottle/`
7. **viewavailablebotte**
   - **Endpoint**: `/bottle/view-available-bottles/`
8. **buybottle**:
   - **Endpoint**: `/bottle/buy-bottle/`
9. **viewabblitiestobuy**:
   - **Endpoint**: `/bottle/view-abilities-tobuy/`
10. **buyreplyabbility**:
   - **Endpoint**: `/bottle/buy-ability-to-reply/`
11. **buyabilitytoreadmore**:
   - **Endpoint**: `/bottle/buy-ability-to-read-more/`
12. **replytobottle**:
   - **Endpoint**: `/bottle/reply-to-bottle/`
13. **fillthemap**:
   - **Endpoint**: `/user/fill-the-map/`

### Data-Base AND Stuff
for making new bottles to buy you have to creat them in admin panel and make them available to buy for players the model is ToBuyBottle create some in and put them in DB. dont use fill-the-map when you run the game in real life  

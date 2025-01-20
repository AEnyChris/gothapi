# gothapi
An API for Game of Thrones

This is an open API that provides data about the GOT Universe based on the TV series _Game of Thrones_ with an hope of expansion to cover _House of Dragons_ by HBO in subsequent versions.
The currently available resources, schema and the associated endpoints are described below.



### Authentication:
The API is an open API, hence no authentication is required. Consequently, the request method is restricted only to GET.

### Structure:

Resources:
The following are the resources covered:

- <strong>People</strong>: Characters as portrayed in the GOT and HOD series
- <strong>Houses</strong>: The ruling houses in Westeros
- <strong>Places</strong>: the places, the Countries, the house 
- <strong>Dragons</strong>: the dragons of Game of Thrones and House of Dragons
- <strong>Seasons</strong>: the seasons of Game of Thrones
- <strong>Episodes</strong>: The episodes of all seasons

### Endpoints:

_Base URL_: 

        https://www.gothapi.com/api/ or 
        http://localhost:8000/api/

	
_Root_:

		https://www.gothapi.com/ or
        http://localhost:8000/
    
The root API gives the details of all available resources in the database.
Using httpie to output is given as below:

    HTTP/1.1 200 OK
    Allow: GET, HEAD, OPTIONS
    Content-Length: 303
    Content-Type: application/json
    Cross-Origin-Opener-Policy: same-origin
    Date: Sun, 19 Jan 2025 23:23:06 GMT
    Referrer-Policy: same-origin
    Server: WSGIServer/0.2 CPython/3.11.3
    Vary: Accept, Cookie
    X-Content-Type-Options: nosniff
    X-Frame-Options: DENY

    {
        "api/dragons": "http://localhost:8000/api/dragons/",
        "api/episodes": "http://localhost:8000/api/episodes/",
        "api/houses": "http://localhost:8000/api/houses/",
        "api/people": "http://localhost:8000/api/people/",
        "api/places": "http://localhost:8000/api/places/",
        "api/seasons": "http://localhost:8000/api/seasons/"
    }

_Stats_:

		https://www.gothapi.com/api/stats
The stats endpoint gives the statistics of all available resources: the resources and the number of each in the database at the time. The GOT Universe is vast, and all the data according to the series or books may not be available when this API goes live. However, more data will be continually added until we have traversed all of Westeros, Essos, Bravos, and beyond the known world (if Arya Stark does not beat us to it 🙂).

People:

	https://www.gothapi.com/api/people - get all the people assets available
	https://www.gothapi.com/api/people/<id> - get a specific people asset by id
	https://www.gothapi.com/api/people/<name> -get a specific people asset by name

Houses:

	https://www.gothapi.com/api/houses - get the houses available
	https://www.gothapi.com/api/houses/<id> get specific houses by id
	https://www.gothapi.com/api/houses/<name> get a specific house by name

Places:

	https://www.gothapi.com/api/places - get all the place assets 
	https://www.gothapi.com/api/places/<id> - get specific place asset
	https://www.gothapi.com/api/places/<name>

Dragons:

	https://www.gothapi.com/api/dragons - get all the dragons asset
	https://www.gothapi.com/api/dragons/<id> - get specific dragon asset by id
	https://www.gothapi.com/api/dragons/<name>
	
Seasons:

	https://www.gothapi.com/api/seasons - get all the seasons
	https://www.gothapi.com/api/seasons/<number> - get specific season

Episodes

	https://www.gothapi.com/api/seasons/episode - get all episodes of a season
	https://www.gothapi.com/api/season/episode/<number> get specific episode of a season

### Schema:
People:

	name: - string the name of the character
    titles: - list positions and titles held an empty list if such had no title
    aliases: - list	nicknames and other names the character is known by
    gender: string The gender of the character, male or female
	played_by: - string link to a Wikipedia page of actor if available
	house: - string the URL of a house the character belongs to
	culture: - string
	birth_place: - string the URL of the place asset where the character is born
	parents: - list a list of URLs of people resource. Empty if parents are unknown
	siblings: - list a list of URLs of people resource. Empty if siblings are unknown
    death: - string about the death of character, how, who, where and when
    episodes: - list - URLs of episodes resources the character appears. 
	created_at: time the asset was created
	updated_at; time the asset was updated

Houses:

	name: - string name of the house
	sigil: - string description of the sigil of the house
    heads: -list a list of the names of people who have headed the house as seen in the TV series
    members: - list a list of URLs of people who are members of the house
    titles: - list  A list of titles given to the lord of the house
	culture: - string The culture of the people as depicted e.g Dothraki
	motto: - string A saying of the house 
	seat: - string the castle or palace of the house
	founder: - string the originator of the house as mentioned
	created_at: string time the asset was created
	updated_at: - string time the asset was updated

Places:

	name: - string name of the place
	description: - string a brief detail about the place
	region: - string of the main regions Westeros, Essos, Bravos
	area: - string the area in the region e.g North, South, Beyond the wall e.tc
	controlled_by: - string the house the place is controlled by
	events: - string notable events surrounding that place as in the series
	created_at: time the resource was created
	updated_at; time the resource was updated

Dragons:

	name: - string name of the dragon
	original_rider: - string URL of the character to whom the dragon belongs
	riders: - list a list of URLs of characters that ever rode dragon
	colour: - string the colour of the dragon
	size: - string a relative description of the size not a specific dimensions
	facts: - string some notable facts about the dragon
	death: - string how the dragon died
    created_at: time the asset was created
	updated_at; time the asset was updated

Seasons:

	number: int an integer number of the season
	num_of_episodes: int the number of episodes in the season
	episodes: - list a list of URLs of episodes
	premiered: - int Year of its play
	show_period: string the period the season ran for
	budget: int budget in making the season
	rating: int Rotten Tomatoes rating of the season
    created_at: time the asset was created
	updated_at; time the asset was updated

Episodes:

	title: string title of the episode
	season: string the season the episode belongs to
	num_in_season: - int number of the episode in the season
	num_overall: - int  number of the episode in all the seasons
	director: - string the name of the director for that episode
	written_by: - string comma-separated names of writers
	original_air_data: date object the date the episode was originally broadcasted
	synopsis: - string a brief summary of the episode plot
    created_at: time the asset was created
	updated_at; time the asset was updated

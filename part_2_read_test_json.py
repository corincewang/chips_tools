import test_data
import json

#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json( json_data ):
    #Initialize a new GameLibrary
    game_library = test_data.GameLibrary()

    ### Begin Add Code Here ###
    #Loop through the json_data
        #Create a new Game object from the json_data by reading
        #  title
        #  year
        #  platform (which requires reading name and launch_year)
        #Add that Game object to the game_library
    ### End Add Code Here ###
    for game in json_data['games']:
        title = game['title']
        year = game['year']
        
        platform_name = game['platform']['name']
        platform_launch_year = game['platform']['launch_year']
        platform = test_data.Platform(name=platform_name, launch_year=platform_launch_year)
        
        game_object = test_data.Game(title=title, platform=platform, year=year)
        
        game_library.add_game(game_object)
    return game_library


#Part 2
input_json_file = "data/test_data.json"

### Begin Add Code Here ###
#Open the file specified by input_json_file
#Use the json module to load the data from the file
#Use make_game_library_from_json(json_data) to convert the data to GameLibrary data
#Print out the resulting GameLibrary data using print()
### End Add Code Here ###
with open(input_json_file, 'r') as file:
    json_data = json.load(file)
    game_library = make_game_library_from_json(json_data)
print(game_library)
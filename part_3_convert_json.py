import json
import cc_dat_utils  # Assuming you have the write_cc_level_pack_to_dat function here
from cc_classes import CCLevelPack, CCLevel, CCMapTitleField, CCEncodedPasswordField, CCMapHintField, CCMonsterMovementField, CCTrapControlsField, CCCloningMachineControlsField, CCTrapControl, CCCoordinate, CCCloningMachineControl

# Load JSON data from file
def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Convert JSON data to CCLevelPack
def create_cc_level_pack(json_data):
    level_pack = CCLevelPack()
    
    for level_data in json_data['level_pack']['levels']:
        level = CCLevel()
        level.level_number = level_data['level_number']
        level.time = level_data['time_limit']
        level.num_chips = level_data['num_chips']
        level.upper_layer = level_data['upper_layer']
        level.lower_layer = level_data['lower_layer']
        
        for field_data in level_data['optional_fields']:
            if field_data['type'] == 3:
                field = CCMapTitleField(field_data['title'])
            elif field_data['type'] == 6:
                field = CCEncodedPasswordField(field_data['password'])
            elif field_data['type'] == 7:
                field = CCMapHintField(field_data['hint'])
            elif field_data['type'] == 10:
                monsters = [CCCoordinate(monster['x'], monster['y']) for monster in field_data['monsters']]
                field = CCMonsterMovementField(monsters)
            elif field_data['type'] == 4:
                traps = [CCTrapControl(trap['button_coord']['x'], trap['button_coord']['y'], trap['trap_coord']['x'], trap['trap_coord']['y']) for trap in field_data['traps']]
                field = CCTrapControlsField(traps)
            elif field_data['type'] == 5:
                machines = [CCCloningMachineControl(machine['button_coord']['x'], machine['button_coord']['y'], machine['machine_coord']['x'], machine['machine_coord']['y']) for machine in field_data['machines']]
                field = CCCloningMachineControlsField(machines)
            level.add_field(field)
        
        level_pack.add_level(level)
    
    return level_pack

# Main program
input_json_file = "data/hanwang3_cc1.json"  # Input JSON file path

# Load the JSON data
with open(input_json_file, 'r') as file:
    json_data = json.load(file)

# Convert JSON data to CCLevelPack
cc_level_pack = create_cc_level_pack(json_data)

with open("data/hanwang3_cc1.txt", "w") as output_file:
    output_file.write(str(cc_level_pack))
    
    
# Save the CCLevelPack object as a DAT file using the existing function from cc_dat_utils
output_dat_file = "data/hanwang3_cc18.dat"
cc_dat_utils.write_cc_level_pack_to_dat(cc_level_pack, output_dat_file)

# Print confirmation message
print(f"DAT file saved to {output_dat_file}")

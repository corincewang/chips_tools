import cc_dat_utils

# Part 1: Load the DAT file and print its string representation
input_dat_file = "data/pfgd_test.dat"

# Use cc_dat_utils.make_cc_level_pack_from_dat() to load the file specified by input_dat_file
level_pack = cc_dat_utils.make_cc_level_pack_from_dat(input_dat_file)

# Print the string representation of the level_pack
print(str(level_pack))

# Save the output to a text file in the data folder
with open("data/pfgd_test.txt", "w") as output_file:
    output_file.write(str(level_pack))

# You would need to manually load the pfgd_test.dat file in TileWorld and take a screenshot at this point.
# After taking the screenshot, save it as pfgd_test_screenshot.png or .jpg in the data folder.

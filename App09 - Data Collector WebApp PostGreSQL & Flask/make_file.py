def make_file(height, avg_height, count):
    if count != 1:
        message = "Hey there, your height is {} cm.\nAverage height of all is {} cm and that is calculated out of {} people.\nThank you.".format(height, avg_height, count)
    else:
        message = "Hey there, your height is {} cm.\nAverage height of all is {} cm and that is calculated out of {} person.\nThank you.".format(height, avg_height, count)
    with open("height_data.txt", 'a') as file:
        file.truncate(0)
        file.write(message)
    return file
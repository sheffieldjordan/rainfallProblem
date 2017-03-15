def average_rainfall():
	rain_data = [] 
	with open("rainfall.txt", "r") as file_handle:
		raw_data = file_handle.readlines()	
	
	# print(raw_data)
	for i in range(len(raw_data)): # removes all parts of a string after the delimiter, " " or "\n". 
		raw_data[i] = raw_data[i].split(" ")[0] # this ensures entries like "2 100" are inputted as only "2"
		raw_data[i] = raw_data[i].split("\n")[0] 
	
	for i in raw_data:
		if i == '-999': 
			break # stops reading the raw data once it gets to -999
		if i.isdigit():
			rain_data.append(int(i)) # adds positive integers to the list
		if i.strip('0123456789') == '.':
			rain_data.append(float(i)) # adds floats to the list			
		if i.strip('0123456789') == ',': #handles the case of someone accidentally entering 1,000 instead of 10000.
			rain_data.append(int(i.replace(',', '')))
			
	try:
		sum(rain_data) / float(len(rain_data)) # exception handling for invalid inputs
	except:
		return "There are no valid rainfall inputs" 
	# print(rain_data)
	average_rainfall = sum(rain_data) / len(rain_data) # calculates average rainfall
	if average_rainfall.is_integer(): # ensures the average displays as an integer, if it's an integer
		average_rainfall = int(average_rainfall) 
	
	return "Average rainfall = {} inches".format(average_rainfall)

def main(): #boilerplate code
	print(average_rainfall())

if __name__ == "__main__":
	main() 
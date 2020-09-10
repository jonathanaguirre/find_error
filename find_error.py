# The purpose of this script is to search a log file for by input and then output
# the error into a seperate file
#!/usr/bin/env python3
import sys
import os
import re
# The error_search function will take a log_file as a parameter and return returned_errors
def error_search(log_file):
	error = input("what is the error foudn in the log file? The error should be in all CAPS ")
	returned_errors = []
	# All error logs are now enlisted, now reading the file encoded as UFT-8
	with open(log_file, mode='r',encoding='UTF-8') as file:
		for log in file.readlines():
			# Error can be changed to INFO and WARN if required. Can also be empty to 
			# initilize all types of logs
			error_patterns = ["error"]
			for i in range(len(error.split(' '))):
				error_patterns.append(r"{}".format(error.split(' ')[i].lower()))
			# Checks log file for user defined pattern and if found, append them to the list named
			# returned _errors.
			if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
				returned_errors.append(log)
		file.close()
	return returned_errors

def file_output(returned_errors):
	# Write returned_erros into errors_found.log by opening file in writing mode. ~ will return
	# the home diarectory of your system.
	with open(os.path.expanduser('~') + '/save_errorlogs_here/errors_found.log', 'w') as file:
		for error in returned_errors:
			file.write(error)
		file.close()
# Both functions will be called. Call the first function error_search() and pass log_file to 
# function. Then call the second function file_output and pass returned_errors as a parameter.
if __name__ == "__main__":
	log_file	 = sys.argv[1]
	returned_errors = error_search(log_file)
	file_output(returned_errors)
	sys.exit(0)
# Date Wanted (XX-XX-XXXX // always add a 0 if single digit (e.g. 01, 02, 03))
MONTH = '03'
DAY = '20'
YEAR = '2023'

# How many in your party? (2-4)
# PLAYER_COUNT cannot be 1 or the code will crash
PLAYER_COUNT = 4

# Uses Standard Time (7:00AM - 6:52PM - make sure time is identical to the tee time list below)
WANTED_TIME = '7:00AM'

# User Credentials for San Jose Muni website
USER_NAME = 'markcuasay@gmail.com'
PASSWORD = 'Golf408$'


# Do not touch anything below this line
# Adjust date
DATE = YEAR + MONTH + DAY

# Format URL
FULL_URL = f'https://sanjosemuni.quick18.com/teetimes/searchmatrix?teedate={DATE}'

tee_time_list = ['7:00AM', '7:07AM', '7:15AM', '7:22AM', '7:30AM', '7:37AM', '7:45AM', '7:52AM',
                 '8:00AM', '8:07AM', '8:15AM', '8:22AM', '8:30AM', '8:37AM', '8:45AM', '8:52AM',
                 '9:00AM', '9:07AM', '9:15AM', '9:22AM', '9:30AM', '9:37AM', '9:45AM', '9:52AM',
                 '10:00AM', '10:07AM', '10:15AM', '10:22AM', '10:30AM', '10:37AM', '10:45AM', '10:52AM',
                 '11:00AM', '11:07AM', '11:15AM', '11:22AM', '11:30AM', '11:37AM', '11:45AM', '11:52AM',
                 '12:00PM', '12:07PM', '12:15PM', '12:22PM', '12:30PM', '12:37PM', '12:45PM', '12:52PM',
                 '1:00PM', '1:07PM', '1:15PM', '1:22PM', '1:30PM', '1:37PM', '1:45PM', '1:52PM',
                 '2:00PM', '2:07PM', '2:15PM', '2:22PM', '2:30PM', '2:37PM', '2:45PM', '2:52PM',
                 '3:00PM', '3:07PM', '3:15PM', '3:22PM', '3:30PM', '3:37PM', '3:45PM', '3:52PM',
                 '4:00PM', '4:07PM', '4:15PM', '4:22PM', '4:30PM', '4:37PM', '4:45PM', '4:52PM',
                 '5:00PM', '5:07PM', '5:07PM', '5:22PM', '5:30PM', '5:37PM', '5:45PM', '5:52PM',
                 '6:00PM', '6:07PM', '6:15PM', '6:22PM', '6:30PM', '6:37PM', '6:45PM', '6:52PM']

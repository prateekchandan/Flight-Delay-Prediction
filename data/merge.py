import sys
import csv
from sets import Set
import logging
import time

plm = ""
toolbar_width = 40

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def time_diff(a, b):
    mina = (a/100)*60 + (a%100)
    minb = (b/100)*60 + (b%100)
    return abs(mina-minb)

if len(sys.argv) < 2:
    message = bcolors.BOLD + "Usage: python merge.py <year>" + bcolors.ENDC
    sys.exit(message)

input_year = sys.argv[1]

if int(input_year) < 1997 or int(input_year) > 2006:
    message = bcolors.FAIL + "Error: year should be in [1997, 2006]" + bcolors.ENDC
    sys.exit(message)



logfile = input_year + 'log.log'
logging.basicConfig(filename=logfile, level=logging.DEBUG)

airline_file_name = 'airline_data/' + input_year + '.csv'

merged_file_name = 'merged' + input_year + '.csv'
merged_file = open(merged_file_name, 'wb')

try:
    airline_file = open(airline_file_name, 'r')
except:
    message = bcolors.FAIL + "airline data file " + airline_file_name + " does not exist" + bcolors.ENDC
    sys.exit(message)

merged_file_writer = csv.writer(merged_file)

wban_code = {}
weather_data = {}

def progress_string(reps):
    s = ""
    for i in range(0, reps):
        s += '-'
    return s

def toolbar_init(message):
    # setup toolbar
    sys.stdout.write("%s: [%s]" % (message, " " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

def make_progress(toolbar_accum, prev_toolbar_accum):
    sys.stdout.write("\b" * (prev_toolbar_accum)) # return to start of line, after '['
    sys.stdout.write(progress_string(int(toolbar_accum)))
    sys.stdout.flush()


toolbar_init("Building wban map")
toolbar_accum = 0
prev_toolbar_accum = 0
for i in range(1, 12):
    time.sleep(0.1)
    toolbar_accum += toolbar_width*1.0/12
    make_progress(toolbar_accum, prev_toolbar_accum)
    prev_toolbar_accum = int(toolbar_accum)
    
    path = 'weather/' + input_year
    num = str(i)
    if(i < 10):
        num = '0' + num
    map_file_name = path + num + '/station.txt'

    try:
        map_file = open(map_file_name)
    except:
        message = bcolors.FAIL + map_file_name + " does not exist" + bcolors.ENDC
        sys.exit(message)

    lines = map_file.readlines()
    for i in range(1, len(lines)):
        items = lines[i].split('|')
        wban_code[items[2]] = int(items[0])
    map_file.close()
    
make_progress(toolbar_width, prev_toolbar_accum)
prev_toolbar_accum = 0
sys.stdout.write("\n")


mpfile = open('mapfile.txt', 'w')
mpfile.write(str(wban_code))
mpfile.close()

airline_lines = airline_file.read().splitlines()
airline_file.close()

header = airline_lines[0].split(',')
done = False

start = 1
num_items_processed = 0
for i in range(1, 13):

    weather_data = {}

    for key, value in wban_code.iteritems():
        weather_data[value] = {}
    
    path = 'weather/' + input_year
    num = str(i)
    if(i < 10):
        num = '0' + num

    hourly_file_name = path + num + '/' + input_year + num + 'hourly.txt'
    try:
        hourly_file = open(hourly_file_name)
    except:
        message = bcolors.FAIL + "Hourly file " + path + " does not exist" + bcolors.ENDC
        sys.exit(message)

    toolbar_init("Processing for " + hourly_file_name)
    #print("Processing: ", hourly_file_name)
    toolbar_accum = 0
    prev_toolbar_accum = 0

    lines = hourly_file.read().splitlines()
    hourly_file.close()
    
    headings = lines[0].split(',')

    cnt = 0
    for item in headings:
        if cnt < 2:
            cnt+=1
            continue
        header.append("source " + item)

    cnt = 0
    for item in headings:
        if cnt < 2:
            cnt+=1
            continue
        header.append("dest " + item)
    if not(done):
        merged_file_writer.writerow(header)
        done = True
    
    for j in range(1, len(lines)):
        items = lines[j].split(',')
        #print items[2:]
        try:
            date = int(items[1])
            wban = int(items[0])
        except:
            message = "Date/wban invalid in hourly file"
            if message != plm:
                logging.debug(message)
            plm = message
            continue
        #print date, wban
        try:
            if date in weather_data[wban]:
                weather_data[wban][date].append(items[2:])
            else:
                weather_data[wban][date] = [items[2:]]
        except:
            message = "wban: " + str(wban) + " not in wban_code map"
            if message != plm:
                logging.error(message)
            plm = message
            continue

    
        #print weather_data[wban]

    for k in range(start, len(airline_lines)):

        toolbar_accum += toolbar_width*12.0/len(airline_lines)
        make_progress(toolbar_accum, prev_toolbar_accum)
        prev_toolbar_accum = int(toolbar_accum)
        
        items = airline_lines[k].split(',')
        year = items[0]
        month = items[1]
        day = items[2]
        if (int(month) != i):
            break
        num_items_processed += 1
        origin = items[16]
        dest = items[17]

        if int(month) < 10:
            month = '0' + month
        if int(day) < 10:
            day = '0' + day
            
        date_stamp = year + month + day
        date_stamp = int(date_stamp)
        #print origin, dest, origin_wban, date_stamp

        try:
            origin_wban = wban_code[origin]
        except:
            message = "wban not available for " + origin + "/" + dest
            if message != plm:
                logging.error(message)
            plm = message
            continue
        
        try:
            l = weather_data[origin_wban][date_stamp]
        except:
            message = "Weather data not available for " + str(origin_wban)
            if message != plm:
                logging.error(message)
            plm = message
            continue
        
        least_diff = 1000000
        closest = []
        for lst in l:
            try:
                if time_diff(int(lst[0]), int(items[5])) < least_diff:
                    least_diff = abs(int(lst[0]) - int(items[5]))
                    closest = lst
            except:
                message = "conversion to int weather file: " + lst[0] + " ,airline file: " + items[5]
                if message != plm:
                     logging.error(message)
                plm = message
                continue

        try:
            items.extend(closest)
        except:
            message = "Error while extending list"
            if message != plm:
                logging.error(message)
            plm = message
            continue

        try:
            dest_wban = wban_code[dest]
        except:
            message = "wban not available for " + dest + "/" + dest
            if message != plm:
                logging.error(message)
            plm = message
            continue
        
        try:
            l = weather_data[dest_wban][date_stamp]
        except:
            message = "Weather data not available for " + str(dest_wban)
            if message != plm:
                logging.error(message)
            plm = message
            continue
        
        least_diff = 10000
        closest = []
        for lst in l:
            try:
                if time_diff(int(lst[0]) - int(items[5])) < least_diff:
                    least_diff = abs(int(lst[0]) - int(items[5]))
                    closest = lst
            except:
                message = "conversion to int weather file: " + lst[0] + " ,airline file: " + items[5]
                if message != plm:
                     logging.error(message)
                plm = message
                continue

        try:
            items.extend(closest)
        except:
            message = "Error while extending list"
            if message != plm:
                logging.error(message)
            plm = message
            continue
                
        
        merged_file_writer.writerow(items)
    make_progress(toolbar_width, prev_toolbar_accum)
    sys.stdout.write('\n')

    print("total items processed till now: ", num_items_processed)
    start = num_items_processed+1

merged_file.close()

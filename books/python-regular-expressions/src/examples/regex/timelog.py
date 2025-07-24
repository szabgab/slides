import sys


if len(sys.argv) < 2:
   exit("Usage: {} FILENAME".format(sys.argv[0]))



data = {}

def read_file(filename):
   entries = []
   with open(filename) as fh:
       for row in fh:
           row = row.rstrip("\n")
           if row == '':
               process_day(entries)
               entries = []
               continue
           #print(row)
           time, title = row.split(" ", 1)
           #print(time)
           #print(title)
           #print('')

           entries.append({
               'start': time,
               'title': title,
           })
       process_day(entries)

def process_day(entries):
   for i in range(len(entries)-1):
       start = entries[i]['start']
       title = entries[i]['title']
       end   = entries[i+1]['start']
       print("{}-{} {}".format(start, end, title))

       # manual way to parse timestamp and calculate elapsed time
       # as we have not learned to use the datetim module yet
       start_hour, start_min = start.split(':')
       end_hour, end_min = end.split(':')
       start_in_min = 60*int(start_hour) + int(start_min)
       end_in_min = 60*int(end_hour) + int(end_min)
       elapsed_time = end_in_min - start_in_min
       #print(elapsed_time)

       if title not in data:
           data[title] = 0
       data[title] += elapsed_time


   print('')

def print_summary():
   total = 0
   for val in data.values():
       total += val

   for key in sorted( data.keys() ):
       print("{:20}     {:4} minutes  {:3}%".format(key, data[key], int(100 * data[key]/total)))


read_file( sys.argv[1] )
print_summary()



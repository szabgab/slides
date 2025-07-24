import sys

def process(filename):
   snmps = []
   with open(filename) as fh:
       for row in fh:
           snmps.append({
               'orig': row.rstrip(),
           })
   #print(snmps)

   max_number_of_parts = 0
   max_number_of_digits = 0
   for snmp in snmps:
       snmp['split'] = snmp['orig'].split('.')
       max_number_of_parts  = max(max_number_of_parts, len(snmp['split']))
       for part in snmp['split']:
           max_number_of_digits = max(max_number_of_digits, len(part))

   padding = "{:0" + str(max_number_of_digits)  +  "}"
   #print(padding)
   for snmp in snmps:
       padded = []
       padded_split = snmp['split'] + ['0'] * (max_number_of_parts - len(snmp['split']))

       for part in padded_split:
           padded.append(padding.format( int(part)))
       snmp['padded'] = padded
       snmp['joined'] = '.'.join(padded)


   #print(snmps)
   #print(max_number_of_parts)
   #print(max_number_of_digits)

   snmps.sort(key = lambda e: e['joined'])
   sorted_snmps = []
   for snmp in snmps:
       sorted_snmps.append( snmp['orig'] )
   for snmp in sorted_snmps:
      print(snmp)

# get the max number of all the snmp parts
# make each snmp the same length
# pad each part to that length with leading 0s

if len(sys.argv) < 2:
   exit("Usage: {} FILENAME".format(sys.argv[0]))
process(sys.argv[1])


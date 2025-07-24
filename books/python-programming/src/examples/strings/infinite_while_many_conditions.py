
while True:
   line = get_next_line()

   if last_line:
       break

   if line is empty:
      continue

   if line_has_a_hash: # at the  beginning:
      continue

   if line_has_two_slashes: // at the beginning:
      continue

   do_the_real_stuff()

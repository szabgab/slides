
while True:
   line = get_next_line()
   
   if last_line:
       break
   
   if line_is_empty:
      continue

   if line_has_an_hash_at_the_beginning: # #
      continue

   if line_has_two_slashes_at_the_beginning: # //
      continue

   do_the_real_stuff

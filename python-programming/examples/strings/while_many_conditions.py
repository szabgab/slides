while (not found_error) and (not found_warning) and (not found_exit):
    do_the_real_stuff()

while True:
    line = get_next_line()

    if found_error:
        break

    if found_warning:
        break

    if found_exit:
        break

    do_the_real_stuff()

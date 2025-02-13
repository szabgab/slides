
machine_is_on = False
print(machine_is_on)   # False

# Instead of this:

if machine_is_on:
    machine_is_on = False
else:
    machine_is_on = True

# Write this:

machine_is_on = not machine_is_on
print(machine_is_on)   # True

machine_is_on = not machine_is_on
print(machine_is_on)   # False


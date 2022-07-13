def format_name(f_name, l_name):
  """Takes a first and last name, and formats it to return the title case version of the name."""
  formatedFname = f_name.title()
  formatedLname = l_name.title()
  return f"{formatedFname} {formatedLname}"


print(format_name("rocio", "suarez galan"))


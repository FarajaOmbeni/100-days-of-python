def format_name(fname: str, lname: str):
    """Returns a name in title case"""
    fname = fname.title()
    lname = lname.title() 
    return f"{fname} {lname}"

ben = format_name("ombeni", "faraja")
print(ben)
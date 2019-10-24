
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}           # key value pair

print(monthConversions["Jan"])
print(monthConversions.get("RR"))       # default = None
print(monthConversions.get("KK", "Not found!"))

from collections import namedtuple

nmdTpl = namedtuple("Players", "plyname age sport ctry")
plyr = nmdTpl(plyname="Sachin", age=34, sport='Cricket', ctry="India")
print(f"Name    :{plyr.plyname}")
print(f"Age     :{plyr.age}")
print(f"Sport   :{plyr.sport}")
print(F"Country :{plyr.ctry}")
plyr.plyname = "Rohi35"

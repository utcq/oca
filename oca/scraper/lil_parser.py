def parse_desc(desc:str)->dict:
    res = {
        "urls": [],
        "hosts": []
    }

    lindex = 0
    while True:
        lindex = desc.find("(", lindex)
        if lindex >= 0:
            end=desc.find(")", lindex)
            res["urls"].append(
                desc[lindex+1:][:end][:-1]
            )
            lindex=end
        else:
            break
    
    regex_pattern = r"nc [a-zA-Z0-9\-_]+(?:\.challs\.olicyber\.it) \d+"
    matches=re.findall(regex_pattern, desc, re.MULTILINE | re.DOTALL)
    
    for match in matches:
        res["hosts"].append(
            tuple(match.split("nc ")[1].split(" "))
        )

    return res

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
    
    hindex = 0
    while True:
        hindex = desc.find("`", hindex)
        if hindex >= 0:
            end=desc.find("`", hindex+1)
            res["hosts"].append(
                tuple(desc[hindex+1:][:end][:-1].split('nc ')[1].split(" "))
            )
            hindex=end+1
        else:
            break
    return res
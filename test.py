def download_attachment(url):
    pass

def extract_attributes(data_str,url):

    attributes = {}
    attr_list = data_str.strip("~~~~").split("~~~~")
    attributes["URL"] =url
    for attr in attr_list:
        _d = attr.split(":")
        if not _d[0] in attributes.keys():
            _key=_d[0].strip()
            _val=_d[1].strip()


            print("_key",_key,"_val",_val)
            if _key == "Dates":
                _dt = _val.split("      ")
                attributes[_key] =_dt[0].strip()
            elif _key =="Contact Name & Title":
                _cnt=_val.split(",")
                attributes["Contact Name"] =_cnt[0].strip()
                attributes["Title"] =_cnt[1].strip()
            elif _key.startswith("City"):
                _keys = _key.split(" / ")
                _vals = _val.split(" / ")
                for i in range(len(_keys)):
                    attributes[_keys[i].strip()] = _vals[i].strip()
            else:
                attributes[_key] =_val

    return attributes 
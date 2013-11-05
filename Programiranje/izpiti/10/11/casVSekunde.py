cas = "11:15:12"
def cas_v_sekunde(cas):
    h,m,s = cas.split(":")
    return int(h)*3600 + int(m)*60 + int(s)



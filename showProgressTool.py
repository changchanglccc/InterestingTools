# Shows progress of a certain operation in percentage
def update_progress(progress, total):
    print('\r[{0}] {1}%'.format('#'*int((progress*30)/total), math.ceil(progress*100/total)), end="", flush=True)


##collect from Caio, thanks~
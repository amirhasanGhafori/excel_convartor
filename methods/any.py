import numpy as np
import re

def check_permission_worker(data):
    list_permission = ['تحلیلگر','معاونت','مهندس فنی','کارگردان']
    if data in list_permission:
        return 'کاربر مجاز' + list_permission[list_permission.index(data)]
    else:
        return ''
    


def check_location_worker(loc,location):
    converStr = str(loc)
    res = converStr.split('+')
    result = location[location['استان'] == res[-1].strip()]
    print(result)
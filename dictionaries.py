
mystuff = {"key1":123, 'key2':'value2','key3':{'123':[1,2,'grab Me']}}
print(mystuff)
print(mystuff['key2'])
print(mystuff['key3']['123'][2].upper())  #Result GRAB ME

food_list = {'lunch':'Pizza','bfast':'eggs'}
food_list['bfast'] = 'parata'
food_list['dinner'] = 'Pasta'
print(food_list['dinner'])
print(food_list)

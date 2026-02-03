#prints a dictionary 
def dict_display(key, dic_name):
    # print the dictionary key (e.g., character name)
    print(f"{key}:")
    dic = dic_name[key]
    for i in dic:
        if isinstance(dic[i], dict):
            print(f"{i.capitalize()}:")
            for j in dic[i]:
                value = dic[i][j]
                # Inventory-style entries: item dict, list, or nested dict (attributes)
                if isinstance(value, dict) and 'name' in value and 'stats' in value:
                    print(f"  {j.capitalize()}: {value}")
                elif isinstance(value, list):
                    # list of strings or list of item-dicts
                    if value and isinstance(value[0], dict) and 'name' in value[0]:
                        print(f"  {j.capitalize()}: {', '.join(v for v in value)}")
                    else:
                        print(f"  {j.capitalize()}: {', '.join(str(v) for v in value) if value else 'None'}")
                elif isinstance(value, dict):
                    # nested attributes dictionary
                    print(f"  {j.capitalize()}:")
                    for k in value:
                        print(f"    {k.capitalize()}: {value[k]}")
                else:
                    print(f"  {j.capitalize()}: {value}")
        elif isinstance(dic[i], list):
            print(f"{i.capitalize()}: {', '.join(str(x) for x in dic[i]) if dic[i] else 'None'}")
        elif isinstance(dic[i], set):
            print(f"{i.capitalize()}: {', '.join(dic[i]) if dic[i] else 'None'}")
        else:
            print(f"{i.capitalize()}: {dic[i]}")
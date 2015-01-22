import sys

# site_id,site_domain,site_category,app_id,app_domain,app_category,device_id,device_ip,device_model
def main():
    i = 0
    feature_lists = {"site_id_list": [], "site_domain_list": [], "site_category_list": [], \
                     "app_id_list": [], "app_domain_list": [], "app_category_list": [], \
                     "device_id_list": [], "device_ip_list": [], "device_model_list": []}
    with open(sys.argv[1], 'r') as f:
        for line in f:
            if i:
                elem_list = line.split(',')
                feature_lists["site_id_list"].append(elem_list[5])
                feature_lists["site_domain_list"].append(elem_list[6])
                feature_lists["site_category_list"].append(elem_list[7])
                feature_lists["app_id_list"].append(elem_list[8])
                feature_lists["app_domain_list"].append(elem_list[9])
                feature_lists["app_category_list"].append(elem_list[10])
                feature_lists["device_id_list"].append(elem_list[11])
                feature_lists["device_ip_list"].append(elem_list[12])
                feature_lists["device_model_list"].append(elem_list[13])
            i += 1

    print "Encoding for each feature"
    print
    for list_name in feature_lists:
        feature_lists[list_name] = list(set(feature_lists[list_name]))
        print list_name
        print
        for id, elem in enumerate(feature_lists[list_name]):
            print "{0}, {1}".format(elem, id)
        print

if __name__ == "__main__":
    main()

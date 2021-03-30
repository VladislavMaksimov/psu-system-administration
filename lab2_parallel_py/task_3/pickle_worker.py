import pickle

def write_pickle(my_list, filename):
    with open(filename, 'wb') as file:
        pickle.dump(my_list, file)

def read_pickle(filename):
    try:
        with open(filename, 'rb') as file:
            my_list = pickle.load(file)
            return my_list
    except Exception as e:
        print(e)
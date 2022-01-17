def rename_file() :
    
    #old_files_path = "C:/Users/acer/Desktop/Mini_hackathon_workingspace/SUPERAI2_HACK1_datasets/train_data/0123456789"
    #new_files_path = ""

    path = "C:/Users/acer/Desktop/Mini_hackathon_workingspace/SUPERAI2_HACK1_datasets/train_data/0123456789"
    files = os.listdir(path)
    
    for index, file in enumerate(files):
        os.rename(os.path.join(path, file), os.path.join(path, ''.join(["0123456789_" + str(index), '.jpg'])))
        #print(file)

    print("done !")

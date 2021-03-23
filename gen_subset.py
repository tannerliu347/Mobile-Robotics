
import subset_gen
#folder_name, label_file,  train_freq, test_freq, tail_str, name_timestep_len, accuracy=1e-5
#gen = subset_gen.Subset('/home/eecs568/eecs568/new_version/Mobile-Robotics/lu_data/', '/home/eecs568/eecs568/new_version/Mobile-Robotics/lu_data/dataset.csv', 4, 8, '.png', 19, 1e-2)
gen = subset_gen.Subset('./2012-03-31/lb3/Cam0', './2012-03-31/lb3/groundtruth_2012-03-31.csv', 7, 4, '.tiff', 12, 1e-5)
#gen = subset_gen.Subset('/home/eecs568/eecs568/new_version/Mobile-Robotics/nclt_01_18/', '/home/eecs568/Documents/groundtruth_2012-01-08.csv', 10, 1, '.tiff', 12, 1e-5)

#               is_euler, is_train, is_test
gen.gen_subset(True,      True,      True)  

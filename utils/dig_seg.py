import cv2
import matplotlib.pyplot as plt

# Create function to do digits segmentation and preprocessing our data

def split_digits(image):

    image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

    # Extract the index of pixel that have black(0) in it 
    crop_1=[]
    index_1 = 0
    for i in image:
        if 0 in i:
           crop_1.append(index_1)
        index_1 += 1

    # Extract the discontiuity in the image (digit-whitespace-digit-...)
    crop_2 = []
    index_2 = 0
    for num in crop_1:

        if num != crop_1[index_2-1] + 1:
            crop_2.append(crop_1[index_2-1])
            crop_2.append(num)

        index_2 += 1

    crop_2 = sorted(crop_2)

    total_digits = len(crop_2) / 2
    total_digits = int(total_digits)

    return crop_2

def pre_processing(image) : 

    # Image preprocessing : 
    image = cv2.fastNlMeansDenoisingColored(image,None,10,10,7,21)
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    res,thresh = cv2.threshold(gray,150,255,cv2.THRESH_BINARY_INV) #threshold 
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3)) 

    dilated = cv2.dilate(thresh,kernel,iterations = 3) 

    #print(dilated.shape)

    #cv2.imshow('windows', ~dilated)
    #cv2.waitKey(0)

    tar_image =  ~dilated

    return tar_image


if __name__ == "__main__" :

    #number_of_images = 113
    save_path = "C:/Users/acer/Desktop/Mini_hackathon_workingspace/SUPERAI2_HACK1_datasets/train_data/train_data_crop/"
    change_num_here = 121
    num_data = change_num_here
    for i in range(change_num_here, change_num_here + 10) : 
        image = cv2.imread("C:/Users/acer/Desktop/Mini_hackathon_workingspace/SUPERAI2_HACK1_datasets/train_data/0123456789/0123456789_%s.jpg" %i) 
        
        tar_image = pre_processing(image)
    
        result = split_digits(tar_image)

        total_digits = len(result) // 2
        total_digits = int(total_digits)
        print(total_digits)

        a = 0
        b = 1
        
        for k in range(0, total_digits):
            rot_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
            crop_image = rot_image[result[a]:result[b]]
            org_image = cv2.rotate(crop_image, cv2.ROTATE_90_COUNTERCLOCKWISE)
            cv2.imwrite(save_path + str(k) + "_%s.jpg" %num_data, org_image)
            

            a += 2
            b += 2
        num_data += 1
        
        print("image {} of {}".format(i, change_num_here + 10))
    
print("done !")

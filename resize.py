import cv2
import os 

def resize_images(input_folder, out_folder ,img_name , scale_percent):
    #scale_percent = percent of original size
    input_path = input_folder+'/'+img_name
    image = cv2.imread(input_path)
    width_new = int(image.shape[1] * scale_percent)
    height_new = int(image.shape[0] * scale_percent)
    dim = (width_new,height_new)

    resize_image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

    # reset name
    img_name , img_type = img_name.split(".")
    out_path = out_folder+'/'+img_name  + "INTER_AREA" + "." + img_type
    cv2.imwrite( out_path, resize_image )

    resize_image = cv2.resize(image, dim, interpolation=cv2.INTER_LINEAR )

    # reset name
    out_path = out_folder+'/'+img_name  + "INTER_LINEAR " + "." + img_type
    cv2.imwrite( out_path, resize_image )

    resize_image = cv2.resize(image, dim, interpolation=cv2.INTER_NEAREST )

    # reset name
    out_path = out_folder+'/'+img_name  + "INTER_NEAREST " + "." + img_type
    cv2.imwrite( out_path, resize_image )

    resize_image = cv2.resize(image, dim, interpolation=cv2.INTER_CUBIC )

    # reset name
    out_path = out_folder+'/'+img_name  + "INTER_CUBIC " + "." + img_type
    cv2.imwrite( out_path, resize_image )

    resize_image = cv2.resize(image, dim, interpolation=cv2.INTER_LANCZOS4 )

    # reset name
    out_path = out_folder+'/'+img_name  + "INTER_LANCZOS4 " + "." + img_type
    cv2.imwrite( out_path, resize_image )

if __name__=='__main__':
    input_folder = r'datasets\compare_input'
    out_folder = r'datasets\compare'
    files= os.listdir(input_folder)
    for idx in range(len(files)):
        resize_images( input_folder ,out_folder , files[idx] , (1/3))
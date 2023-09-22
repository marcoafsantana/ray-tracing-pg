def convert_to_jpg(file_name="test"):
    import os 
    import cv2

    cwd = os.getcwd()
    input_dir = os.path.join(cwd, f"{file_name}.ppm")    

    cv2.imwrite("test.png", cv2.imread(input_dir))
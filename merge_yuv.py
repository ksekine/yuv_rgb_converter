'''
Merge separated YUV images to RGB images.
Load directory must have y, u and v subdirectory.
'''
import os
import glob
import cv2
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--load_dir', type=str, required=True, help='input dir that contains yuv images')
    parser.add_argument('--save_dir', type=str, required=True, help='output dir that saves rgb images')
    args = parser.parse_args()

    y_dir = os.path.join(args.load_dir, 'y')
    u_dir = os.path.join(args.load_dir, 'u')
    v_dir = os.path.join(args.load_dir, 'v')

    y_files = sorted(glob.glob(os.path.join(y_dir, '*.png')))
    
    for y_file in y_files:
        file_name = os.path.basename(y_file)
        
        y = cv2.imread(y_file, cv2.IMREAD_GRAYSCALE)
        u = cv2.imread(os.path.join(u_dir, file_name), cv2.IMREAD_GRAYSCALE)
        v = cv2.imread(os.path.join(v_dir, file_name), cv2.IMREAD_GRAYSCALE)

        yuv = cv2.merge([y, u, v])
        bgr = cv2.cvtColor(yuv, cv2.COLOR_YUV2BGR)

        if not os.path.exists(args.save_dir):
            os.makedirs(args.save_dir)

        cv2.imwrite(os.path.join(args.save_dir, file_name), bgr)

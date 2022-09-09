'''
Convert RGB images to YUV images
and save each channel separately
'''
import cv2
import os
import glob
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--load_dir', type=str, required=True, help='input dir that contains rgb images')
    parser.add_argument('--save_dir', type=str, required=True, help='output dir that saves y, u and v images')
    args = parser.parse_args()

    files = sorted(glob.glob(os.path.join(args.load_dir, '*.png')))
    for file in files:
        img = cv2.imread(file)
        img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
        y, u, v = cv2.split(img_yuv)

        y_dir = os.path.join(args.save_dir, 'y')
        u_dir = os.path.join(args.save_dir, 'u')
        v_dir = os.path.join(args.save_dir, 'v')

        if not os.path.exists(y_dir):
            os.makedirs(y_dir)
        if not os.path.exists(u_dir):
            os.makedirs(u_dir)
        if not os.path.exists(v_dir):
            os.makedirs(v_dir)

        file_name = os.path.basename(file)
        cv2.imwrite(os.path.join(y_dir, file_name), y)
        cv2.imwrite(os.path.join(u_dir, file_name), u)
        cv2.imwrite(os.path.join(v_dir, file_name), v)

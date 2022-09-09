'''
Convert YUV_420_888 (NV21) to RGB image

- Xioami Mi 11
  width = 5920
  height = 2664
  stride = 5952

- Google Pixel 6
  width = 4080
  height = 3072
  stride = 4080

- Galaxy S8
  width = 4032
  height = 3024
  stride = 4032
'''
import numpy as np
import cv2
import glob
import os
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--load_dir', type=str, required=True, help='input dir that contains yuv images')
    parser.add_argument('--save_dir', type=str, required=True, help='output dir that saves rgb images')
    parser.add_argument('--width', type=int, required=True, help='input image width')
    parser.add_argument('--height', type=int, required=True, help='input image height')
    parser.add_argument('--stride', type=int, required=True, help='input image stride')
    args = parser.parse_args()

    imgs = sorted(glob.glob(os.path.join(args.load_dir, '*.yuv')))
    if not os.path.exists(args.save_dir):
        os.makedirs(args.save_dir)

    for fname in imgs:
        basename = os.path.basename(fname)
        filename, _ = os.path.splitext(basename)

        yuv_file = open(fname, 'rb')
        frame_len = args.stride * args.height * 1.5
        shape = (int(args.height * 1.5), args.stride)
        raw = yuv_file.read(int(frame_len))
        yuv = np.frombuffer(raw, dtype=np.uint8)
        yuv = yuv.reshape(shape)

        bgr = cv2.cvtColor(yuv, cv2.COLOR_YUV2BGR_NV21)
        bgr = bgr[:, 0:args.width]
        cv2.imwrite(os.path.join(args.save_dir, filename + '.png'), bgr)

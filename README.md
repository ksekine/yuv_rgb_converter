# YUV / RGB converter  

Set environment  

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Convert YUV_420_888 (NV21) to RGB  

```
python yuv2rgb.py --load_dir [LOAD_DIR] --save_dir [SAVE_DIR] --width [IMAGE WIDTH] --height [IMAGE HEIGHT] --stride [IMAGE STRIDE]
```

Convert RGB to separated YUV  

```
python rgb2yuv.py --load_dir [LOAD_DIR] --save_dir [SAVE_DIR]
```

Merge separated YUV to RGB  

```
python merge_yuv.py --load_dir [LOAD_DIR] --save_dir [SAVE_DIR]
```

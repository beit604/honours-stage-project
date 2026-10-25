"""
qwop_vision.py —— 精简版：仅屏幕图像提取
功能: 截取屏幕指定区域(ROI),支持实时预览窗口和保存 PNG

依赖: pip install mss opencv-python numpy
用法:
    python qwop_vision.py                # 实时预览 ROI 画面,按 Esc 退出
    python qwop_vision.py out.png        # 截取一帧保存为图片后退出

完整版(含距离读数/姿态提取/摔倒检测)备份在 qwop_vision_full.py
"""
import sys
import time

import cv2
import mss
import numpy as np


# ----------------------------------------------------------------------
# 配置 —— 截取区域在屏幕上的位置 (left, top, width, height)
# 改 left/top 移动拍摄位置,改 width/height 调整画面大小
# ----------------------------------------------------------------------
ROI = dict(left=800, top=150, width=900, height=490)


def grab() -> np.ndarray:
    """截取 ROI 区域,返回 BGR 图像 (H, W, 3)"""
    with mss.MSS() as sct:
        shot = np.asarray(sct.grab(ROI))   # BGRA
    return cv2.cvtColor(shot, cv2.COLOR_BGRA2BGR)


def preview():
    """实时预览窗口:持续显示截取画面,按 Esc 退出"""
    win = "qwop preview"
    cv2.namedWindow(win)
    print("预览窗口已打开,按 Esc 退出", flush=True)
    start = time.time()
    while True:
        frame = grab()
        cv2.imshow(win, frame)
        if cv2.waitKey(1) & 0xFF == 27:                   # Esc 退出
            break
        # 给窗口 2 秒创建时间,之后再检查是否被点关闭按钮
        if time.time() - start > 2:
            if cv2.getWindowProperty(win, cv2.WND_PROP_VISIBLE) < 1:
                break
    cv2.destroyAllWindows()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        out_path = sys.argv[1]
        frame = grab()
        cv2.imwrite(out_path, frame)
        print(f"已截取 {frame.shape[1]}x{frame.shape[0]} 图像 -> {out_path}")
    else:
        preview()

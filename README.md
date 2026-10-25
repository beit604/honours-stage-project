# Honours Stage Project

University of Hull — Honours Stage Project repository.

## Contents

- `qwop_vision.py` — Screen ROI capture utility for the QWOP game project. Uses `mss` + OpenCV to grab a configurable region of the screen, supports live preview and single-frame PNG export.

## Requirements

```
pip install mss opencv-python numpy
```

## Usage

```
python qwop_vision.py                # live preview of ROI, press Esc to exit
python qwop_vision.py out.png        # capture one frame and save as PNG
```

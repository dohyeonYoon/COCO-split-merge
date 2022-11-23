# COCO-split-merge

This code divides the coco format segmentation json file into individual json files according to the file name,
and merges only the desired files into one json file.

![그림2](https://user-images.githubusercontent.com/66056440/203495919-7f3c8748-fc67-4f48-80c4-940145004bf3.jpg)



## :heavy_check_mark: Tested

| Python |   Windows   |   Mac   |   Linux  |
| :----: | :---------: | :-----: | :------: |
|  3.8  | windows10 | Proceeding |  Proceeding |


## :arrow_down: Installation

Clone repo and install [requirements.txt](https://github.com/dohyeonYoon/COCO-split-merge/blob/main/requirements.txt) in a
**Python>=3.8.0** environment

```bash
git clone https://github.com/dohyeonYoon/COCO-split-merge  # clone
cd COCO-split-merge
pip install -r requirements.txt  # install
```

## :rocket: Getting started

You can split the desired json file into individual json files according to the file name 
and optionally merge them again.

```bash
cd src
python coco_json_split
python coco_json_merge
python coco_json_edit(optional)
```

## 🚫 Caution

This code only works for coco format segmentation json file.

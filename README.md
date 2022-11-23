# COCO-split-merge

This code divides the coco format segmentation json file into individual json files according to the file name,
and merges only the desired files into one json file.

![그림1](https://user-images.githubusercontent.com/66056440/203495399-3f310719-8c29-43ba-a970-cefadc3ddf66.jpg)


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

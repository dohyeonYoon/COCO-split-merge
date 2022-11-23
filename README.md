# COCO-split-merge

This code divides the coco format segmentation json file into individual json files according to the file name,
and merges only the desired files into one json file.

## :heavy_check_mark: Tested

| Python |   Windows   |   Mac   |   Linux  |
| :----: | :---------: | :-----: | :------: |
|  3.8  | windows10 | Proceeding |  Proceeding |


## :arrow_down: Installation

Clone repo and install [requirements.txt](https://github.com/dohyeonYoon/License-plate-generater/requirements.txt) in a
**Python>=3.8.0** environment

```bash
git clone https://github.com/dohyeonYoon/License-plate-generater  # clone
cd License-plate-generater
pip install -r requirements.txt  # install
```

## :rocket: Getting started

You can generate Korean motorcycle license plate format jpg file in output folder.

```bash
python main.py -n 100 
```

-n : 생성하고자 하는 데이터셋 개수, default=100 <br/>
-i : save directory, default=./output/image/ <br/>
-s : save 여부, default=True

## :link: Dataset
[행정구역 데이터셋](https://drive.google.com/file/d/1-QBeNquEbhvqfj5IrQpLDPqQF7BFRW85/view?usp=sharing) 

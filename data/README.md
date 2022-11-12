# Datasets

This page gives an overview of all datasets, which are actively used in this project. 


## Overview

| Name           | Resolution       | Channels | #Images | #Classes | Task\* | Ref.                                                                                                                                               |
|----------------|------------------|----------|---------|----------|--------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| EuroSAT        | 256x256          | Sen-2    | 27,000  | 10       | C      | [Source](https://github.com/phelber/eurosat), [P1](https://doi.org/10.1109/JSTARS.2019.2918242), [P2](https://doi.org/10.1109/IGARSS.2018.8519248) |
| AID            | 600x600          | RGB      | 10,00   | 30       | C      | [Source](https://captain-whu.github.io/AID/), [P1](https://doi.org/10.1109/TGRS.2017.2685945)                                                      |
| UC-Merced      | 256x256          | RGB      | 2,100   | 21       | C      | [Source](http://weegee.vision.ucmerced.edu/datasets/landuse.html), [P1](https://doi.org/10.1145/1869790.1869829)                                   |
| Resisc45       | 256x256          | RGB      | 31,500  | 45       | C      | [P1](https://doi.org/10.1109/JPROC.2017.2675998)                                                                                                   |
| RSI-CB256      | 256x256          | RGB      | 24,000  | 35       | C      | [Source](https://github.com/lehaifeng/RSI-CB), [P1](https://doi.org/10.3390/s20061594)                                                             |

\* C - Classification, S - Segmentation, CD - Change Detection <br/>
\** Multi-label 


## Detailes Descriptions


### EuroSAT
The EuroSAT dataset is composed of aerial image tiles showing varying land-use classes in RGB colors as well as with multispectral bands.

*Key Features:*
* Number of images: 27.000
* Number of classes: 10
* Label type: single label
* geo-referenced: Yes
* Image resolution: 256x256 pixels

[Source](https://github.com/phelber/eurosat), [Paper no. 1](https://doi.org/10.1109/JSTARS.2019.2918242), [Paper no. 2](https://doi.org/10.1109/IGARSS.2018.8519248)

### UC-Merced Land Use Dataset
The UC-Merced Land Use Dataset is composed of aerial image tiles showing varying land-use classes.

*Key Features:*
* Number of images: 2100
* Number of classes: 21
* Label type: single label
* geo-referenced: No
* Image resolution: 256x256 pixels

[Source](http://weegee.vision.ucmerced.edu/datasets/landuse.html), [Paper](https://doi.org/10.1145/1869790.1869829)

### AID
The AID (Aerial Scene Classification) Dataset is composed of aerial image tiles showing varying land-use classes.

*Key Features:*
* Number of images: 10.000
* Number of classes: 30
* Label type: single label
* geo-referenced: TBD
* Image resolution: 600x600 pixels

[Source](https://captain-whu.github.io/AID/), [Paper](https://doi.org/10.1109/TGRS.2017.2685945)

### Resisc45
The Resisc45 Dataset is composed of aerial image tiles showing varying land-use classes.

Website is currently down. - 19.7.2022

*Key Features:*
* Number of images: 31.500
* Number of classes: 45
* Label type: single label
* geo-referenced: No
* Image resolution: 256x256 pixels

[Paper](https://doi.org/10.1109/JPROC.2017.2675998)

### RSI-CB256
The RSI-CB256 Dataset is composed of aerial image tiles showing varying land-use classes.

Info: This dataset does also exist with the resolution 128 x 128 pixels (RSI-CB128).

*Key Features:*
* Number of images: 24.000
* Number of classes: 35
* Label type: single label
* geo-referenced: No
* Image resolution: 256x256 pixels

[Source](https://github.com/lehaifeng/RSI-CB), [Paper](https://doi.org/10.3390/s20061594)
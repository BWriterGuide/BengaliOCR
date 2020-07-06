# BengaliOCR 
This repository contains the implementation of BengaliOCR system and preprocessing.

# Pre Process:
  ## Page Cropper
  This pre-process technique cut out the unwanted background portion and extract the written area from the image.
  
  `Run "Book_Page_Cropper.ipynb" Notebook to perform page cropping process.`
  
`INPUT`
![1](https://user-images.githubusercontent.com/16709991/83765475-0a3bf800-a69d-11ea-8ab7-d0e75fa502d7.png)
`OUTPUT`
![Res_4_re(2048)](https://user-images.githubusercontent.com/16709991/83765489-0d36e880-a69d-11ea-9fe2-6ef598d7c4d8.png)


  ## Multi Colored Text Enhancement
  Some text lines are difficult or impossible to recognize when text is colorful. 
  So this pre-processing teqhnique is based on intelligent binarization and image color processing.
  It enhances the color text lines and convert the color and greyscale images into black-and-white images successfully.
  
  `Run "Multi_Colored_Text_Enhancement.ipynb" Notebook to perform colored text transformation process.`
  
`INPUT`

![image](https://user-images.githubusercontent.com/16709991/83763859-014a2700-a69b-11ea-9b09-18c9b9d59164.png)

`OUTPUT`

![image](https://user-images.githubusercontent.com/16709991/83763889-0c04bc00-a69b-11ea-9a7e-8565c1df6cd2.png)

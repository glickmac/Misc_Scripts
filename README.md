# Tutorials
This repository contain useful scripts and demos that I have completed throughout the years. 

### Useful Command Line Scripts
This chunk contains useful command line scripts for text processing

- Remove first line from a file inplace
```
sed -i '1d' filename
```


### Running Photo Mosaic Script 
- Download images and photo mosaic image to use 

- Use Test script to check if image library contains images with at least three dimensions
```python Mosaic_Test.py```

- Options of Mosaic.py

Smaller the grid size, larger the inserted images

```
python Mosaic.py --target-image image_to_use --reuse-image True --input-folder images/ --grid-size 64 64
```


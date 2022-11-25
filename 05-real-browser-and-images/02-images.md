# Images

## Downloading Images

### Basic file downloads

Here's a basic function you can paste into a script that will download any file based on its URL. 


```python
def download_file(url, local_filename=None):
    """
    Downloads a file from a remote URL
    """
    if local_filename is None:
        local_filename = url.split("/")[-1]
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename
```

To use simply pass in a URL you want to download, like so:

```python
download_file("https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Rosa_Luxemburg.jpg/440px-Rosa_Luxemburg.jpg")
```

By default, the function will save the image into the same folder as your python script, using the name of the image from the url. You can also enter a name to save the image to by including a second argument:

```python
download_file("https://cool.images/goodpicture.jpg", "mycoolpic.jpg")
```


### Bing

Microsoft's Bing is a good resource if you'd like to download a bunch of images. You can definitely write your own scraper for this, or use an existing library like `bing-image-downloader`.

To install: 

```
pip3 install bing-image-downloader
```

To use:

```python
from bing_image_downloader import downloader


downloader.download(
    "Rosa Luxemburg",
    limit=100,
    output_dir="dataset",
    adult_filter_off=True,
    force_replace=False,
    timeout=60,
)
```

### Instagram

For Instagram downloads, I recommend the following command line application:

[https://github.com/arc298/instagram-scraper/](https://github.com/arc298/instagram-scraper/
)

*Note: This actually isn't working at the moment!*

Install:

```
pip3 install instagram-scraper
```

To use, you'll need to provide an instagram username and password. In this example I've created a fake instagram user named "karlmarx4201".

This example downloads all media, including location data, from the "samlavigne" account, first logging in as "karlmarx4201".

```
instagram-scraper samlavigne --include-location -u karlmarx4201 -p fakeinstagrampassword!
```

This downloads everything from a particular location:

```
instagram-scraper --location 2371720 --include-location --maximum 10  -u karlmarx4201 -p fakeinstagrampassword!
```

And this downloads everything tagged "karlmarx"

```
instagram-scraper --tag karlmarx --include-location --maximum 10  -u karlmarx4201 -p fakeinstagrampassword!
```


### Flickr

I've written a python script to download images from Flickr that you can grab from:

[https://github.com/antiboredom/flickr-scrape/](https://github.com/antiboredom/flickr-scrape/)

Instructions are provided in the github readme.



## Manipulating Images

### Imagemagick

https://legacy.imagemagick.org/Usage/basics/

```
brew install imagemagick
sudo apt-get install imagemagick
```

```
 convert image.jpg image.png
 convert image.png -resize 50% image2.png
 convert image.png -resize 640x480 image2.png
```

```
-crop  -repage  -border  -frame  -trim  -chop  -draw  -annotate  -resize  -scale  -sample  -thumbnail  -magnify  -adaptive-resize  -liquid-resize  -distort  -morpohology  -sparse-color  -rotate  -swirl  -implode  -wave  -flip  -flop  -transpose  -transverse  -blur  -gaussian-blur  -convolve  -shadow  --radial-blur  -motion-blur  -sharpen  -unsharp  -adaptive-sharpen  -adaptive-blur  -noise  -despeckle  -median  -negate  -level  -level-color  -gamma  -auto-level  -auto-gamma  -sigmoidial-contrast  -normalize  -linear-stretch  -contrast-stretch  -colorize  -tint  -modulate  -contrast  -equalize  -sepia-tone  -solarize  -recolor  -opaque  -transparent  -colors  -map  -ordered-dither  -random-dither  -raise  -paint  -sketch  -charcoal  -edge  -vignette  -emboss  -shade  -poloroid  -encipher  -decipher  -stegano  -evaluate  -function  -alpha  -colorspace  -separate
```

```
montage -tile 2x0 -geometry 200x200+5+50 -border 10 *.png out.png
```


### Faces

```
pip install opencv-python
```

```
python image_faces.py *.jpg
```

### objects

download these files:

* https://pjreddie.com/media/files/yolov3.weights
* https://raw.githubusercontent.com/opencv/opencv_extra/master/testdata/dnn/yolov3.cfg
* https://raw.githubusercontent.com/nandinib1999/object-detection-yolo-opencv/master/coco.names

then run:

```
python image_detect_objects.py IMAGE.jpg
```

### Turn a folder of images into a website

```
python3 create_image_website.py foldername > image_archive.html
```

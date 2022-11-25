from bing_image_downloader import downloader


downloader.download(
    "Jeff Bezos",
    limit=100,
    output_dir="bingimages",
    adult_filter_off=False,
    force_replace=False,
    timeout=60,
)

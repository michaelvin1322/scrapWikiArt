ITEM_PIPELINES = {
    'scrapy.pipelines.images.ImagesPipeline': 1,
}

IMAGE_STORES = "data/img"

DOWNLOADER_MIDDLEWARES = {
    'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
    'rotating_proxies.middlewares.BanDetectionMiddleware': 620,
}

ROTATING_PROXY_LIST_PATH = "proxy_list.txt"

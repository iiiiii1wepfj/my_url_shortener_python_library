import setuptools

with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="urlshortlib",
    version="1",
    author="Itay K",
    author_email="itayki98@gmail.com",
    description="A Python Wrapper for s.itayki.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/iiiiii1wepfj/my_url_shortener_python_library",
    packages=setuptools.find_packages(),
    download_url = 'https://github.com/iiiiii1wepfj/my_url_shortener_python_library/archive/refs/tags/v1.tar.gz',
    project_urls={'Documentation': 'https://s.itayki.com/docs', 'Source': 'https://github.com/iiiiii1wepfj/my_url_shortener_python_library'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "httpx[http2]",
    ],
)

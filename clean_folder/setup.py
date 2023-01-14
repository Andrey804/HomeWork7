from setuptools import setup

setup(
    name="clean_folder",
    version="1",
    author="Andrey",
    author_email="reydigls@gmail.com",
    description="Cleaning script",
    long_description="This is our the very usefull programm",
    url="",
    classifiers=[
        "Python version :: Python :: 3",
        "Licence :: OSI Approved :: MIT Licence",
        "Operating System :: Windows :: Linux :: Mac"
    ],
    packages=["clean_folder"],
    python_requires=">=3.7",
    entry_points={'console_scripts': ['clean-folder = clean_folder.clean:main']}
)

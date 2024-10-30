from setuptools import setup, find_namespace_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='detr',
    version='0.11.0',
    description='Final implementation of DETR a visual transformer for object detection and recognition',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Facebook AI Research',
    author_email='info@bazaro.io',  # Optional
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
    ],

    keywords='detr, object recognition, facebook',  # Optional

    package_dir={'': 'src'},

    package_data={
    },

    # You can just specify package directories manually here if your project is
    # simple. Or you can use find_packages().
    #
    # Alternatively, if you just want to distribute a single Python file, use
    # the `py_modules` argument instead as follows, which will expect a file
    # called `my_module.py` to exist:
    #
    #   py_modules=["my_module"],
    #
    packages=find_namespace_packages(where='src'),  # Required

    python_requires='>=3.10, <4',

    install_requires=['cython',
                      'submitit',
                      'torch>=1.5.0',
                      'torchvision>=0.6.0',
                      'scipy',
                      'onnx',
                      'onnxruntime',
                      'pycocotools',
                      # 'pycocotools@git+https://github.com/cocodataset/cocoapi.git#subdirectory=PythonAPI&egg=pycocotools',
                      # 'panopticapi@git+https://github.com/cocodataset/panopticapi.git#egg=panopticapi'
                      ]
    # ,
    # dependency_links=[
    #     'git+https://github.com/cocodataset/cocoapi.git#subdirectory=PythonAPI&egg=pycocotools',
    #     'git+https://github.com/cocodataset/panopticapi.git#egg=panopticapi'
    # ]
)

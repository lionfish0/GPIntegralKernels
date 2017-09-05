from distutils.core import setup
setup(
  name = 'GPIntegralKernels',
  packages = ['GPIntegralKernels'], # this must be the same as the name above
  version = '1.01',
  description = 'A python module containing kernels for GPy to perform integral computations.',
  author = 'Mike Smith',
  author_email = 'm.t.smith@sheffield.ac.uk',
  url = 'https://github.com/lionfish0/GPIntegralKernels.git',
  download_url = 'https://github.com/lionfish0/GPIntegralKernels/archive/1.01.tar.gz',
  keywords = ['gaussian processes'],
  classifiers = [],
  install_requires=['GPy','numpy'],
)

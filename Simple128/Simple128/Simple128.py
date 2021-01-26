"""Simple128 dataset."""

import tensorflow_datasets as tfds

# TODO(Simple128): Markdown description  that will appear on the catalog page.
_DESCRIPTION = """
## Contains 128 images of simple drawings (included all OneLine45)
"""

# TODO(Simple128): BibTeX citation
_CITATION = """
"""


class Simple128(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for Simple128 dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    # TODO(Simple128): Specifies the tfds.core.DatasetInfo object
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            # These are the features of your dataset like images, labels ...
            'image': tfds.features.Image(shape=(512, 512, 1))
        }),
        # If there's a common (input, target) tuple from the
        # features, specify them here. They'll be used if
        # `as_supervised=True` in `builder.as_dataset`.
        supervised_keys=(None),  # Set to `None` to disable
        homepage='https://dataset-homepage/',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    # TODO(Simple128): Downloads the data and defines the splits
    path = dl_manager.download_and_extract('https://github.com/drawwithai/Dataset/raw/main/Simple128/Simple128.zip')

    # TODO(Simple128): Returns the Dict[split names, Iterator[Key, Example]]
    return {
        'train': self._generate_examples(path / 'Simple_train'),
    }

  def _generate_examples(self, path):
    """Yields examples."""
    # TODO(Simple128): Yields (key, example) tuples from the dataset
    for f in path.glob('*.jpg'):
      yield f.name, {
          'image': f,
      }

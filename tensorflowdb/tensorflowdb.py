"""tensorflowdb dataset."""

import tensorflow_datasets as tfds

# TODO(tensorflowdb): Markdown description  that will appear on the catalog page.
_DESCRIPTION = """
#Dataset used for initial tests
"""

# TODO(tensorflowdb): BibTeX citation
_CITATION = """
"""


class Tensorflowdb(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for tensorflowdb dataset."""

  VERSION = tfds.core.Version('1.0.1')
  RELEASE_NOTES = {
      '1.0.1': 'Initial release.',
  }
  MANUAL_DOWNLOAD_INSTRUCTIONS = "Download FormatedImages.zip"

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    # TODO(tensorflowdb): Specifies the tfds.core.DatasetInfo object
    return tfds.core.DatasetInfo(
        builder=self,
        description=_DESCRIPTION,
        features=tfds.features.FeaturesDict({
            # These are the features of your dataset like images, labels ...
            'image': tfds.features.Image(shape=(512, 512, 1)),
            'label': tfds.features.ClassLabel(names=['no', 'yes']),
        }),
        # If there's a common (input, target) tuple from the
        # features, specify them here. They'll be used if
        # `as_supervised=True` in `builder.as_dataset`.
        supervised_keys=('image', 'label'),  # Set to `None` to disable
        homepage='https://dataset-homepage/',
        citation=_CITATION,
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    # TODO(tensorflowdb): Downloads the data and defines the splits
    path = dl_manager.download_and_extract('https://github.com/drawwithai/Dataset/raw/main/FormatedImages.zip')

    # TODO(tensorflowdb): Returns the Dict[split names, Iterator[Key, Example]]
    return {
        'train': self._generate_examples(path / "FormatedImages"),
    }

  def _generate_examples(self, path):
    """Yields examples."""
    # TODO(tensorflowdb): Yields (key, example) tuples from the dataset
    for f in path.glob('*.jpg'):
      yield str(f), {
          'image': f,
          'label': 'yes',
      }

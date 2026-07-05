from whitenoise.storage import CompressedStaticFilesStorage


class PatchedStaticFilesStorage(CompressedStaticFilesStorage):
    """
    Storage personnalisé qui ignore les FileNotFoundError de WhiteNoise
    (bug connu avec Django 4.2 et certains fichiers admin sans extension)
    """

    def post_process(self, paths, dry_run=False, **options):
        try:
            yield from super().post_process(paths, dry_run, **options)
        except FileNotFoundError:
            pass

    def _compress_path(self, path):
        try:
            yield from super()._compress_path(path)
        except FileNotFoundError:
            return

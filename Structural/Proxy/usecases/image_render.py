class Bitmap:
    def __init__(self, filename: str):
        self.filename = filename
        print(f"Load image from {self.filename}!")

    def draw(self):
        print(f"Drawing image {self.filename}")

    def __del__(self):
        print("destroy the bitmap image!")


class LazyBitmap:
    def __init__(self, filename: str):
        self.filename = filename
        self.bitmap = (
            None  # In order to not load an image which is not supposed to be rendered.
        )

    def draw(self):
        if not self.bitmap:
            self.bitmap = Bitmap(self.filename)
        self.bitmap.draw()

    def __del__(self):
        if self.bitmap:
            print("destroy the lazy_bitmap image!")


if __name__ == "__main__":
    bmp = Bitmap("a_bitmap_image.jpg")  # the image is already loaded
    lazy_bmp = LazyBitmap(
        "a_lazy_bitmap_image.jpg"
    )  # The image is not loaded in this step
    lazy_bmp.draw()

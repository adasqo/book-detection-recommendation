import cv2

class ImageManager:

    @staticmethod
    def load_image(image_path):
        return cv2.imread(image_path)

    @staticmethod
    def show_image(image):
        cv2.imshow("img", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    @staticmethod
    def convert_to_grayscale(image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    @staticmethod
    def save_image(image, path):	
        cv2.imwrite(path, image) 

    @staticmethod
    def rotate_image(image, angle):
        return cv2.rotate(image, angle)

    @staticmethod
    def detect_edges(image, threshold1, threshlod2):
        return cv2.Canny(image, threshold1, threshlod2)

    @staticmethod
    def blur_image(image, kernel_size):
        return cv2.blur(image, (kernel_size, kernel_size))
import os


def current_path(image_folder: str, image_file: str) -> str:
            
    """ Print the current executing file path. """
    print("====this is file execuiting folder=========")
    # print(os.path.abspath(__file__))
    print(os.path.dirname(os.path.abspath(__file__)))
    print("===========================================")
    image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 
                              image_folder,
                              image_file)
    return image_path
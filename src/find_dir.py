import os


def find_dir(level = 0, folder = "", file = "") -> str:
            
    """ Print the current executing file path. 
	
	param 
	level :
	    - 0 : current path
		- 1 : 1 upper level
        - 2 : 2 upper level
        - 3 : 3 upper level 

    folder : import할 폴더
    
    file : import 할 파일
	"""
    # print("====this is file execuiting folder=========")
    # haha = f"현재 실행 파일의 절대 경로 : {os.path.abspath(__file__)}"
    # haha = f"현재 실행 파일의 절대 dir  : {os.path.dirname(os.path.dirname(__file__))}"
    
    # prin0t(haha)
    # print(os.path.dirname(os.path.abspath(__file__)))
    # print("===========================================")

    # 1. 실행파일 1단계 상위 폴더 구하는 코드
    # ``` os.path.dirname(os.path.abspath(os.path.dirname(__file__))) ```
    # 2. 2단계 상위 폴더
    # ``` os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__)))))) ```	

    making_path = os.path.dirname(__file__)

    while level > 0:
        # if upper_level == 0:
        #     break
        making_path = os.path.dirname(making_path)
        # print(upper_level)
        level -= 1

    make_path = os.path.join(making_path, folder, file)
    return make_path

if __name__ == "__main__":
    current_path = find_dir(0)
    # current_path = test()
    # current_path = find_dir()
    print(current_path)

    
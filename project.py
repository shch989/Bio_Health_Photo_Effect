import os
import random
from PIL import Image, ImageFilter

def apply_effect(image, effect):
    if effect == 1:  # 좌우반전
        image = image.transpose(Image.FLIP_LEFT_RIGHT)
    elif effect == 2:  # 상하반전
        image = image.transpose(Image.FLIP_TOP_BOTTOM)
    elif effect == 3:  # 회전
        angle = float(input("회전할 각도를 입력하세요: "))
        image = image.rotate(angle)
    elif effect == 4:  # 흑백
        image = image.convert("L")
    elif effect == 5:  # 엠보싱
        image = image.filter(ImageFilter.EMBOSS)
    elif effect == 6:  # 스케치
        image = image.filter(ImageFilter.CONTOUR)
    elif effect == 7:  # 경계선
        image = image.filter(ImageFilter.FIND_EDGES)
    else:
        print("잘못된 입력입니다.")
    return image

# 이미지 파일이 있는 디렉토리 경로
image_directory = "img"
# 디렉토리 내의 이미지 파일 목록 가져오기
image_files = [f for f in os.listdir(image_directory) if f.endswith((".jpg", ".jpeg", ".png", ".bmp"))]
# 랜덤한 이미지 파일 선택
random_image_file = random.choice(image_files)
# 이미지 파일 경로
image_path = os.path.join(image_directory, random_image_file)
# 이미지 열기
image = Image.open(image_path)

while True:
    print("1:좌우반전, 2:상하반전, 3:회전, 4:흑백, 5:엠보싱, 6:스케치, 7:경계선, 0:종료")
    effect = int(input("원하는 효과를 선택하세요: "))
    if effect == 0:
        break
    image = apply_effect(image, effect)
    image.show()

image.close()

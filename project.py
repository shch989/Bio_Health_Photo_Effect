<<<<<<< HEAD
import random
from PIL import Image, ImageFilter, ImageOps
=======
import os
import random
from PIL import Image, ImageFilter
>>>>>>> 5fa71e686ff89791dd9f012a0cf7f7e421cf5290

def apply_effect(image, effect):
    if effect == 1:  # 좌우반전
        image = image.transpose(Image.FLIP_LEFT_RIGHT)
    elif effect == 2:  # 상하반전
        image = image.transpose(Image.FLIP_TOP_BOTTOM)
    elif effect == 3:  # 회전
<<<<<<< HEAD
        image = image.rotate(45, expand=True)
    elif effect == 4:  # 흑백
        image = ImageOps.grayscale(image)
=======
        angle = float(input("회전할 각도를 입력하세요: "))
        image = image.rotate(angle)
    elif effect == 4:  # 흑백
        image = image.convert("L")
>>>>>>> 5fa71e686ff89791dd9f012a0cf7f7e421cf5290
    elif effect == 5:  # 엠보싱
        image = image.filter(ImageFilter.EMBOSS)
    elif effect == 6:  # 스케치
        image = image.filter(ImageFilter.CONTOUR)
    elif effect == 7:  # 경계선
        image = image.filter(ImageFilter.FIND_EDGES)
    else:
        print("잘못된 입력입니다.")
    return image

<<<<<<< HEAD
# 원본 이미지 파일 경로
number = random.randint(1, 3)
if number < 10:
    number = '0' + str(number)
else:
    number = str(number)

original_image_path = 'C:/photo/picture' + number + '.jpg'

# 결과 이미지 파일 경로
output_filename = 'C:/photo/output' + number + '.jpg'

# 이미지 열기
original_image = Image.open(original_image_path)
result_image = original_image.copy()
=======
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
>>>>>>> 5fa71e686ff89791dd9f012a0cf7f7e421cf5290

while True:
    print("1:좌우반전, 2:상하반전, 3:회전, 4:흑백, 5:엠보싱, 6:스케치, 7:경계선, 0:종료")
    effect = int(input("원하는 효과를 선택하세요: "))
    if effect == 0:
        break
<<<<<<< HEAD
    
    # 효과 적용
    result_image = apply_effect(result_image, effect)
    result_image.show()
    
# 결과 이미지 저장
result_image.save(output_filename)

original_image.close()
result_image.close()
=======
    image = apply_effect(image, effect)
    image.show()

image.close()
>>>>>>> 5fa71e686ff89791dd9f012a0cf7f7e421cf5290

import os
from PIL import Image

def convert_pngs_to_pdf(input_folder, output_pdf):
    # 입력 폴더에서 PNG 파일만 필터링 (이름순 정렬)
    png_files = sorted([f for f in os.listdir(input_folder) if f.lower().endswith(".png")])

    if not png_files:
        print("No PNG files found in the input folder.")
        return

    images = []
    for file in png_files:
        img_path = os.path.join(input_folder, file)
        img = Image.open(img_path).convert("RGB")  # 투명 PNG 대비 RGB 변환
        images.append(img)

    # 첫 번째 이미지를 기준으로 PDF 생성
    images[0].save(output_pdf, save_all=True, append_images=images[1:])
    print(f"PDF saved successfully: {output_pdf}")

# 실행 예제
if __name__ == "__main__":
    input_folder = "images"  # PNG 이미지가 들어 있는 폴더
    output_pdf = "output.pdf"  # 변환된 PDF 파일 경로

    convert_pngs_to_pdf(input_folder, output_pdf)
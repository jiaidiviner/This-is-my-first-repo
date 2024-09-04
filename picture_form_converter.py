from PIL import Image, ImageFilter,ImageOps
import os
import argparse
#命令行指令：python picture_form_converter.py "C:\Users\jiaid\Pictures\Screenshots\屏幕截图 2024-09-04 165419.png" "C:\Users\jiaid\Desktop" --name "movhhh.bmp" --style "black"
def process_image(input_path, output_path,name,style):
    picture = Image.open(input_path)
    print(f"原图片的大小与类型分别为：{picture.size}和{type(picture)}")
    if name.lower().endswith(('jpg','jpeg')):
        picture_processed = picture.convert("RGB")
    else:
        picture_processed = picture
    if style != "no":
        picture_RGBA = picture.filter(ImageFilter.CONTOUR)
        picture_RGB = picture_RGBA.convert("RGB")
        print(f"转化后的类型为：{picture_RGB.mode}")
        if style == "black":
            picture_processed = ImageOps.invert(picture_RGB)
        else:
            picture_processed = picture_RGB
    if not name.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        name += '.png'
    completed_save_path = os.path.join(output_path, name)
    picture_processed.save(completed_save_path)
    print(f"文件已成功保存到{completed_save_path}")
    picture_processed.show()
    print("hahaha")
def main():
    parser = argparse.ArgumentParser(description="这是一个生成黑白风格图片的脚本")
    # 添加命令行参数
    parser.add_argument("input", help="输入图像文件的路径")
    parser.add_argument("output", help="保存处理后图像的路径")
    parser.add_argument("--name", default="processed_image.png", help="保存处理后图像的文件名（默认为 'processed_image.png'）")
    parser.add_argument("--style", default="white",help="请选择你要导出的图片风格")

    # 解析参数
    args = parser.parse_args()
    process_image(args.input, args.output, args.name,args.style)

main()
